def L2(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
    from math import log
    exact_error = log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error


x = 100
value, approximate_error, exact_error = L2(x, 100)


def table(x):
    from math import log
    print("x = {:2}, ln(1+x)={:2}".format(x, log(1+x)))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L2(x, n)
        print("n = {:2}, value = {:2}, next term = {:2}, error = {:2}".format(n, value, next, error))


print(table(10))

print(table(100))