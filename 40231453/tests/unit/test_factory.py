import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import pytest

from src.patterns.factory import get_factory, MobileClient, SmartTVClient, LaptopClient


def test_mobile_factory_creates_mobile_client():
    factory = get_factory("mobile")
    client = factory.create_client()
    assert isinstance(client, MobileClient)


def test_smart_tv_factory_creates_smart_tv_client():
    factory = get_factory("smart_tv")
    client = factory.create_client()
    assert isinstance(client, SmartTVClient)


def test_laptop_factory_creates_laptop_client():
    factory = get_factory("laptop")
    client = factory.create_client()
    assert isinstance(client, LaptopClient)


def test_unknown_device_type_raises_error():
    with pytest.raises(ValueError):
        get_factory("smart_fridge")
