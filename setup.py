import setuptools
from setuptools import setup, find_packages

install_requires = []

setup(
      name="roster",
      packages=find_packages(exclude=[]),
      version="0.0.1",
      zip_safe=True,
      include_package_data=True,
      scripts=['roster/new_roster']
)