# 4.1.6.8 Tuples and dictionaries

# update items value
dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}

print(dict)

dict['cat'] = 'minou'

print(dict)

# adding new pairs 

dict['swan'] = 'cygne'

print(dict)

# another way to insert new pairs

dict.update({"duck" : "canard"})

print(dict)

# remove a pairs

del dict['dog']

print(dict)

# remove last item in dictionary 

dict.popitem()

print(dict) 

