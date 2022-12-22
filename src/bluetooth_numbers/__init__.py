# pylint: skip-file
"""bluetooth-numbers

Python package with a wide set of numbers related to Bluetooth

This project offers a Python package with a wide set of numbers related to Bluetooth,
so Python projects can easily use these numbers.

Get the description of a company ID:

>>> from bluetooth_numbers import company
>>> company[0x0499]
'Ruuvi Innovations Ltd.'

Get the description of a service UUID:

>>> from bluetooth_numbers import service
>>> from uuid import UUID
>>> service[0x180F]
'Battery Service'
>>> service[UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")]
'Nordic UART Service'

Get the description of a characteristic UUID:

>>> from bluetooth_numbers import characteristic
>>> from uuid import UUID
>>> characteristic[0x2A37]
'Heart Rate Measurement'
>>> characteristic[UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")]
'UART RX Characteristic'

Get the description of a descriptor UUID:

>>> from bluetooth_numbers import descriptor
>>> descriptor[0x2901]
'Characteristic User Descriptor'

Get the description of an OUI:

>>> from bluetooth_numbers import oui
>>> oui["58:2D:34"]
'Qingping Electronics (Suzhou) Co., Ltd'
"""
import sys

# Public API for easier importing
from ._characteristics import characteristic
from ._companies import company
from ._descriptors import descriptor
from ._ouis import oui
from ._services import service

__all__ = ["characteristic", "company", "descriptor", "oui", "service"]

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "bluetooth-numbers"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
