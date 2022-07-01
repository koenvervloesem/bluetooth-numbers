"""Generate Python modules for Bluetooth numbers."""
import json
from pathlib import Path
from typing import Dict, Tuple

from jinja2 import Environment, FileSystemLoader

BLUETOOTH_NUMBERS_DIR = "bluetooth-numbers-database/v1"
TEMPLATE_DIR = "templates"
CODE_DIR = "src/bluetooth_numbers"
UUID_TEMPLATE = "uuids.py.jinja"
CIC_TEMPLATE = "companies.py.jinja"

file_loader = FileSystemLoader(TEMPLATE_DIR)
env = Environment(loader=file_loader)


def generate_uuid_dictionaries(kind: str) -> Tuple[Dict[int, str], Dict[str, str]]:
    """Generate UUID dictionaries for a module.

    The parameter :param:`kind` should be "service", "characteristic", or "descriptor".

    Returns a tuple of dicts with uuid16 and uuid128 keys and their name.
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
    kind: str, uuid16_dict: Dict[int, str], uuid128_dict: Dict[str, str]
) -> None:
    """Generate Python module for UUIDs.

    The parameter :param:`kind` should be "service", "characteristic", or "descriptor".
    """
    template = env.get_template(UUID_TEMPLATE)
    with (Path(CODE_DIR) / f"{kind}s.py").open("w") as python_file:
        python_file.write(
            template.render(uuids16=uuid16_dict, uuids128=uuid128_dict, uuid_dict=kind)
        )


def generate_cic_dictionary() -> Dict[int, str]:
    """Generate Company ID Code dictionary for a module.

    Returns a dict with CIC keys and their name.
    """
    cic_dict = {}

    with (Path(BLUETOOTH_NUMBERS_DIR) / "company_ids.json").open() as json_file:
        json_data = json.loads(json_file.read())
        for number in json_data:
            code = f"{number['code']:#06x}"
            name = number["name"].replace('"', '\\"')
            cic_dict[code] = name

    return cic_dict


def generate_cic_module(cic_dict: Dict[int, str]) -> None:
    """Generate Python module for Company ID Codes."""
    template = env.get_template(CIC_TEMPLATE)
    with (Path(CODE_DIR) / "companies.py").open("w") as python_file:
        python_file.write(template.render(cics=cic_dict))


# Generate modules for UUIDs
service_uuid16, service_uuid128 = generate_uuid_dictionaries("service")
generate_uuid_module("service", service_uuid16, service_uuid128)
characteristic_uuid16, characteristic_uuid128 = generate_uuid_dictionaries(
    "characteristic"
)
generate_uuid_module("characteristic", characteristic_uuid16, characteristic_uuid128)
descriptor_uuid16, descriptor_uuid128 = generate_uuid_dictionaries("descriptor")
generate_uuid_module("descriptor", descriptor_uuid16, descriptor_uuid128)

# Merge all 16-bit UUIDS and all 128-bit UUIDs
# all_uuid16 = {**service_uuid16, **characteristic_uuid16, **descriptor_uuid16}
# all_uuid128 = {**service_uuid128, **characteristic_uuid128, **descriptor_uuid128}
# generate_uuid_module("uuids", all_uuid16, all_uuid128)

# Generate module for Company ID Codes
cics = generate_cic_dictionary()
generate_cic_module(cics)
