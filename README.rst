.. image:: https://github.com/koenvervloesem/bluetooth-numbers/workflows/tests/badge.svg
    :alt: Continuous Integration
    :target: https://github.com/koenvervloesem/bluetooth-numbers/actions
.. image:: https://codecov.io/gh/koenvervloesem/bluetooth-numbers/branch/main/graph/badge.svg?token=6NR980W2VX
    :alt: Code coverage
    :target: https://codecov.io/gh/koenvervloesem/bluetooth-numbers
.. image:: https://img.shields.io/pypi/v/bluetooth-numbers.svg
    :alt: Python package version
    :target: https://pypi.org/project/bluetooth-numbers/
.. image:: https://img.shields.io/pypi/pyversions/bluetooth-numbers.svg
    :alt: Supported Python versions
    :target: https://python.org/
.. image:: https://readthedocs.org/projects/bluetooth-numbers/badge/?version=latest
    :target: https://bluetooth-numbers.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/github/license/koenvervloesem/bluetooth-numbers.svg
    :alt: License
    :target: https://github.com/koenvervloesem/bluetooth-numbers/blob/main/LICENSE.txt

|

=================
bluetooth-numbers
=================


    Python package with a wide set of numbers related to Bluetooth


This project offers a Python package with a wide set of numbers related to Bluetooth, so Python projects can easily use these numbers. The goal of this project is to provide a shared resource so various Python projects that deal with Bluetooth don't have to replicate this effort by rolling their own database and keeping it updated.

The following sources are used:

* Nordic Semiconductor's `Bluetooth Numbers Database <https://github.com/NordicSemiconductor/bluetooth-numbers-database>`_ for Company IDs, Service UUIDs, Characteristic UUIDs and Descriptor UUIDs
* `Bluetooth Assigned Numbers <https://www.bluetooth.com/specifications/assigned-numbers/>`_ for SDO Service UUIDs and Member Service UUIDs
* The `IEEE database of OUIs <https://standards-oui.ieee.org/oui/oui.txt>`_ for prefixes of Bluetooth addresses

Installation
============

You can install bluetooth-numbers as a package from PyPI with pip::

    pip install bluetooth-numbers

Usage
=====

Get the description of a company ID:

.. code-block:: python

	>>> from bluetooth_numbers import company
	>>> company[0x0499]
	'Ruuvi Innovations Ltd.'

Get the description of a service UUID:

.. code-block:: python

	>>> from bluetooth_numbers import service
	>>> from uuid import UUID
	>>> service[0x180F]
	'Battery Service'
	>>> service[UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E")]
	'Nordic UART Service'

Get the description of a characteristic UUID:

.. code-block:: python

	>>> from bluetooth_numbers import characteristic
	>>> from uuid import UUID
	>>> characteristic[0x2A37]
	'Heart Rate Measurement'
	>>> characteristic[UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E")]
	'UART RX Characteristic'

Get the description of a descriptor UUID:

.. code-block:: python

	>>> from bluetooth_numbers import descriptor
	>>> descriptor[0x2901]
	'Characteristic User Descriptor'

Get the description of an OUI:

.. code-block:: python

	>>> from bluetooth_numbers import oui
	>>> oui["58:2D:34"]
	'Qingping Electronics (Suzhou) Co., Ltd'

License
=======

This project is provided by Koen Vervloesem as open source software with the MIT license. See the `LICENSE <https://github.com/koenvervloesem/bluetooth-numbers/blob/main/LICENSE.txt>`_ file for more information.

See also the `license for the Bluetooth Numbers Database <https://github.com/NordicSemiconductor/bluetooth-numbers-database/blob/master/LICENSE>`_ used in this package.
