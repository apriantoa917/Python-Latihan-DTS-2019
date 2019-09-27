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


# tambahan

# copy hingga bagian tertentu

new_list = old_list[:3] # copy dari awal (index 0) hingga 2

print("new list : ", new_list)

# copy mulai bagian tertentu

new_list = old_list[2:] # copy mulai dari index 2 hingga akhir index

print("new list : ", new_list)

# copy bagian tertentu hingga beberapa index akhir

new_list = old_list[2:-1] # copy nilai dari index 2 hingga 1 index dari index akhir (index akhir = 3, 3-1 = 2)

print("new list : ", new_list)

new_list = old_list[-3:-1] # copy nilai dari 3 index dari akhir index hingga 1 index dari index akhir 

print("new list : ", new_list)
