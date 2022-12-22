"""Test the bluetooth_numbers.utils module."""
from uuid import UUID

import pytest

from bluetooth_numbers.exceptions import (
    No16BitIntegerError,
    NonStandardUUIDError,
    WrongOUIFormatError,
)
from bluetooth_numbers.utils import (
    is_normalized_oui,
    is_uint16,
    normalize_oui,
    uint16_to_hex,
    uuid16_to_uuid128,
    uuid128_to_uuid16,
)


@pytest.mark.parametrize(
    "oui, result",
    [
        ("70:BC:10", True),
        ("44:ec:ce", False),
        ("00-80-C7", False),
        ("6C2B59", False),
        ("a41194", False),
        ("FOOBAR", False),
    ],
)
def test_is_normalized_oui(oui: str, result: bool) -> None:
    """Test whether the is_normalized_oui function correctly checks whether a string
    is a normalized OUI.
    """
    assert is_normalized_oui(oui) == result


@pytest.mark.parametrize(
    "oui, normalized",
    [
        ("00:1B:C0", "00:1B:C0"),
        ("c0:d0:ff", "C0:D0:FF"),
        ("80-7D-3A", "80:7D:3A"),
        ("10-94-bb", "10:94:BB"),
        ("7C6456", "7C:64:56"),
        ("ac6706", "AC:67:06"),
    ],
)
def test_normalize_oui(oui: str, normalized: str) -> None:
    """Test whether the normalize_oui function correctly normalizes an OUI."""
    assert normalize_oui(oui) == normalized


@pytest.mark.parametrize(
    "oui",
    [
        ("AB:CD:EF:GH:IJ:KL"),
        ("gg-hh-ii"),
        ("FOOBAR"),
    ],
)
def test_normalize_oui_exceptions(oui: str) -> None:
    """Test whether the normalize_oui function raises a WrongOUIFormatError exception
    when the argument doesn't have the right format."""
    with pytest.raises(WrongOUIFormatError):
        normalize_oui(oui)


@pytest.mark.parametrize(
    "number, result",
    [
        (0x0000, True),
        (0x1800, True),
        (0x0499, True),
        (0xFD6F, True),
        (-1, False),
        (65536, False),
        (6.5, False),
        ("true", False),
    ],
)
def test_is_uint16(number: int, result: bool) -> None:
    """Test whether the is_uint16 function correctly checks whether a number is a
    16-bit unsigned integer.
    """
    assert is_uint16(number) == result


@pytest.mark.parametrize(
    "number, hex_string",
    [
        (0x004C, "0x004c"),
        (0x0499, "0x0499"),
        (0xFD6F, "0xfd6f"),
    ],
)
def test_uint16_to_hex(number: int, hex_string: str) -> None:
    """Test whether the uint16_to_hex function converts a 16-bit unsigned integer
    to the correct string representation.
    """
    assert uint16_to_hex(number) == hex_string


@pytest.mark.parametrize(
    "number",
    [
        (-1),
        (65536),
        (4.5),
    ],
)
def test_invalid_uint16_to_hex(number: int) -> None:
    """Test whether the uint16_to_hex function raises a No16BitIntegerError for an
    invalid argument.
    """
    with pytest.raises(No16BitIntegerError):
        uint16_to_hex(number)


@pytest.mark.parametrize(
    "uuid16, uuid128",
    [
        (0x1800, UUID("00001800-0000-1000-8000-00805F9B34FB")),
        (0xFD6F, UUID("0000FD6F-0000-1000-8000-00805F9B34FB")),
    ],
)
def test_uuid16_to_uuid128(uuid16: int, uuid128: UUID) -> None:
    """Test whether the uuid16_to_uuid128 function correctly converts a 16-bit UUID
    to a 128-bit UUID with the Bluetooth base UUID.
    """
    assert uuid16_to_uuid128(uuid16) == uuid128


@pytest.mark.parametrize(
    "uuid16",
    [
        (-1),
        (65536),
        (4.5),
    ],
)
def test_invalid_uuid16_to_uuid128(uuid16: int) -> None:
    """Test whether the uuid16_to_uuid128 function raises a No16BitIntegerError for an
    invalid argument.
    """
    with pytest.raises(No16BitIntegerError):
        uuid16_to_uuid128(uuid16)


@pytest.mark.parametrize(
    "uuid128, uuid16",
    [
        (UUID("00001800-0000-1000-8000-00805F9B34FB"), 0x1800),
        (UUID("0000FD6F-0000-1000-8000-00805F9B34FB"), 0xFD6F),
    ],
)
def test_uuid128_to_uuid16(uuid128: UUID, uuid16: int) -> None:
    """Test whether the uuid128_to_uuid16 function correctly converts a 128-bit
    standard Bluetooth UUID to a 16-bit UUID.
    """
    assert uuid128_to_uuid16(uuid128) == uuid16


@pytest.mark.parametrize(
    "uuid128",
    [
        (UUID("bfc46884-ea75-416b-8154-29c5d0b0a087")),
        (UUID("00001800-0000-1000-8000-00805F9B34FC")),
    ],
)
def test_invalid_uuid128_to_uuid16(uuid128: UUID) -> None:
    """Test whether the uuid128_to_uuid16 function raises a NonStandardUUIDError
    for an invalid argument.
    """
    with pytest.raises(NonStandardUUIDError):
        uuid128_to_uuid16(uuid128)
