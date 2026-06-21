"""Module with UUIDs and names for Bluetooth protocols.

Usage:

>>> from bluetooth_numbers import protocol
>>> protocol[0x0003]
'RFCOMM'
"""

from bluetooth_numbers.dicts import UUIDDict

protocol = UUIDDict(
    {
        0x0001: "SDP",
        0x0002: "UDP",
        0x0003: "RFCOMM",
        0x0004: "TCP",
        0x0005: "TCS-BIN",
        0x0006: "TCS-AT",
        0x0007: "ATT",
        0x0008: "OBEX",
        0x0009: "IP",
        0x000A: "FTP",
        0x000C: "HTTP",
        0x000E: "WSP",
        0x000F: "BNEP",
        0x0010: "UPNP",
        0x0011: "HID Protocol",
        0x0012: "HardcopyControlChannel",
        0x0014: "HardcopyDataChannel",
        0x0016: "HardcopyNotificationChannel",
        0x0017: "AVCTP",
        0x0019: "AVDTP",
        0x001B: "CMTP",
        0x001E: "MCAP Control Channel",
        0x001F: "MCAP Data Channel",
        0x0100: "L2CAP",
    },
)
