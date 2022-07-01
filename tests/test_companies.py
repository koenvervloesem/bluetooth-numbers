import pytest

from bluetooth_numbers.companies import company


@pytest.mark.parametrize(
    "code, name",
    [
        (0x0000, "Ericsson Technology Licensing"),
        (0x004C, "Apple, Inc."),
        (0x0499, "Ruuvi Innovations Ltd."),
        (
            0xFFFF,
            "Bluetooth SIG Specification Reserved Default Vendor ID for Remote Devices Without Device ID Service Record.",  # noqa: E501
        ),
    ],
)
def test_company(code: int, name: str) -> None:
    assert company[code] == name


@pytest.mark.parametrize(
    "code",
    [
        (-1),
        (65534),
    ],
)
def test_invalid_company(code: int) -> None:
    with pytest.raises(KeyError):
        company[code]
