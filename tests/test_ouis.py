import pytest

from bluetooth_numbers.ouis import oui


@pytest.mark.parametrize(
    "prefix, name",
    [
        ("58:2D:34", "Qingping Electronics (Suzhou) Co., Ltd"),
        ("C4:7C:8D", "IEEE Registration Authority"),
    ],
)
def test_oui(prefix: str, name: str) -> None:
    assert oui[prefix] == name


@pytest.mark.parametrize(
    "prefix",
    [
        ("FOOBAR"),
        ("AB:CD:EF"),
    ],
)
def test_invalid_company(prefix: str) -> None:
    with pytest.raises(KeyError):
        oui[prefix]
