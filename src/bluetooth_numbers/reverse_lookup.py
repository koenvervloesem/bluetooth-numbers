"""Reverse lookup class to find UUIDs by their description."""
from __future__ import annotations

from typing import Literal, NamedTuple, Sequence, TYPE_CHECKING

if TYPE_CHECKING:
    from uuid import UUID

from bluetooth_numbers import characteristic, company, descriptor, oui, service

LOGIC = Literal["OR", "AND", "SUBSTR"]
UUID_TYPE_DEFAULT: Sequence[str] = (
    "characteristic",
    "company",
    "descriptor",
    "oui",
    "service",
)


class Match(NamedTuple):
    """Named tuple to hold a UUID and its description."""

    uuid: str | UUID | int
    description: str
    uuid_type: str


class ReverseLookup:
    """Reverse lookup class to find UUIDs by their description.

    Examples:
            >>> from bluetooth_numbers.reverse_lookup import ReverseLookup, Match
            >>> rl = ReverseLookup()
            >>> matches = rl.lookup("Cycling Power")
            >>> Match('00:05:5A', 'Power Dsine Ltd.', 'oui') in matches
            True
            >>> rl.lookup("Cycling Power", logic="AND")
            {Match(uuid=6168, description='Cycling Power', uuid_type='service'),
             Match(uuid=10851, description='Cycling Power Measurement',
             uuid_type='characteristic'),
             Match(uuid=10852, description='Cycling Power Vector',
             uuid_type='characteristic'),
             Match(uuid=10853, description='Cycling Power Feature',
             uuid_type='characteristic'),
             Match(uuid=10854, description='Cycling Power Control Point',
             uuid_type='characteristic')}
            >>> rl.lookup("Power Feature", uuid_types=['characteristic'],
            logic="SUBSTR")
            {Match(uuid=10853, description='Cycling Power Feature',
            uuid_type='characteristic')}
    """

    def __init__(self) -> None:
        """Initialize the ReverseLookup class, build index."""
        self.index = self._build_index()

    def _build_index(self) -> dict[str, set[Match]]:
        """Build dictionary (index) of terms to UUIDs.

        Returns:
            dict: dict[str, set[Match]] .
        """
        reverse_lookup: dict[str, set[Match]] = {}
        uuid_dicts = (
            (characteristic, "characteristic"),
            (company, "company"),
            (descriptor, "descriptor"),
            (oui, "oui"),
            (service, "service"),
        )
        for uuid_dict, uuid_type in uuid_dicts:
            for uuid, description in uuid_dict.items():  # type: ignore[attr-defined]
                for term in description.lower().split(" "):
                    if term not in reverse_lookup:
                        reverse_lookup[term] = set()
                    reverse_lookup[term].add(Match(uuid, description, uuid_type))
        return reverse_lookup

    def lookup(
        self,
        terms: str,
        uuid_types: Sequence[str] = UUID_TYPE_DEFAULT,
        logic: LOGIC = "OR",
    ) -> set[Match]:
        """Return the UUIDs for a given term(s).

        Args:
            terms: String with the term(s) to search for.
            uuid_types: Sequence of UUID types to search in.
            logic: Search logic to use. Can be "OR", "AND" or "SUBSTR".

        Returns:
            set: set[Match]: Set of Match named tuples.
        """
        terms_set: set[str] = set(terms.lower().split(" "))
        results: set[Match] = set()
        if logic == "OR":
            """For every term in the string add the UUIDs to the results set."""
            for term in terms_set:
                results.update(
                    m for m in self.index.get(term, set()) if m.uuid_type in uuid_types
                )
        elif logic == "AND":
            """Every term in the terms string must be in the description."""
            for term in terms_set:
                term_matches = {
                    m
                    for m in self.index.get(term, set())
                    if terms_set.issubset(m for m in m.description.lower().split(" "))
                    and m.uuid_type in uuid_types
                }
                if not results:
                    results.update(term_matches)
                else:
                    results.intersection_update(term_matches)
        elif logic == "SUBSTR":
            """The description must match the a substring of the description."""
            lower_term_str = terms.lower()
            for term in terms_set:
                results.update(
                    m
                    for m in self.index.get(term, set())
                    if lower_term_str in m.description.lower()
                    and m.uuid_type in uuid_types
                )
        return results
