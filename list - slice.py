# 3.1.6.2 Operations on lists | slices

# slice : copy part / full elemen list ke list baru

# copy semua elemen list

old_list = [0, 1, 2, 3]

print("old list : ",old_list)

new_list = old_list

print("new list : ", new_list)

# atau

new_list = old_list[:]  # : = semua elemen

print("new list : ", new_list)

# copy elemen tertentu di list

part_list = old_list[0] # hanya copy elemen index ke-0

print("part list : ", part_list)

part_list = old_list[0:2]   # copy elemen index 0-1

print("part list : ", part_list)
