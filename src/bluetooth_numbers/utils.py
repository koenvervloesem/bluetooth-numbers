from typing import Dict, Union
from uuid import UUID

BASE_UUID = UUID("00000000-0000-1000-8000-00805F9B34FB")


def uuid128_to_uuid16(uuid128: UUID) -> int:
    """Convert a 128-bit standard Bluetooth UUID to a 16-bit UUID.

    Args:
        uuid128: A 128-bit standard Bluetooth UUID.

    Raises:
        ValueError: If uuid128 is not a 128-bit standard Bluetooth UUID.

    Returns:
        A 16-bit UUID that is the short UUID of the 128-bit standard Bluetooth UUID.

    >>> uuid128_to_uuid16(UUID('00001800-0000-1000-8000-00805f9b34fb'))
    0x1800
    """
    # Extract 16-bit UUID
    uuid16 = int.from_bytes(uuid128.bytes[2:4], "big")

    # Test whether 128-bit UUID is a standard Bluetooth UUID
    uuid128_bytearray = bytearray(uuid128.bytes)
    uuid128_bytearray[2:4] = b"\x00\x00"
    uuid128 = UUID(bytes=bytes(uuid128_bytearray))
    if uuid128 != BASE_UUID:
        raise ValueError("Not a 128-bit standaard Bluetooth UUID")

    return uuid16


def uuid16_to_uuid128(uuid16: int) -> UUID:
    """Convert a 16-bit UUID to a 128-bit UUID with the Bluetooth base UUID.

    Args:
        uuid16: A 16-bit UUID.

    Raises:
        ValueError: If uuid16 is not an integer from 0 to 65535.

    Returns:
        A 128-bit UUID that is the full UUID of the 16-bit UUID.

    >>> uuid16_to_uuid128(0x1800)
    UUID('00001800-0000-1000-8000-00805f9b34fb')
    """
    if uuid16 < 0 or uuid16 > 0xFFFF or not isinstance(uuid16, int):
        raise ValueError("Not a 16-bit integer")

    uuid128 = bytearray(BASE_UUID.bytes)
    # Insert the 16-bit UUID in the third and fourth bytes of the 128-bit UUID:
    #  00000000-0000-1000-8000-00805f9b34fb
    #      \  /
    #      1800
    uuid128[2:4] = uuid16.to_bytes(2, "big")
    return UUID(bytes=bytes(uuid128))


def uint16_to_hex(number: int) -> str:
    """Convert a 16-bit UUID or Company ID to a string representing the hexadecimal number.

    Args:
        number: A 16-bit number.

    Raises:
        ValueError: If number is not an integer from 0 to 65535.

    Returns:
        A string representing the hexadecimal number.

    >>> uint16_to_hex(0xFD6F)
    '0xfd6f'
    """
    if number < 0 or number > 0xFFFF:
        raise ValueError("Not a 16-bit integer")

    return f"{number:#0{6}x}"


class UUIDDict(Dict[Union[UUID, int], str]):
    """Dictionary class that converts 128-bit standard UUID keys to 16-bit when the key is missing.

    This is used for 128-bit UUIDs.
    """

    def __missing__(self, key: Union[UUID, int]) -> str:
        """Try the key converted to 16-bit UUID"""
        if isinstance(key, UUID):
            try:
                uuid16_key = uuid128_to_uuid16(key)
                return self[uuid16_key]
            except ValueError:
                raise KeyError(key)
        else:
            raise KeyError(key)
