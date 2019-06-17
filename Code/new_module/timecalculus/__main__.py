from timecalculus.timescale import Timescale
from timecalculus.definitions import *
from timecalculus.differenciation import *
from timecalculus.integration import *
from timecalculus.ode import *
from timecalculus.plot import *

from timecalculus.smart_door import open, close
if __name__ == "__main__":
	open()
	close()

Timescale1 = Timescale([0, 1, 2, 3, 4, 5, 6, 7], 'documentation example')

print(Timescale1.ts)