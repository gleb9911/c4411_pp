def check_material(amount_of_material, Limit_value):
    if amount_of_material > Limit_value:
        return "Enough material"
    else:
        raise BuildingError(amount_of_material)
material = 323
check_material(material, 300)
