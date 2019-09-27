# 4.1.6.5 Tuples and dictionaries, 4.1.6.6 Tuples and dictionaries | methods


# how to use dictionary :

dict = {"dog" : "chien", "cat" : "chat", "horse" : "cheval"} 
phoneNumbers = {'boss' : 5551234567, 'Suzy' : 22657854310}
emptyDictionary = {}

print(dict['cat'])
print(phoneNumbers['Suzy'])

# exmple for eror (the key is not available)

# print(phoneNumbers['president'])

print()

# how to use the keys()

print('unsorted dict')

for key in dict.keys():
    print(key, "->", dict[key]) 
print()

# sorted key output

print('sorted dict')

for key in sorted(dict.keys()):
    print(key, "->", dict[key]) 