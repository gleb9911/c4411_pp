def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"sorry, we can't work with {type(var_1)}, we need class str")