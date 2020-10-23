from glob import glob
from os.path import basename, splitext
from setuptools import setup, find_packages

def _get_requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="DADecorator",
    version="1.0.0",
    license="MIT",
    description="Decorator sample",
    author="Akagawa Daisuke",
    url="http://github.com/Akasan",
    packages=["DADecorator"],
    include_package_data=True,
    zip_safe=False,
    install_requires=_get_requires_from_file("requirements.txt"),
)
