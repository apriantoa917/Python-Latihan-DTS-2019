# 3.1.4.13 LAB: The basics of lists - the Beatles

#step 1

beatles = []

print(beatles)

# step 2

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Step 2:", beatles)

# step 3

for i in range(2):
    member = input("next members : ")
    beatles.append(member)

print("Step 3:", beatles)

# step 4

for i in range(2):
    length = len(beatles)-1
    del beatles [length]

print("Step 4:", beatles)

# step 5

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))