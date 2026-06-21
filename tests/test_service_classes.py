"""Test the bluetooth_numbers._service_classes module."""
from uuid import UUID

import pytest

from bluetooth_numbers import service_class
from bluetooth_numbers.exceptions import No16BitIntegerError, UnknownUUIDError


@pytest.mark.parametrize(
    ("uuid", "name"),
    [
        (0x1101, "SerialPort"),
        (0x1105, "OBEXObjectPush"),
        (0x1200, "PnPInformation"),
    ],
)
def test_uuid16(uuid: int, name: str) -> None:
    """Test the service_class dict with known 16-bit UUIDs."""
    assert service_class[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        -1,
        65536,
        6.5,
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    """Test the service_class dict with invalid keys.

    Using a key that's not a 16-bit unsigned integer should raise a
    No16BitIntegerError exception.
    """
    with pytest.raises(No16BitIntegerError):
        _ = service_class[uuid]


@pytest.mark.parametrize(
    "uuid",
    [
        0x0000,
        0x1099,
        0xFFFF,
    ],
)
def test_unknown_uuid16(uuid: int) -> None:
    """Test the service_class dict with unknown 16-bit UUIDs.

    Using an unknown 16-bit UUID as a key should raise an UnknownUUIDError
    exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = service_class[uuid]


@pytest.mark.parametrize(
    ("uuid", "name"),
    [
        (UUID("00001101-0000-1000-8000-00805F9B34FB"), "SerialPort"),
        (UUID("0000110A-0000-1000-8000-00805F9B34FB"), "Audio Source"),
    ],
)
def test_uuid16_as_uuid128(uuid: UUID, name: str) -> None:
    """Test the service_class dict with 128-bit standard UUIDs."""
    assert service_class[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        UUID("e85e7f31-69a0-4784-ae25-fd3f452bf563"),
        UUID("85AB7C38-2C67-4A4F-8379-E6BC606D15EA"),
    ],
)
def test_unknown_uuid128(uuid: UUID) -> None:
    """Test the service_class dict with unknown 128-bit UUIDs.

    Using an unknown 128-bit UUID as a key should raise an UnknownUUIDError
    exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = service_class[uuid]
