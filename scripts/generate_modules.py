"""Generate Python modules for Bluetooth numbers."""
from __future__ import annotations

import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

DATA_DIR = "data"
BLUETOOTH_NUMBERS_DIR = f"{DATA_DIR}/bluetooth-numbers-database/v1"
TEMPLATE_DIR = "templates"
CODE_DIR = "src/bluetooth_numbers"
UUID_TEMPLATE = "uuids.py.jinja"
CIC_TEMPLATE = "companies.py.jinja"
OUI_TEMPLATE = "ouis.py.jinja"
OUI_RE = re.compile(r"^([0-9A-F]{2}-[0-9A-F]{2}-[0-9A-F]{2})\s*\(hex\)\s+(.*)\s*$")

file_loader = FileSystemLoader(TEMPLATE_DIR)
env = Environment(loader=file_loader)


def generate_uuid16_dictionary(kind: str) -> dict[int, str]:
    """Generate 16-bit UUID dictionary for a module.

    Args:
        kind (str): Should be "sdo_service".

    Returns:
        dict[int, str]: A dict with 16-bit UUIDs as keys.
    """
    uuid16_dict = {}

    with (Path(DATA_DIR) / f"{kind}_uuids.json").open() as json_file:
        json_data = json.loads(json_file.read())
        for number in json_data:
            name = number["name"]
            uuid = number["uuid"]
            uuid16_dict[uuid] = name

    return uuid16_dict


def generate_uuid_dictionaries(kind: str) -> tuple[dict[int, str], dict[str, str]]:
    """Generate UUID dictionaries for a module.

    Args:
        kind (str): Should be "service", "characteristic", or "descriptor".

    Returns:
        tuple[dict[int, str], dict[str, str]]: A tuple of dicts. The first dict
          has 16-bit UUIDs as keys, the second one 128-bit UUIDs.
    """
    uuid16_dict = {}
    uuid128_dict = {}

    with (Path(BLUETOOTH_NUMBERS_DIR) / f"{kind}_uuids.json").open() as json_file:
        json_data = json.loads(json_file.read())
        for number in json_data:
            name = number["name"]
            uuid = number["uuid"]
            if len(uuid) == 4:
                uuid16_dict[uuid] = name
            else:
                uuid128_dict[uuid] = name

    return uuid16_dict, uuid128_dict


def generate_uuid_module(
    kind: str, uuid16_dict: dict[int, str], uuid128_dict: dict[str, str]
) -> None:
    """Generate Python module for UUIDs.

    Args:
        kind (str): Should be "service", "characteristic", or "descriptor".
        uuid16_dict (dict[int, str]): Dict with 16-bit UUIDs as keys.
        uuid128_dict (dict[str, str]): Dict with 128-bit UUIDs as keys.
    """
    template = env.get_template(UUID_TEMPLATE)
    with (Path(CODE_DIR) / f"_{kind}s.py").open("w") as python_file:
        python_file.write("# pylint: skip-file\n")
        python_file.write(
            template.render(uuids16=uuid16_dict, uuids128=uuid128_dict, uuid_dict=kind)
        )


def generate_cic_dictionary() -> dict[str, str]:
    """Generate Company ID Code dictionary for a module.

    Returns:
        dict[str, str]: A dict with CIC keys and their name.
    """
    cic_dict = {}

    with (Path(BLUETOOTH_NUMBERS_DIR) / "company_ids.json").open() as json_file:
        json_data = json.loads(json_file.read())
        for number in json_data:
            code = f"{number['code']:#06x}"
            name = number["name"].replace('"', '\\"')
            cic_dict[code] = name

    return cic_dict


def generate_cic_module(cic_dict: dict[str, str]) -> None:
    """Generate Python module for Company ID Codes.

    Args:
        cic_dict (dict[str, str]): The dict with CICs to generate a Python
          module for.
    """
    template = env.get_template(CIC_TEMPLATE)
    with (Path(CODE_DIR) / "_companies.py").open("w") as python_file:
        python_file.write("# pylint: skip-file\n")
        python_file.write(template.render(cics=cic_dict))


def generate_oui_dictionary() -> dict[str, str]:
    """Generate OUI dictionary for a module.

    Returns:
        dict[str, str]: A dict with OUI prefixes and their name.
    """
    oui_dict = {}

    with (Path(DATA_DIR) / "oui.txt").open() as txt_file:
        for line in txt_file:
            extracted = OUI_RE.match(line)
            if extracted:
                oui_dict[extracted.group(1).replace("-", ":")] = extracted.group(2)

    return oui_dict


def generate_oui_module(oui_dict: dict[str, str]) -> None:
    """Generate Python module for OUIs.

    Args:
        oui_dict (dict[str, str]): The dict with OUIs to generate a Python
          module for.
    """
    template = env.get_template(OUI_TEMPLATE)
    with (Path(CODE_DIR) / "_ouis.py").open("w") as python_file:
        python_file.write("# pylint: skip-file\n")
        python_file.write(template.render(ouis=oui_dict))


if __name__ == "__main__":
    # Generate module for service UUIDs
    service_uuid16, service_uuid128 = generate_uuid_dictionaries("service")
    member_service_uuid16 = generate_uuid16_dictionary("member_service")
    sdo_service_uuid16 = generate_uuid16_dictionary("sdo_service")
    # Don't let the UUIDs from the Assigned Numbers document overwrite the ones from the
    # Bluetooth Numbers Database because the latter has the names of the services, which
    # give more information than the names of the companies in the Assigned Numbers
    # document.
    service_uuid16.update(
        {
            key: value
            for key, value in member_service_uuid16.items()
            if key not in service_uuid16
        }
    )
    service_uuid16.update(sdo_service_uuid16)
    generate_uuid_module("service", service_uuid16, service_uuid128)

    # Generate module for characteristic UUIDs
    characteristic_uuid16, characteristic_uuid128 = generate_uuid_dictionaries(
        "characteristic"
    )
    generate_uuid_module(
        "characteristic", characteristic_uuid16, characteristic_uuid128
    )

    # Generate module for descriptor UUIDs
    descriptor_uuid16, descriptor_uuid128 = generate_uuid_dictionaries("descriptor")
    generate_uuid_module("descriptor", descriptor_uuid16, descriptor_uuid128)

    # Generate module for Company ID Codes
    cics = generate_cic_dictionary()
    generate_cic_module(cics)

    # Generate module for OUIs
    ouis = generate_oui_dictionary()
    generate_oui_module(ouis)
