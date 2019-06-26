#!/opt/conda/bin/python3
"""Setuptools based setup script for TimeScale

You can use Setuptools (https://setuptools.readthedocs.io/en/latest/)
to automatically handle dependencies. For the easiest installation
just type the command (you'll probably need root privileges for that):
	python setup.py install
This will install the library in the default location. For instructions on
how to customize the install procedure read the output of:
	python setup.py --help install
In addition, there are some other commands:
	python setup.py clean -> will clean all trash (*.pyc and stuff)
	python setup.py test  -> will run the complete test suite
	python setup.py bench -> will run the complete benchmark suite
	python setup.py audit -> will run pyflakes checker on source code
To get a full list of available commands, read the output of:
	python setup.py --help-commands
Or, if all else fails, feel free to write at
caznaranl@uni.pe and ask for help.
"""
from setuptools import setup, find_packages
from io import open

requirements = [
	'symengine>=0.3.1.dev0',
	'numpy',
	'scipy',
]

setup(
	name = "timescale",
	version = "0.1",
	description = ("Paquete para el cálculo en escala de tiempo."),
	author = "Tom Cuchta",
	author_email = "tomcuchta@gmail.com",
	license = "GPL V3",
	url = "https://github.com/tomcuchta/timescalecalculus",
	packages = find_packages(),
	scripts = [],
	install_requires = []
)
