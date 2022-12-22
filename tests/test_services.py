"""Test the bluetooth_numbers.services module."""
from uuid import UUID

import pytest

from bluetooth_numbers import service
from bluetooth_numbers.exceptions import No16BitIntegerError, UnknownUUIDError


@pytest.mark.parametrize(
    "uuid, name",
    [
        (0x1800, "Generic Access"),
        (0x1812, "Human Interface Device"),
        (0xFD6F, "Exposure Notification Service"),
    ],
)
def test_uuid16(uuid: int, name: str) -> None:
    """Test whether the service dict returns the correct name for a few 16-bit
    UUIDs.
    """
    assert service[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        (-1),
        (65536),
        (6.5),
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    """Test whether getting the value of an invalid 16-bit UUID from the
    service dict raises the No16BitIntegerError exception.
    """
    with pytest.raises(No16BitIntegerError):
        _ = service[uuid]


@pytest.mark.parametrize(
    "uuid",
    [
        (0x0000),
        (0x1799),
        (0xFFFF),
    ],
)
def test_unknown_uuid16(uuid: int) -> None:
    """Test whether getting the value of an unknown 16-bit UUID from the
    service dict raises the UnknownUUIDError exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = service[uuid]


@pytest.mark.parametrize(
    "uuid, name",
    [
        (
            UUID("7905F431-B5CE-4E99-A40F-4B1E122D00D0"),
            "Apple Notification Center Service",
        ),
        (UUID("6e400001-b5a3-f393-e0a9-e50e24dcca9e"), "Nordic UART Service"),
        (UUID("8D53DC1D-1DB7-4CD3-868B-8A527460AA84"), "SMP Service"),
    ],
)
def test_uuid128(uuid: UUID, name: str) -> None:
    """Test whether the service dict returns the correct name for a few 128-bit
    non-standard UUIDs.
    """
    assert service[uuid] == name


@pytest.mark.parametrize(
    "uuid, name",
    [
        (UUID("00001800-0000-1000-8000-00805F9B34FB"), "Generic Access"),
        (UUID("00001812-0000-1000-8000-00805F9B34FB"), "Human Interface Device"),
        (UUID("0000FD6F-0000-1000-8000-00805F9B34FB"), "Exposure Notification Service"),
    ],
)
def test_uuid16_as_uuid128(uuid: UUID, name: str) -> None:
    """Test whether the service dict returns the correct name for a few 128-bit
    standard UUIDs.
    """
    assert service[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        (UUID("e85e7f31-69a0-4784-ae25-fd3f452bf563")),
        (UUID("85AB7C38-2C67-4A4F-8379-E6BC606D15EA")),
    ],
)
def test_unknown_uuid128(uuid: UUID) -> None:
    """Test whether getting the value of an unknown 128-bit UUID from the service dict
    results in an UnknownUUIDError.
    """
    with pytest.raises(UnknownUUIDError):
        _ = service[uuid]
