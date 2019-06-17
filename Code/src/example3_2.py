def yfunc(t, v0):
    g = 9.81
    y = v0*t - 0.5*g*t**2
    dydt = v0 - g*t
    return y, dydt


position, velocity = yfunc(0.6, 3)

t_values = [0.05*i for i in range(10)]

for t in t_values:
    position, velocity = yfunc(t, v0=5)
    print("t = {:5}, position = {:5}, velocity = {:5}".format(t, position, velocity))
