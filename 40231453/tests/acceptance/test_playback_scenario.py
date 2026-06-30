"""
Acceptance test for the scenario view (+1):
User logs in -> selects a movie -> request is sent to server ->
server authenticates + checks subscription -> server streams the video.
"""

import sys
import os
from datetime import date

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import pytest

from src.entities import User, Subscription, Content
from src.services import (
    AuthenticationService,
    SubscriptionService,
    MovieCatalogService,
    StreamingService,
)
from src.patterns.facade import StreamingFacade, PlaybackDeniedError


@pytest.fixture
def streaming_system():
    auth = AuthenticationService()
    subscription = SubscriptionService()
    catalog = MovieCatalogService()
    streaming = StreamingService()
    facade = StreamingFacade(auth, subscription, catalog, streaming)

    user = User(
        user_id=1,
        full_name="Nastaran",
        email="nastaran@example.com",
        password_hash="secret123",
        phone="0912xxxxxxx",
        join_date=date(2026, 1, 1),
    )
    subscription.add_subscription(
        Subscription(
            sub_id=1,
            user_id=1,
            plan_id=1,
            start_date=date(2026, 1, 1),
            end_date=date(2027, 1, 1),
            status="active",
        )
    )
    catalog.add_content(
        Content(content_id=100, title="The Matrix", type="movie", release_year=1999)
    )

    return {
        "auth": auth,
        "subscription": subscription,
        "catalog": catalog,
        "streaming": streaming,
        "facade": facade,
        "user": user,
    }


def test_full_playback_scenario_succeeds(streaming_system):
    auth = streaming_system["auth"]
    facade = streaming_system["facade"]
    user = streaming_system["user"]

    # Step 1: user logs in
    logged_in = auth.authenticate(user.user_id, "secret123", user.password_hash)
    assert logged_in is True

    # Step 2 & 3: user selects a movie and request is sent to the server
    # Step 4: server authenticates + checks subscription, then streams
    stream = facade.request_playback(user.user_id, content_id=100)

    assert stream.play() == "Playing The Matrix"


def test_playback_denied_without_login(streaming_system):
    facade = streaming_system["facade"]
    user = streaming_system["user"]

    with pytest.raises(PlaybackDeniedError):
        facade.request_playback(user.user_id, content_id=100)


def test_playback_denied_without_active_subscription(streaming_system):
    auth = streaming_system["auth"]
    subscription = streaming_system["subscription"]
    facade = streaming_system["facade"]
    user = streaming_system["user"]

    auth.authenticate(user.user_id, "secret123", user.password_hash)
    subscription._subs[user.user_id].status = "expired"

    with pytest.raises(PlaybackDeniedError):
        facade.request_playback(user.user_id, content_id=100)
