"""Test the bluetooth_numbers.reverse_lookup module."""
import pytest

from bluetooth_numbers.reverse_lookup import ReverseLookup, Match


@pytest.fixture()
def reverse_lookup() -> ReverseLookup:
    """Return a ReverseLookup instance."""
    return ReverseLookup()


def test_valid_reverse_lookup(reverse_lookup: ReverseLookup) -> None:
    """Test terms that should return a Match."""
    assert Match(6168, "Cycling Power", "service") in reverse_lookup.lookup(
        "Power",
        logic="OR",
    )
    assert Match(6168, "Cycling Power", "service") in reverse_lookup.lookup(
        "Power Cycling",
        logic="AND",
    )
    assert Match(6168, "Cycling Power", "service") in reverse_lookup.lookup(
        "Power",
        logic="SUBSTR",
    )
    assert Match(6168, "Cycling Power", "service") in reverse_lookup.lookup(
        "Cycling",
        uuid_types=["service"],
        logic="OR",
    )


def test_bad_term_reverse_lookup(reverse_lookup: ReverseLookup) -> None:
    """Test terms that should return an empty set."""
    assert reverse_lookup.lookup("foobar") == set()
    assert reverse_lookup.lookup("foobar", logic="AND") == set()
    assert Match(6168, "Cycling Power", "service") not in reverse_lookup.lookup(
        "Power FooBar",
        logic="AND",
    )
    assert reverse_lookup.lookup("foobar", logic="SUBSTR") == set()


def test_wrong_uuid_type_reverse_lookup(reverse_lookup: ReverseLookup) -> None:
    """Return an empty set when the term is not found in the uuid_type."""
    assert Match(6168, "Cycling Power", "service") not in reverse_lookup.lookup(
        "Cycling",
        uuid_types=["descriptor"],
        logic="OR",
    )


def test_bad_valid_terms_reverse_lookup(reverse_lookup: ReverseLookup) -> None:
    """Test terms that should return an empty set."""
    assert Match(6168, "Cycling Power", "service") in reverse_lookup.lookup(
        "Power FooBar",
        logic="OR",
    )
    assert Match(6168, "Cycling Power", "service") not in reverse_lookup.lookup(
        "Power FooBar",
        logic="AND",
    )
    assert Match(6168, "Cycling Power", "service") not in reverse_lookup.lookup(
        "Power FooBar",
        logic="SUBSTR",
    )
