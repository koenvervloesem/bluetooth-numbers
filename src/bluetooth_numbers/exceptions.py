"""Module with exceptions raised by this library."""


class BluetoothNumbersError(Exception):
    """Base class for all exceptions raised by this library."""


class No16BitIntegerError(BluetoothNumbersError):
    """Exception raised when an integer is not a 16-bit number."""


class NonStandardUUIDError(BluetoothNumbersError):
    """Exception raised when a 128-bit UUID is not a standard Bluetooth UUID."""


class UnknownCICError(BluetoothNumbersError):
    """Exception raised when a CIC is not known."""


class UnknownOUIError(BluetoothNumbersError):
    """Exception raised when an OUI is not known."""


class UnknownUUIDError(BluetoothNumbersError):
    """Exception raised when a UUID is not known."""


class WrongOUIFormatError(BluetoothNumbersError):
    """Exception raised when a string isn't a supported format for an OUI."""
