"""Test the bluetooth_numbers._ouis module."""
import pytest

from bluetooth_numbers import oui
from bluetooth_numbers.exceptions import UnknownOUIError, WrongOUIFormatError


@pytest.mark.parametrize(
    "prefix, name",
    [
        ("58:2D:34", "Qingping Electronics (Suzhou) Co., Ltd"),
        ("C4:7C:8D", "IEEE Registration Authority"),
        ("ac:67:06", "Ruckus Wireless"),
        ("B8-75-C0", "PayPal, Inc."),
        ("245BA7", "Apple, Inc."),
        ("a0-6f-aa", "LG Innotek"),
        ("407c7d", "Nokia"),
    ],
)
def test_oui(prefix: str, name: str) -> None:
    """Test the oui dict with known values."""
    assert oui[prefix] == name


@pytest.mark.parametrize(
    "prefix",
    [
        "FOOBAR",
        "AB-CD-EF-GH",
    ],
)
def test_invalid_oui(prefix: str) -> None:
    """Test the oui dict with invalid prefixes.

    Using an invalid prefix as a key should raise a WrongOUIFormatError exception.
    """
    with pytest.raises(WrongOUIFormatError):
        _ = oui[prefix]


@pytest.mark.parametrize(
    "prefix",
    [
        "12:34:56",
        "AB:CD:EF",
    ],
)
def test_unknown_oui(prefix: str) -> None:
    """Test the oui dict with unknown prefixes.

    Using an unknown prefix as a key should raise an UnknownOUIError exception.
    """
    with pytest.raises(UnknownOUIError):
        _ = oui[prefix]
