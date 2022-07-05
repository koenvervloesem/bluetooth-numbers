#!/usr/bin/env python3

from pathlib import Path

import setuptools

project_dir = Path(__file__).parent

setuptools.setup(
    name="bluetooth-numbers",
    version="0.1.2",
    description="Database of all relevant numbers in the Bluetooth specification",
    long_description=project_dir.joinpath("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    keywords=["bluetooth", "ble", "bluetooth-low-energy"],
    author="Koen Vervloesem",
    author_email="koen@vervloesem.eu",
    url="https://github.com/koenvervloesem/bluetooth-numbers",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    package_data={"bluetooth_numbers": ["py.typed"]},
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
