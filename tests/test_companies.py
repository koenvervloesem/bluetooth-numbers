# pylint: disable=line-too-long
"""Test the bluetooth_numbers._companies module."""
import pytest

from bluetooth_numbers import company
from bluetooth_numbers.exceptions import No16BitIntegerError, UnknownCICError


@pytest.mark.parametrize(
    "code, name",
    [
        (0x0000, "Ericsson Technology Licensing"),
        (0x004C, "Apple, Inc."),
        (0x0499, "Ruuvi Innovations Ltd."),
        (
            0xFFFF,
            "Bluetooth SIG Specification Reserved Default Vendor ID for Remote Devices Without Device ID Service Record.",
        ),
    ],
)
def test_company(code: int, name: str) -> None:
    """Test the company dict with known values."""
    assert company[code] == name


@pytest.mark.parametrize(
    "code",
    [
        -1,
        65536,
        6.5,
        "test",
    ],
)
def test_invalid_company(code: int) -> None:
    """Test the company dict with invalid keys.

    Using a key that's not a 16-bit unsigned integer should raise a
    No16BitIntegerError exception.
    """
    with pytest.raises(No16BitIntegerError):
        _ = company[code]


@pytest.mark.parametrize(
    "code",
    [
        0xEEEE,
        65534,
    ],
)
def test_unknown_company(code: int) -> None:
    """Test the company dict with unknown keys.

    Using an unknown company code as a key should raise an UnknownCICError exception.
    """
    with pytest.raises(UnknownCICError):
        _ = company[code]
