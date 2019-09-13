# 4.1.6.11 RINGKASAN BAGIAN (2/3)


#assign items to variabel using get()
# -----------------------------------------------
polEngDict = {
    "kwiat" : "flower",
    "woda"  : "water",
    "gleba" : "soil"
    }

item1 = polEngDict["gleba"]    # ex. 1
print(item1)    # outputs: soil

item2 = polEngDict.get("woda")
print(item2)    # outputs: water

# add new pair to dictionary
# -----------------------------------------------

polEngDict["zamek"] = "lock"

item = polEngDict["zamek"]   
print(item)     # outputs: lock
print(polEngDict)


# remove spesific item on dictionary
# -----------------------------------------------
del polEngDict["zamek"]    # remove an item
print(polEngDict)

# clear item values on dictionary
# -----------------------------------------------
polEngDict.clear()
print(polEngDict)

# delete  dictionary
# -----------------------------------------------
# del polEngDict   