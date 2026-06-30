"""Factory pattern: creates the right DeviceClient based on the device type."""

from abc import ABC, abstractmethod


class DeviceClient(ABC):
    @abstractmethod
    def play(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def pause(self) -> str:
        raise NotImplementedError


class MobileClient(DeviceClient):
    def play(self) -> str:
        return "playing on mobile"

    def pause(self) -> str:
        return "paused on mobile"


class SmartTVClient(DeviceClient):
    def play(self) -> str:
        return "playing on smart tv"

    def pause(self) -> str:
        return "paused on smart tv"


class LaptopClient(DeviceClient):
    def play(self) -> str:
        return "playing on laptop"

    def pause(self) -> str:
        return "paused on laptop"


class DeviceClientFactory(ABC):
    @abstractmethod
    def create_client(self) -> DeviceClient:
        raise NotImplementedError


class MobileClientFactory(DeviceClientFactory):
    def create_client(self) -> DeviceClient:
        return MobileClient()


class SmartTVClientFactory(DeviceClientFactory):
    def create_client(self) -> DeviceClient:
        return SmartTVClient()


class LaptopClientFactory(DeviceClientFactory):
    def create_client(self) -> DeviceClient:
        return LaptopClient()


def get_factory(device_type: str) -> DeviceClientFactory:
    factories = {
        "mobile": MobileClientFactory,
        "smart_tv": SmartTVClientFactory,
        "laptop": LaptopClientFactory,
    }
    factory_cls = factories.get(device_type)
    if factory_cls is None:
        raise ValueError(f"Unknown device type: {device_type}")
    return factory_cls()
