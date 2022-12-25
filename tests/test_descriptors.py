"""Test the bluetooth_numbers._descriptors module."""
import pytest

from bluetooth_numbers import descriptor
from bluetooth_numbers.exceptions import No16BitIntegerError, UnknownUUIDError


@pytest.mark.parametrize(
    "uuid, name",
    [
        (0x2900, "Characteristic Extended Properties"),
        (0x2906, "Valid Range"),
        (0x290E, "Time Trigger Setting"),
    ],
)
def test_uuid16(uuid: int, name: str) -> None:
    """Test the descriptor dict with known values."""
    assert descriptor[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        -1,
        65536,
        6.5,
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    """Test the descriptor dict with invalid keys.

    Using a key that's not a 16-bit unsigned integer should raise a
    No16BitIntegerError exception.
    """
    with pytest.raises(No16BitIntegerError):
        _ = descriptor[uuid]


@pytest.mark.parametrize(
    "uuid",
    [
        0x0000,
        0x28FF,
        0xFFFF,
    ],
)
def test_unknown_uuid16(uuid: int) -> None:
    """Test the descriptor dict with unknown 16-bit UUIDs.

    Using an unknown 16-bit UUID as a key should raise an UnknownUUIDError
    exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = descriptor[uuid]
