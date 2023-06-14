# Separating the code in verious module

# import converters           # import (converters) object
# print(converters.kg_to_lbs(70))
# print(converters.lbs_to_kg(60))


from converters import lbs_to_kg    # import (specific function) and it is directly access,no object call is important
print(lbs_to_kg(60))