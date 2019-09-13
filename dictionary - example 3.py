#4.1.6.7 Tuples and dictionaries | methods

# key - item pairs ---> values - items

dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

# output is a pairs of key and item. use dict.item
# english = key, french = item
for english, french in dict.items():
    print(english, "->", french)
print()

# output is a pairs of key and item in default output use dict.item, french recognize as a 'dict'
for french in dict.items():
    print(french)
print()

# output is a key list use dict.values()
for french in dict.values():
    print(french)