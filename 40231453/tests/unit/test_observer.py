import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.patterns.observer import (
    PlaybackSession,
    ProgressBarUI,
    WatchHistoryLogger,
    RecommendationEngine,
)


def test_initial_state_is_stopped():
    session = PlaybackSession()
    assert session.state == "stopped"
    assert session.position_sec == 0


def test_play_changes_state_to_playing():
    session = PlaybackSession()
    session.play()
    assert session.state == "playing"


def test_pause_changes_state_to_paused():
    session = PlaybackSession()
    session.play()
    session.pause()
    assert session.state == "paused"


def test_observer_receives_update_on_play():
    session = PlaybackSession()
    progress_bar = ProgressBarUI()
    session.attach(progress_bar)

    session.play()

    assert progress_bar.last_position == session.position_sec


def test_multiple_observers_are_notified():
    session = PlaybackSession()
    logger = WatchHistoryLogger()
    recommender = RecommendationEngine()
    session.attach(logger)
    session.attach(recommender)

    session.play()
    session.pause()

    assert len(logger.log) == 2
    assert recommender.last_state == "paused"


def test_detach_stops_notifications():
    session = PlaybackSession()
    logger = WatchHistoryLogger()
    session.attach(logger)
    session.detach(logger)

    session.play()

    assert len(logger.log) == 0
