"""Test the bluetooth_numbers._characteristics module."""
from uuid import UUID

import pytest

from bluetooth_numbers import characteristic
from bluetooth_numbers.exceptions import No16BitIntegerError, UnknownUUIDError


@pytest.mark.parametrize(
    "uuid, name",
    [
        (0x2A7E, "Aerobic Heart Rate Lower Limit"),
        (0x2A37, "Heart Rate Measurement"),
        (0x2ADE, "Mesh Proxy Data Out"),
    ],
)
def test_uuid16(uuid: int, name: str) -> None:
    """Test the characteristic dict with known values."""
    assert characteristic[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        -1,
        65536,
        6.5,
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    """Test the characteristic dict with invalid keys.

    Using a key that's not a 16-bit unsigned integer should raise a
    No16BitIntegerError exception.
    """
    with pytest.raises(No16BitIntegerError):
        _ = characteristic[uuid]


@pytest.mark.parametrize(
    "uuid",
    [
        0x0000,
        0x2ACA,
        0xFFFF,
    ],
)
def test_unknown_uuid16(uuid: int) -> None:
    """Test the characteristic dict with unknown 16-bit UUIDs.

    Using an unknown 16-bit UUID as a key should raise an UnknownUUIDError
    exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = characteristic[uuid]


@pytest.mark.parametrize(
    "uuid, name",
    [
        (UUID("00001524-1212-EFDE-1523-785FEABCD123"), "Blinky Button State"),
        (UUID("ef680301-9B35-4933-9b10-52ffa9740042"), "Thingy LED State"),
        (UUID("E95D1B25-251D-470A-A062-FA1922DFA9A8"), "micro:bit Temperature Period"),
    ],
)
def test_uuid128(uuid: UUID, name: str) -> None:
    """Test the characteristic dict with 128-bit non-standard UUIDs."""
    assert characteristic[uuid] == name


@pytest.mark.parametrize(
    "uuid, name",
    [
        (
            UUID("00002A7E-0000-1000-8000-00805F9B34FB"),
            "Aerobic Heart Rate Lower Limit",
        ),
        (UUID("00002a37-0000-1000-8000-00805f9B34fb"), "Heart Rate Measurement"),
        (UUID("00002ADE-0000-1000-8000-00805F9B34FB"), "Mesh Proxy Data Out"),
    ],
)
def test_uuid16_as_uuid128(uuid: UUID, name: str) -> None:
    """Test the characteristic dict with 128-bit standard UUIDs."""
    assert characteristic[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        UUID("2ac35699-9af0-4228-80fb-8ca56c77ac73"),
        UUID("9652BA73-AA7C-4B56-BB93-CCC6D44937C8"),
    ],
)
def test_unknown_uuid128(uuid: UUID) -> None:
    """Test the characteristic dict with unknown 128-bit UUIDs.

    Using an unknown 128-bit UUID as a key should raise an UnknownUUIDError
    exception.
    """
    with pytest.raises(UnknownUUIDError):
        _ = characteristic[uuid]
