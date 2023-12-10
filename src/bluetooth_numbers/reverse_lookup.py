from __future__ import annotations

import typing
from typing import Literal
from uuid import UUID

from bluetooth_numbers import characteristic, company, descriptor, oui, service

LOGIC = Literal["OR", "AND", "EXACT"]
UUID_TYPES = Literal["characteristic", "company", "descriptor", "ouis", "service"]
UUID_TYPE_DEFAULT = ("characteristic", "company", "descriptor", "ouis", "service")

class Match(typing.NamedTuple):
    """Named tuple to hold a UUID and its description."""
    uuid: str | UUID | int
    description: str
    uuid_type: str

class ReverseLookup:
    """Class to build a reveers lookup index and return the UUIDs for a given term(s)."""

    def __init__(self):
        self.index = self._build_index()

    def _build_index(self)-> dict:
        """Build dictionary (index) of terms to UUIDs.

        Returns:
            dict: Dictionary of terms to UUIDs.
            """
        reverse_lookup = {}
        uuid_dicts = ((characteristic, "characteristic"), (company, "company"), (descriptor, "descriptor"),
                      (oui, "ouis"), (service, "service"))
        for uuid_dict, uuid_type in uuid_dicts:
            for uuid, description in uuid_dict.items():
                for term in description.lower().split(" "):
                    if term not in reverse_lookup:
                        reverse_lookup[term] = set()
                    reverse_lookup[term].add(Match(uuid, description, uuid_type))
        return reverse_lookup

    def lookup(self, terms: str, uuid_types: list[UUID_TYPES] = UUID_TYPE_DEFAULT,
               logic: LOGIC = "OR") -> set:
        """Return the UUIDs for a given term(s).

        Args:
            terms: String with the term(s) to search for.
            uuid_types: List of UUID types to search in.
            logic: Search logic to use. Can be "OR", "AND" or "EXACT".

        Returns:
            set or Match, named tuples, (uuid, description, uuid_type)
        """
        terms_set = set(terms.lower().split(" "))
        results = set()
        if logic == "OR":
            """For every term in the string add the UUIDs to the results set."""
            for term in terms_set:
                results.update(m for m in self.index.get(term, set())
                               if m.uuid_type in uuid_types)
        elif logic == "AND":
            """Every term in the terms string must be in the description."""
            print(f"uuid_types: {uuid_types}")
            print(f"terms_set: {terms_set}")
            for term in terms_set:
                term_matches = set(m for m in self.index.get(term, set()) if
                                            terms_set.issubset(set(m for m in m.description.lower().split(" "))) and m.uuid_type in uuid_types)
                print(f"term_matches: {term_matches}")
                if not results:
                    results.update(term_matches)
                else:
                    results.intersection_update(term_matches)
        elif logic == "EXACT":
            """The description must match the terms string exactly."""
            lower_term_str = terms.lower()
            for term in terms_set:
                results.update(m for m in self.index.get(term, set()) if
                               lower_term_str in m.description.lower() and m.uuid_type in uuid_types)
        return results
