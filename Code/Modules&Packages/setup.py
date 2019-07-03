import sys
import os
import glob

modules = [
	'timescale.calculus',
	'timescale.core',
	'timescale.discrete',
	'timescale.functions',
	'timescale.plotting',
	'timescale.sets',
	'timescale.solvers'
]

tests = [
	'timescale.calculus.tests',
	'timescale.core.tests',
	'timescale.discrete.tests',
	'timescale.functions.tests',
	'timescale.plotting.tests',
	'timescale.sets.tests',
	'timescale.solvers.tests'
]

long_description = '''SymPy is a Python library for time scale calculus.
Time scale calculus is a unification and extension of differential and
difference calculus in which one does calculus upon a set T of real numbers
called a time scale. It aims to become a full-featured computer algebra system
(CAS) while keeping the code as simple as possible in order to be comprehensible
and easily extensible.'''

with open(os.path.join(dir_setup, 'sympy', 'release.py')) as f:
    # Defines __version__
	exec(f.read())

if __name__ == '__main__':
	setup(name='sympy',
		  version=__version__,
