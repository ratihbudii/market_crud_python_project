# Create price list
price_apple = 10000
price_orange = 15000
price_grape = 20000

# Create user input 
amount_apple = input("Masukkan jumlah apel: ")
amount_orange = input("Masukkan jumlah jeruk: ")
amount_grape = input("Masukkan jumlah anggur: ")

# Convert user input to integer
amount_apple = int(amount_apple)
amount_orange = int(amount_orange)
amount_grape = int(amount_grape)

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
if yangDibayar < total_beli:
    selisih_kurang_bayar = total_beli - yangDibayar
    print("Transaksi anda dibatalkan")
    print(f"Uang kurang sebesar {selisih_kurang_bayar}")
elif yangDibayar == total_beli:
    print("Terima kasih")
else:
    lebih_bayar = yangDibayar - total_beli
    print(f"Uang kembalian Anda sebesar {lebih_bayar}")
    print("Terima kasih")