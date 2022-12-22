=========
Changelog
=========

Version 1.0.0 (2022-12-22)
==========================

This is a major release with some breaking changes.

Whereas in previous versions you did:

.. code-block:: python

    from bluetooth_numbers.companies import company

This is now:

.. code-block:: python

    from bluetooth_numbers import company

The OUIs and CICs now also use their own dict-like class, just like the services, characteristics and descriptions already did.

All searches for numbers now raise package-specific exceptions when something's wrong, for instance for invalid or unknown values.

Look at the `API documentation <https://bluetooth-numbers.readthedocs.io/en/latest/api/modules.html>`_ for all these changes.

What's Changed
--------------

* Documentation improvements with docstrings by @koenvervloesem in https://github.com/koenvervloesem/bluetooth-numbers/pull/1
* Run doctests in CI to make sure examples in the documentation work by @koenvervloesem in https://github.com/koenvervloesem/bluetooth-numbers/pull/2
* Add package data for minimum Python version and keywords by @koenvervloesem in https://github.com/koenvervloesem/bluetooth-numbers/pull/3
* Run mypy in pre-commit hook by @koenvervloesem in https://github.com/koenvervloesem/bluetooth-numbers/pull/4
* Add custom exceptions for this package by @koenvervloesem in https://github.com/koenvervloesem/bluetooth-numbers/pull/5
* Change public API for easier importing by @koenvervloesem in https://github.com/koenvervloesem/bluetooth-numbers/pull/6

Version 0.2.1 (2022-12-20)
==========================

This bugfix release updates the Bluetooth Numbers Database to commit `3d0f452 <https://github.com/NordicSemiconductor/bluetooth-numbers-database/tree/3d0f452460237f76d7e11d8cd0de8c1cba46b62a>`_ (December 20 2022). This fixes some issues with Philips Hue UUIDs. Upstream PR: `NordicSemiconductor/bluetooth-numbers-database#94 <https://github.com/NordicSemiconductor/bluetooth-numbers-database/pull/94>`_.

Version 0.2.0 (2022-12-19)
==========================

* Adds SDO service UUIDs.
* Adds member service UUIDs.

Both types of UUIDs are taken from the Bluetooth Assigned Numbers document from 2022-12-15.

Version 0.1.3 (2022-12-18)
==========================

* Adds typing to company dict.
* Tracks `bluetooth-numbers-database @ 4a5f38a <https://github.com/NordicSemiconductor/bluetooth-numbers-database/tree/4a5f38a7b41795b79acbcca30165ead7cb11ad45>`_.


Version 0.1.2 (2022-07-05)
==========================

Updates company IDs, services, characteristics and descriptors. This tracks `bluetooth-numbers-database @ 2178b94 <https://github.com/NordicSemiconductor/bluetooth-numbers-database/tree/2178b94e52d30adab10a972a753f49229deed6ac>`_ (July 5 2022).

Version 0.1.1 (2022-07-01)
==========================

Initial release
