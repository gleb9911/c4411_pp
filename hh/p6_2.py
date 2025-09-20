try:
    print("start code")
    print(10/0)
    print("no error")
except NameError:
    print("we have a NameError")
except ZeroDivisionError:
    print("we have a OdivError")
print("code  after")