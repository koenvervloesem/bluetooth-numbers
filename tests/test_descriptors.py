import pytest

from bluetooth_numbers.descriptors import descriptor


@pytest.mark.parametrize(
    "uuid, name",
    [
        (0x2900, "Characteristic Extended Properties"),
        (0x2906, "Valid Range"),
        (0x290E, "Time Trigger Setting"),
    ],
)
def test_uuid16(uuid: int, name: str) -> None:
    assert descriptor[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        (-1),
        (65535),
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    with pytest.raises(KeyError):
        descriptor[uuid]
