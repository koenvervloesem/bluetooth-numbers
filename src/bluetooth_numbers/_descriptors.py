"""Module with UUIDs and names for Bluetooth descriptors.

Usage:

>>> from bluetooth_numbers import descriptor
>>> descriptor[0x2901]
'Characteristic User Descriptor'
"""

from bluetooth_numbers.dicts import UUIDDict

descriptor = UUIDDict(
    {
        0x2900: "Characteristic Extended Properties",
        0x2901: "Characteristic User Descriptor",
        0x2902: "Client Characteristic Configuration",
        0x2903: "Server Characteristic Configuration",
        0x2904: "Characteristic Presentation Format",
        0x2905: "Characteristic Aggregate Format",
        0x2906: "Valid Range",
        0x2907: "External Report Reference",
        0x2908: "Report Reference",
        0x2909: "Number of Digitals",
        0x290A: "Value Trigger Setting",
        0x290B: "Environmental Sensing Configuration",
        0x290C: "Environmental Sensing Measurement",
        0x290D: "Environmental Sensing Trigger Setting",
        0x290E: "Time Trigger Setting",
        0x290F: "Complete BR-EDR Transport Block Data",
    },
)
