"""
    Función Salto hacia adelante:

    \sigma(t) = \inf \{z\in\mathds{T} : z>t \}
"""

def sigma(self, t):
    tIndex = 0
    tNext = None
    iterations = 0

    for x in self.ts:
        if (not isinstance(x, list) and t == x) or (isinstance(x, list) and t >= x[0] and t <= x[1]):
            tIndex = iterations
            break

        iterations = iterations + 1

    if (tIndex + 1) == len(self.ts):
        return t

    elif isinstance(self.ts[tIndex], list):
        if (t != self.ts[tIndex][1]):
            return t

        else:
            if (isinstance(self.ts[tIndex + 1], list)):
                return self.ts[tIndex + 1][0]

            else:
                return self.ts[tIndex + 1]

    else:
        tNext = self.ts[tIndex + 1]

        if isinstance(tNext, list):
            return tNext[0]

        else:
            return tNext


"""
    Función Salto hacia atrás:

    \rho(t) = \sup \{ z\in\mathds{T} : z<t \}
"""

"""
    Función de granicidad:
    
    \mu(t) = \sigma(t) - t
"""

"""
    Función de granicidad minimal:

    \mu_{\ast} = \inf_{\tau\in\left[s,\infty\right)\cap\mathds{T}}\mu(t).
"""

Timescale2 = Timescale([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 , 10], 'documentation example')