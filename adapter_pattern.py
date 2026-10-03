from abc import ABC, abstractmethod


class Target(ABC):
    """Interface expected by the client."""

    @abstractmethod
    def request(self) -> str:
        raise NotImplementedError


class Adaptee:
    """Existing class with an incompatible interface."""

    def specific_request(self) -> str:
        return "Legacy service response"


class Adapter(Target):
    """Converts the Adaptee interface into the Target interface."""

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapted: {self.adaptee.specific_request()}"


def client_code(target: Target) -> None:
    print(target.request())


if __name__ == "__main__":
    legacy_service = Adaptee()
    adapter = Adapter(legacy_service)
    client_code(adapter)
