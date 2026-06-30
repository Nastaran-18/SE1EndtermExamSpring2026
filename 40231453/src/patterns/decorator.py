"""Decorator pattern: wraps a VideoStream with extra features."""

from abc import ABC, abstractmethod


class VideoStream(ABC):
    @abstractmethod
    def play(self) -> str:
        raise NotImplementedError


class BasicVideoStream(VideoStream):
    def __init__(self, title: str) -> None:
        self.title = title

    def play(self) -> str:
        return f"Playing {self.title}"


class StreamDecorator(VideoStream, ABC):
    def __init__(self, wrappee: VideoStream) -> None:
        self._wrappee = wrappee

    def play(self) -> str:
        return self._wrappee.play()


class SubtitleDecorator(StreamDecorator):
    def play(self) -> str:
        return f"{self._wrappee.play()} + subtitles"


class HDQualityDecorator(StreamDecorator):
    def play(self) -> str:
        return f"{self._wrappee.play()} + HD quality"


class MultiAudioDecorator(StreamDecorator):
    def play(self) -> str:
        return f"{self._wrappee.play()} + multi-audio"
