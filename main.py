# Create price list
price_apple = 10000
price_orange = 15000
price_grape = 20000

# Stock Feature
stock_apple = 30
stock_orange = 40
stock_grape = 50

# While condition
amount_apple = int(input("Masukkan jumlah apel: "))
while amount_apple > stock_apple: # while itu  pasti berjalan sekali dulu sebelum  keluar iterasi
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_apple = int(input("Masukkan jumlah apel: "))
    
amount_orange = int(input("Masukkan jumlah jeruk: "))
while amount_orange > stock_orange: # while itu  pasti berjalan sekali dulu sebelum  keluar iterasi
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_orange = int(input("Masukkan jumlah jeruk: "))

amount_grape = int(input("Masukkan jumlah anggur: "))
while amount_grape > stock_grape: # while itu  pasti berjalan sekali dulu sebelum  keluar iterasi
    print("Jumlah yang dimasukkan terlalu banyak")
    amount_grape = int(input("Masukkan jumlah anggur: "))

# Calculate price
price_apple_total = price_apple * amount_apple
price_orange_total = price_orange * amount_orange
price_grape_total = price_grape * amount_grape

# Show the detail 
print("Detail Belanja")
print(f"Apel: {amount_apple} x {price_apple} = {price_apple_total}")
print(f"Jeruk: {amount_orange} x {price_orange} = {price_orange_total}")
print(f"Anggur: {amount_grape} x {price_grape} = {price_grape_total}")

print("Total belanja: ", price_apple_total+price_orange_total+price_grape_total)

# Create ask amount of money
yangDibayar = int(input("Masukkan jumlah uang: "))

total_beli = price_apple_total + price_orange_total + price_grape_total

# Condiiton 1 2 dan 3

# while yg dibayar > total beli
# selisih kurang bayar = total beli - yang dibayar
# print(f"Uang kurang sebesar {selisih kurang bayar})
# yangDibayar = int(input("Masukkan jumlah uang: "))

while yangDibayar < total_beli:
    selisih_kurang_bayar = total_beli - yangDibayar
    print(f"Uang kurang sebesar {selisih_kurang_bayar}")
    yangDibayar = int(input("Masukkan jumlah uang: "))

if yangDibayar == total_beli:
    print("Terima kasih")
else:
    lebih_bayar = yangDibayar - total_beli
    print(f"Uang kembalian Anda sebesar {lebih_bayar}")
    print("Terima kasih")