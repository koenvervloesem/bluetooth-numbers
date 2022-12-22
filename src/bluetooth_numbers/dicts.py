"""Module with specialized dictionary classes for UUIDs, CICs and OUIs used in
Bluetooth applications.
"""
from typing import Dict, Union
from uuid import UUID

from bluetooth_numbers.exceptions import (
    No16BitIntegerError,
    NonStandardUUIDError,
    UnknownCICError,
    UnknownOUIError,
    UnknownUUIDError,
)
from bluetooth_numbers.utils import (
    is_normalized_oui,
    is_uint16,
    normalize_oui,
    uuid128_to_uuid16,
)


class CICDict(Dict[int, str]):
    """Dictionary class to hold 16-bit company codes and their names.

    You can use this class as a dict with the following differences:

    - If you check for a key that doesn't exist, this raises an UnknownCICError.
    - If you check for a key that isn't a 16-bit unsigned integer, this raises a
      No16BitIntegerError.

    Example:

    >>> from bluetooth_numbers import company
    >>> company[0x004C]
    'Apple, Inc.'
    >>> company[-1]
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.No16BitIntegerError: -1
    >>> company[65534]
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.UnknownCICError: 65534
    """

    def __missing__(self, key: int) -> str:
        """Try the key and raise exception when it's invalid"""
        if is_uint16(key):
            raise UnknownCICError(key)

        raise No16BitIntegerError(key)


class OUIDict(Dict[str, str]):
    """Dictionary class to hold OUIs and their names.

    You can use this class as a dict with the following differences:

    - You can check for an OUI in the formats "xx:yy:zz", "xx-yy-zz" or "xxyyzz".
      Both lowercase and uppercase letters are supported.
    - If you check for a key that doesn't exist, this raises an UnknownOUIError.
    - If you check for a key that doesn't have one of the supported formats, this
      raises WrongOUIFormatError.

    Example:

    >>> from bluetooth_numbers import oui
    >>> oui["98:E7:43"]
    'Dell Inc.'
    >>> oui["c4-29-96"]
    'Signify B.V.'
    >>> oui["A44519"]
    'Xiaomi Communications Co Ltd'
    >>> oui["FOOBAR"]
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.WrongOUIFormatError: 'FOOBAR'
    >>> oui["AB:CD:EF"]
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.UnknownOUIError: AB:CD:EF
    """

    def __missing__(self, key: str) -> str:
        """Try the key and raise exception when it's invalid"""
        if is_normalized_oui(key):
            raise UnknownOUIError(key)

        return self[normalize_oui(key)]


class UUIDDict(Dict[Union[UUID, int], str]):
    """Dictionary class that converts 128-bit standard UUID keys to 16-bit when the key
    is missing.

    You can use this class as a dict for Bluetooth UUIDs, with the following
    differences:

    - If you check for a 128-bit standard UUID and this UUID doesn't exist in the
      dictionary, it will check for the corresponding 16-bit UUID.
    - If you check for a UUID that doesn't exist, this raises an UnknownUUIDError.
    - If you check for a key that isn't a 16-bit unsigned integer, this raises a
      No16BitIntegerError.

    Example:

    >>> from bluetooth_numbers import service
    >>> from uuid import UUID
    >>> service[UUID("0000180F-0000-1000-8000-00805F9B34FB")]
    'Battery Service'
    >>> service[0x180F]
    'Battery Service'
    >>> service[0]
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.UnknownUUIDError: 0
    >>> service[6.5]
    Traceback (most recent call last):
    bluetooth_numbers.exceptions.No16BitIntegerError: 6.5
    """

    def __missing__(self, key: Union[UUID, int]) -> str:
        """Try the key converted to 16-bit UUID"""
        if isinstance(key, UUID):
            try:
                uuid16_key = uuid128_to_uuid16(key)
                return self[uuid16_key]
            except NonStandardUUIDError as error:
                raise UnknownUUIDError(key) from error
        elif is_uint16(key):
            raise UnknownUUIDError(key)
        else:
            raise No16BitIntegerError(key)
