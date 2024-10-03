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