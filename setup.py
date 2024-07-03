# setup.py
from setuptools import setup, find_packages

setup(
    name="anarchygraph",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ipycytoscape",
        "hypothesis",
        "pytest",
        "pyperf",
    ],
    url="https://pypi.org/project/anarchygraph/",
)


