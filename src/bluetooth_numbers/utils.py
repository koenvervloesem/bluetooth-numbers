"""Module with utility classes and functions used by the other modules of this
package. They are also useful in programs using this library.
"""
import re
from uuid import UUID

from bluetooth_numbers.exceptions import (
    No16BitIntegerError,
    NonStandardUUIDError,
    WrongOUIFormatError,
)

BASE_UUID = UUID("00000000-0000-1000-8000-00805F9B34FB")
"""Base UUID defined by the Bluetooth SIG."""

_OUI_RE = re.compile(r"^([0-9A-F]{2})[-:]*([0-9A-F]{2})[-:]*([0-9A-F]{2})$")
_NORMALIZED_OUI_RE = re.compile(r"^[0-9A-F]{2}:[0-9A-F]{2}:[0-9A-F]{2}$")


def is_normalized_oui(oui: str) -> bool:
    """Check whether the argument is a normalized OUI: a string with format
    "XX:YY:ZZ" where XX, YY and ZZ are uppercase hexadecimal digits.

    Args:
        oui (str): The string to check

    Returns:
        True if the argument is a normalized OUI, False otherwise.

    Examples:

    >>> from bluetooth_numbers.utils import is_normalized_oui
    >>> is_normalized_oui("98-e7-43")
    False
    >>> is_normalized_oui("98:E7:43")
    True
    >>> is_normalized_oui("FOOBAR")
    False
    """
    return bool(_NORMALIZED_OUI_RE.match(oui))


def normalize_oui(oui: str) -> str:
    """Normalize an OUI to uppercase hexadecimal letters and with a colon between
    the OUI's bytes.

    Args:
        oui (str): The OUI to normalize

    Raises:
        WrongOUIFormatError: If the OUI doesn't have the right format.

    Returns:
        The normalized OUI

    Examples:

    >>> from bluetooth_numbers.utils import normalize_oui
    >>> normalize_oui("98-e7-43")
    '98:E7:43'
    >>> normalize_oui("98e743")
    '98:E7:43'
    >>> normalize_oui("FOOBAR")
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.WrongOUIFormatError: 'FOOBAR'
    """
    oui_parts = _OUI_RE.match(oui.upper())
    if oui_parts:
        return oui_parts.group(1) + ":" + oui_parts.group(2) + ":" + oui_parts.group(3)
    raise WrongOUIFormatError(oui)


def is_uint16(number: int) -> bool:
    """Check whether a number is a 16-bit unsigned integer.

    Args:
        number (int): The number to check.

    Returns:
        True if the argument is a 16-bit unsigned integer; False otherwise.

    Examples:

    >>> from bluetooth_numbers.utils import is_uint16
    >>> is_uint16(0x1800)
    True
    >>> is_uint16(-1)
    False
    """
    return isinstance(number, int) and 0 <= number <= 0xFFFF


def uuid128_to_uuid16(uuid128: UUID) -> int:
    """Convert a 128-bit standard Bluetooth UUID to a 16-bit UUID.

    Args:
        uuid128 (UUID): A 128-bit standard Bluetooth UUID.

    Raises:
        NonStandardUUIDError: If uuid128 is not a 128-bit standard Bluetooth UUID.

    Returns:
        A 16-bit UUID that is the short UUID of the 128-bit standard Bluetooth UUID.

    Example:

    >>> from bluetooth_numbers.utils import uuid128_to_uuid16, uint16_to_hex
    >>> uint16_to_hex(uuid128_to_uuid16(UUID('00001800-0000-1000-8000-00805f9b34fb')))
    '0x1800'
    """
    # Test whether the 128-bit UUID is a standard Bluetooth UUID
    uuid128_bytearray = bytearray(uuid128.bytes)
    uuid128_bytearray[2:4] = b"\x00\x00"
    uuid128_masked = UUID(bytes=bytes(uuid128_bytearray))
    if uuid128_masked != BASE_UUID:
        raise NonStandardUUIDError(uuid128_masked)

    # If it is, extract the 16-bit UUID
    uuid16 = int.from_bytes(uuid128.bytes[2:4], "big")
    return uuid16


def uuid16_to_uuid128(uuid16: int) -> UUID:
    """Convert a 16-bit UUID to a 128-bit UUID with the Bluetooth base UUID.

    Args:
        uuid16 (int): A 16-bit UUID.

    Raises:
        No16BitIntegerError: If uuid16 is not an integer from 0 to 65535.

    Returns:
        A 128-bit UUID that is the full UUID of the 16-bit UUID.

    Example:

    >>> from bluetooth_numbers.utils import uuid16_to_uuid128
    >>> uuid16_to_uuid128(0x1800)
    UUID('00001800-0000-1000-8000-00805f9b34fb')
    """
    if not is_uint16(uuid16):
        raise No16BitIntegerError(uuid16)

    uuid128 = bytearray(BASE_UUID.bytes)
    # Insert the 16-bit UUID in the third and fourth bytes of the 128-bit UUID.
    # For example:
    #  00000000-0000-1000-8000-00805f9b34fb
    #      \  /
    #      1800
    uuid128[2:4] = uuid16.to_bytes(2, "big")
    return UUID(bytes=bytes(uuid128))


def uint16_to_hex(number: int) -> str:
    """Convert a 16-bit UUID or Company ID to a string representing the hexadecimal
    number.

    Args:
        number (int): A 16-bit number.

    Raises:
        No16BitIntegerError: If number is not an integer from 0 to 65535.

    Returns:
        A string representing the hexadecimal number.

    Example:

    >>> from bluetooth_numbers.utils import uint16_to_hex
    >>> uint16_to_hex(0xFD6F)
    '0xfd6f'
    """
    if not is_uint16(number):
        raise No16BitIntegerError(number)

    return f"{number:#0{6}x}"
