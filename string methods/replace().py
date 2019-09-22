# 5.1.9.11 String methods

# two parameters replace

# Demonstrating the replace() method
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# three parameters replace (word, new word, limits of replace)

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

text = 'here is are guess is the most intellegence is the powerful limits is most underdogs is the nobody'

print(text.replace('is', 'REPLACE', 1))
print(text.replace('is', 'REPLACE', 2))
print(text.replace('is', 'REPLACE', 3))