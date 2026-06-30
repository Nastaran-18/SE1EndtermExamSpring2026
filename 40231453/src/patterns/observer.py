"""Observer pattern: PlaybackSession notifies observers when state changes."""

from abc import ABC, abstractmethod
from typing import List


class PlaybackObserver(ABC):
    @abstractmethod
    def update(self, state: dict) -> None:
        raise NotImplementedError


class PlaybackSubject(ABC):
    @abstractmethod
    def attach(self, observer: PlaybackObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer: PlaybackObserver) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self) -> None:
        raise NotImplementedError


class PlaybackSession(PlaybackSubject):
    def __init__(self) -> None:
        self._observers: List[PlaybackObserver] = []
        self.state = "stopped"
        self.position_sec = 0

    def attach(self, observer: PlaybackObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: PlaybackObserver) -> None:
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for obs in self._observers:
            obs.update({"state": self.state, "position": self.position_sec})

    def play(self) -> None:
        self.state = "playing"
        self.notify_observers()

    def pause(self) -> None:
        self.state = "paused"
        self.notify_observers()


class ProgressBarUI(PlaybackObserver):
    def __init__(self) -> None:
        self.last_position = 0

    def update(self, state: dict) -> None:
        self.last_position = state["position"]


class WatchHistoryLogger(PlaybackObserver):
    def __init__(self) -> None:
        self.log: List[dict] = []

    def update(self, state: dict) -> None:
        self.log.append(state)


class RecommendationEngine(PlaybackObserver):
    def __init__(self) -> None:
        self.last_state = None

    def update(self, state: dict) -> None:
        self.last_state = state["state"]
