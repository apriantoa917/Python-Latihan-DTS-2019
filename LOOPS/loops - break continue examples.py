#3.1.2.7 Loop control in Python | break and continue

# break : keluar dari kondisi loops dan menjalankan sintaks setelah looping

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue : keluar dari kondisi loop saat ini dan melanjutkan looping (melompati loop)

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")