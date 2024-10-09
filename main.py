# Create price list
price_apple = 10000
price_orange = 15000
price_grape = 20000

# Stock Feature
stock_apple = 30
stock_orange = 40
stock_grape = 50

# Tampilan daftar buah 
list_fruit = {"Fruit name" : ["apple" , "orange", "grape"],
            "Stock" : [stock_apple , stock_orange, stock_grape],
            "Price" : [price_apple , price_grape, price_orange] }

# Cart
list_cart_fruit = {"Fruit name" : ["apple", "grape"],
                 "Qty" : [1, 2],
                 "Price" : [10000, 40000]}

# Menu Feature
def get_menu_choice():
    def print_menu ():
        print(30 * "-", "Menu Pasar Buah", 30 * "-" )
        print("1. Menampilkan daftar buah")
        print("2. Menambah buah")
        print("3. Menghapus buah")
        print("4. Membeli buah")
        print("5. Exit program")
        print(73 * "-")
    def print_list_fruit():
        print(f"Index\t | Name\t\t | Stock\t | Price\t ")
        index = 0
        for fruit in list_fruit["Fruit name"]:
            print(f"{index}\t | {list_fruit.get("Fruit name")[index]}\t | {list_fruit.get("Stock")[index]}\t\t | {list_fruit.get("Price")[index]}\t ")
            index += 1
    def add_new_fruit():
        new_fruit_name = input("Masukkan nama buah baru: ")
        new_fruit_stock = int(input("Masukkan stok buah baru: "))
        new_fruit_price = int(input("Masukkan harga buah baru: "))
        list_fruit["Fruit name"].append(new_fruit_name)
        list_fruit["Stock"].append(new_fruit_stock)
        list_fruit["Price"].append(new_fruit_price)
        print(list_fruit)
    def delete_fruit():
        delete_index = int(input("Masukkan index buah yang ingin dihapus: "))
        list_fruit["Fruit name"].pop(delete_index)
    def buy_fruit():
        buy_index = int(input("Masukkan index buah yang ingin dibeli: "))
        while buy_index < 0 and buy_index >= len(list_fruit["Fruit name"]):
            print("User wajib input ulang")
            buy_index = int(input("Masukkan index buah yang ingin dibeli: "))
        # jika user input selain index yang terdaftar, maka user input ulang
        # Input index yang dipilih

        # Input jumlah yang dibeli
        amount_fruit = int(input("Masukkan jumlah buah: "))
        while amount_fruit > list_fruit["Stock"][buy_index]: 
            print("Jumlah yang dimasukkan terlalu banyak")
            print(f"Stok tidak cukup, stok buah {list_fruit["Fruit name"][buy_index]} sekarang: {list_fruit['Stock'][buy_index]}")
            amount_fruit = int(input("Masukkan jumlah buah: "))
        
        list_cart_fruit["Fruit name"].append(list_fruit["Fruit name"][buy_index])
        list_cart_fruit["Qty"].append(amount_fruit)
        list_cart_fruit["Price"].append(list_fruit["Price"][buy_index])
        cart_fruit()
        buy_confirmation = input("Mau beli buah yang lain? (ya atau tidak): ")
        while buy_confirmation != "ya" and buy_confirmation != "tidak":
            print("Input salah. Masukkan kembali")
            buy_confirmation = input("Mau beli buah yang lain? (ya atau tidak): ")
        if buy_confirmation == "ya":
            buy_fruit()
        elif buy_confirmation == "tidak":
            cart_fruit()
            total_beli = 0
            for index in range (len(list_cart_fruit["Qty"])):
                total_beli = total_beli + (list_cart_fruit["Qty"][index] * list_cart_fruit["Price"][index])
            print(f"Total yang harus dibayar: {total_beli}")
            yangDibayar = int(input("Masukkan jumlah uang: "))
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
        else:
            print("Pilihan salah")

            # tampilin harga buah yang dipilih * kuantitas
            # tampilin total harga yg harus dibayar
            # tampilin jumlah uang yg dibayar
            # tampilin uang kembalian
            # terimakasih
    def cart_fruit():
        print("Cart Fruit: ")
        print(f"Name\t | Qty\t | Price\t ")
        index = 0
        for fruit in list_cart_fruit["Fruit name"]:
            print(f"{list_cart_fruit.get("Fruit name")[index]}\t | {list_cart_fruit.get("Qty")[index]}\t | {list_cart_fruit.get("Price")[index]}\t ")
            index += 1
        
        # Kalau stok ga cukup, maka print stok jeruk skrng
        # print isi cart
        # Konfirmasi sblm checkout
        # Jika tambah buah lain, maka ulangi dari atas
        # Jika checkout, maka tampilkan daftar belanja dan total harga
        # Tampilkan total yang dibayar
        # Masukkan jumlah uang
        # Jika yang dibayar kurang dari total belanja, maka masukkan jumlah uang lagi
        # Uang kembalian
        # Terimakasih
    
    loop = True
    int_choice = -1 

    while loop:
        print_menu()
        choice  = input("Silakan pilih menu: ")

        if choice == "1":
            print_list_fruit()
            int_choice = 1
            loop = True
        elif choice == "2":
            add_new_fruit()
            print_list_fruit()
            int_choice = 2
            loop = True
        elif choice == "3":
            print_list_fruit()
            delete_fruit()
            print_list_fruit()
            int_choice = 3
            loop = True
        elif choice == "4": 
            print_list_fruit()
            buy_fruit() 
            int_choice = 4
            loop = False
        elif choice == "5":
            print("Terimakasih sudah melihat menu kami")
            int_choice = 5
            loop = False
        else:
            input("Pilihan menu salah. Coba lagi")
    return[int_choice, choice]

get_menu_choice()


