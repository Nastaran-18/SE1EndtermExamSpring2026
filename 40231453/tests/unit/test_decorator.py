import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from src.patterns.decorator import (
    BasicVideoStream,
    SubtitleDecorator,
    HDQualityDecorator,
    MultiAudioDecorator,
)


def test_basic_stream_plays_title():
    stream = BasicVideoStream("Inception")
    assert stream.play() == "Playing Inception"


def test_subtitle_decorator_adds_subtitles():
    stream = SubtitleDecorator(BasicVideoStream("Inception"))
    assert stream.play() == "Playing Inception + subtitles"


def test_decorators_can_be_stacked():
    stream = MultiAudioDecorator(
        HDQualityDecorator(SubtitleDecorator(BasicVideoStream("Inception")))
    )
    result = stream.play()
    assert "Playing Inception" in result
    assert "subtitles" in result
    assert "HD quality" in result
    assert "multi-audio" in result
