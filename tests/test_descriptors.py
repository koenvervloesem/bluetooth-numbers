"""Test the bluetooth_numbers.descriptors module."""
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
    """Test whether the descriptor dict returns the correct name for a few UUIDs."""
    assert descriptor[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        (-1),
        (65536),
        (6.5),
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    """Test whether getting the value of an invalid UUID from the descriptor dict
    raises the No16BitIntegerError exception.
    """
    with pytest.raises(No16BitIntegerError):
        _ = descriptor[uuid]


@pytest.mark.parametrize(
    "uuid",
    [
        (0x0000),
        (0x28FF),
        (0xFFFF),
    ],
)
def test_unknown_uuid16(uuid: int) -> None:
    """Test whether getting the value of an unknown UUID from the descriptor dict
    raises the UnknownUUIDError exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = descriptor[uuid]
