from timescale.classes.timescale import Timescale
Timescale2 = Timescale([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10], 'documentation example')

print ("La escala de tiempo {} se llama {}.".format(Timescale2.ts, Timescale2.name))

print(Timescale2)