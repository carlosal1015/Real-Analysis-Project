def C2F(C):
    """Convert Celsius degree (C) to Fahrenheit."""
    return (9.0/5)*C + 32


def line(x0, y0, x1, y1):
    """
    Compute the coefficients a and b in the mathematical
    expression for a straight line y = a*x + b that goes
    through  two points (x0,y0) and (x1,y1).


    x0, y0: a point on the line (floats).
    x1, y1: another point on the line (floats).
    return: coefficients a, b (floats) for the line (y=a*x+b).
    """
    a = (y1 - y0)/float(x1 - x0)
    b = y0 - a*x0
    return a, b


print(line.__doc__)