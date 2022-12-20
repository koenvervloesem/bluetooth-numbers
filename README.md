# Bluetooth numbers for Python

[![Continous Integration](https://github.com/koenvervloesem/bluetooth-numbers/workflows/Tests/badge.svg)](https://github.com/koenvervloesem/bluetooth-numbers/actions)
[![PyPI package version](https://img.shields.io/pypi/v/bluetooth-numbers.svg)](https://pypi.org/project/bluetooth-numbers)
[![Python versions](https://img.shields.io/pypi/pyversions/bluetooth-numbers.svg)](https://www.python.org)
[![GitHub license](https://img.shields.io/github/license/koenvervloesem/bluetooth-numbers.svg)](https://github.com/koenvervloesem/bluetooth-numbers/blob/main/LICENSE.txt)

This project offers a Python package with a wide set of numbers related to Bluetooth, so Python projects can easily use these numbers. The goal of this project is to provide a shared resource so various Python projects that deal with Bluetooth don't have to replicate this effort by rolling their own database and keeping it updated.

The following sources are used:

* Nordic Semiconductor's [Bluetooth Numbers Database](https://github.com/NordicSemiconductor/bluetooth-numbers-database) for Company IDs, Service UUIDs, Characteristic UUIDs and Descriptor UUIDs
* [Bluetooth Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/) for SDO Service UUIDs and Member Service UUIDs
* The [IEEE database of OUIs](https://standards-oui.ieee.org/oui/oui.txt) for prefixes of Bluetooth addresses

## Installation

The package can be installed from PyPI:

```shell
pip install bluetooth-numbers
```

## Usage

Get the description of a company ID:

```python
>>> from bluetooth_numbers.companies import company
>>> company[0x0499]
'Ruuvi Innovations Ltd.'
```

Get the description of a service UUID:

```python
>>> from bluetooth_numbers.services import service
>>> from uuid import UUID
>>> service[0x180F]
'Battery Service'
>>> service[UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")]
'Nordic UART Service'
```

Get the description of a characteristic UUID:

```python
>>> from bluetooth_numbers.characteristics import characteristic
>>> from uuid import UUID
>>> characteristic[0x2A37]
'Heart Rate Measurement'
>>> characteristic[UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")]
'UART RX Characteristic'
```

Get the description of a descriptor UUID:

```python
>>> from bluetooth_numbers.descriptors import descriptor
>>> descriptor[0x2901]
'Characteristic User Descriptor'
```

Get the description of a OUI:

```python
>>> from bluetooth_numbers.ouis import oui
>>> oui["58:2D:34"]
'Qingping Electronics (Suzhou) Co., Ltd'
```

## License

This project is provided by Koen Vervloesem as open source software with the MIT license. See the [LICENSE](https://github.com/koenvervloesem/bluetooth-numbers/blob/main/LICENSE.txt) file for more information.

See also the [license for the Bluetooth Numbers Database](https://github.com/NordicSemiconductor/bluetooth-numbers-database/blob/master/LICENSE) used in this package.
