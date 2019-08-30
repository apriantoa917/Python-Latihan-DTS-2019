# list biasa

a = ["String", 0, True]

print(a)

# nested list

b = ["String", 0, False, ["Nested String", 1, True]]

print(b)

c = b[3]

print(c)

d = b[3][0]

print(d)

# super nested list

e = ["String", 0, False, ["Nested String", 1, True, [True, [False]]]]

f = e[3][3][1] #mengakses False di dalam list terdalam

print(f)