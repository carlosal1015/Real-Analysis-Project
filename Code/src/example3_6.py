def somefun(arg1, arg2, kwarg1=True, kwarg2=0):
    print(arg1, arg2, kwarg1, kwarg2)


print(somefun("Hello", [1, 2]))
print(somefun("Hello", [1, 2], kwarg1="Hi"))
print(somefun("Hello", [1, 2], kwarg2="Hi"))
print(somefun("Hello", [1, 2], kwarg2="Hi", kwarg1=6))

print(somefun(kwarg2="Hello", arg1="Hi", kwarg1=6, arg2=[1,2],))