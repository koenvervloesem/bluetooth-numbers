from uuid import UUID

import pytest

from bluetooth_numbers.characteristics import characteristic


@pytest.mark.parametrize(
    "uuid, name",
    [
        (0x2A7E, "Aerobic Heart Rate Lower Limit"),
        (0x2A37, "Heart Rate Measurement"),
        (0x2ADE, "Mesh Proxy Data Out"),
    ],
)
def test_uuid16(uuid: int, name: str) -> None:
    assert characteristic[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        (-1),
        (65535),
    ],
)
def test_invalid_uuid16(uuid: int) -> None:
    with pytest.raises(KeyError):
        characteristic[uuid]


@pytest.mark.parametrize(
    "uuid, name",
    [
        (UUID("00001524-1212-EFDE-1523-785FEABCD123"), "Blinky Button State"),
        (UUID("ef680301-9B35-4933-9b10-52ffa9740042"), "Thingy LED State"),
        (UUID("E95D1B25-251D-470A-A062-FA1922DFA9A8"), "micro:bit Temperature Period"),
    ],
)
def test_uuid128(uuid: UUID, name: str) -> None:
    assert characteristic[uuid] == name


@pytest.mark.parametrize(
    "uuid, name",
    [
        (UUID("00002A7E-0000-1000-8000-00805F9B34FB"), "Aerobic Heart Rate Lower Limit"),
        (UUID("00002a37-0000-1000-8000-00805f9B34fb"), "Heart Rate Measurement"),
        (UUID("00002ADE-0000-1000-8000-00805F9B34FB"), "Mesh Proxy Data Out"),
    ],
)
def test_uuid16_as_uuid128(uuid: UUID, name: str) -> None:
    assert characteristic[uuid] == name


@pytest.mark.parametrize(
    "uuid",
    [
        (UUID("2ac35699-9af0-4228-80fb-8ca56c77ac73")),
        (UUID("9652BA73-AA7C-4B56-BB93-CCC6D44937C8")),
    ],
)
def test_invalid_uuid128(uuid: UUID) -> None:
    with pytest.raises(KeyError):
        characteristic[uuid]
