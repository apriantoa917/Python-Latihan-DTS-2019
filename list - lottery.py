# 3.1.6.8 Lists - more details

# menghitung jumlah menang

drawn = [5, 11, 9, 42, 3, 49] # nomor yang anda miliki

bets = [3, 7, 11, 42, 34, 49] # nomor yang menang

hits = 0  # jumlah menang

for number in bets :
    if number in drawn :
        hits += 1

print(hits)