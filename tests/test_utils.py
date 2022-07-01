from uuid import UUID

import pytest

from bluetooth_numbers.utils import uint16_to_hex, uuid16_to_uuid128, uuid128_to_uuid16


@pytest.mark.parametrize(
    "number, hex_string",
    [
        (0x004C, "0x004c"),
        (0x0499, "0x0499"),
        (0xFD6F, "0xfd6f"),
    ],
)
def test_uint16_to_hex(number: int, hex_string: str) -> None:
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
    with pytest.raises(ValueError):
        uint16_to_hex(number)


@pytest.mark.parametrize(
    "uuid16, uuid128",
    [
        (0x1800, UUID("00001800-0000-1000-8000-00805F9B34FB")),
        (0xFD6F, UUID("0000FD6F-0000-1000-8000-00805F9B34FB")),
    ],
)
def test_uuid16_to_uuid128(uuid16: int, uuid128: UUID) -> None:
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
    with pytest.raises(ValueError):
        uuid16_to_uuid128(uuid16)


@pytest.mark.parametrize(
    "uuid128, uuid16",
    [
        (UUID("00001800-0000-1000-8000-00805F9B34FB"), 0x1800),
        (UUID("0000FD6F-0000-1000-8000-00805F9B34FB"), 0xFD6F),
    ],
)
def test_uuid128_to_uuid16(uuid128: UUID, uuid16: int) -> None:
    assert uuid128_to_uuid16(uuid128) == uuid16


@pytest.mark.parametrize(
    "uuid128",
    [
        (UUID("bfc46884-ea75-416b-8154-29c5d0b0a087")),
        (UUID("00001800-0000-1000-8000-00805F9B34FC")),
    ],
)
def test_invalid_uuid128_to_uuid16(uuid128: UUID) -> None:
    with pytest.raises(ValueError):
        uuid128_to_uuid16(uuid128)
