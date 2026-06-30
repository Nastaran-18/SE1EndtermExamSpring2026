"""
Facade pattern: StreamingFacade hides AuthenticationService,
SubscriptionService, MovieCatalogService and StreamingService behind a
single requestPlayback() call, implementing the scenario view:
login -> select movie -> request -> auth + subscription check -> stream.
"""

from typing import Optional

from src.entities import Content
from src.services import (
    AuthenticationService,
    SubscriptionService,
    MovieCatalogService,
    StreamingService,
)


class PlaybackDeniedError(Exception):
    pass


class StreamingFacade:
    def __init__(
        self,
        auth_service: AuthenticationService,
        subscription_service: SubscriptionService,
        catalog_service: MovieCatalogService,
        streaming_service: StreamingService,
    ) -> None:
        self._auth = auth_service
        self._subscription = subscription_service
        self._catalog = catalog_service
        self._streaming = streaming_service

    def request_playback(self, user_id: int, content_id: int):
        if not self._auth.is_authenticated(user_id):
            raise PlaybackDeniedError("User is not authenticated")

        if not self._subscription.check_subscription(user_id):
            raise PlaybackDeniedError("User has no active subscription")

        content: Optional[Content] = self._catalog.get_movie(content_id)
        if content is None:
            raise PlaybackDeniedError("Content not found")

        return self._streaming.start_stream(content)
