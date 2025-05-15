import json

class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def list_product(self):
        return {
            "name" : self.name,
            "price" : self.price,
            "quantity" : self.quantity
        }

def read_product_from_file(filename):
    products = []
    try:
        with open (filename,"r") as file:
            lines = file.readlines()
            for idx,line in enumerate(lines, 1):
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print(f"Dong {idx} co dinh dang sai: '{line.strip()}' - bo qua")
                    continue
                name, price_str, quantity_str = parts
                try:
                    price = float(price_str)
                    quantity = int(quantity_str)
                    products.append(Product(name.strip(),price,quantity))
                except ValueError:
                    print(f"Gia hoac so luong khong hop le o dong {idx}: '{line.strip()}' ")
    except FileNotFoundError:
        print(f"Khong tim thay file: {filename}")
    except Exception as e:
        print(f"Loi: {e}")
    return products

def display_products(products):
    print("Danh sach san pham: ")
    for product in products:
        print(f"- {product.name}: {product.price} USD (So luong: {product.quantity})")

def save_products_to_json(products,output_filename):
    try:
        data = [product.list_product() for product in products]
        with open (output_filename,"w") as json_file:
            json.dump(data,json_file, indent=4)
        print(f"Du lieu da duoc luu vao: {output_filename}")
    except Exception as e:
        print(f"Loi: {e}")

def main():
    filename = "products.txt"
    output_file = "products.json"

    while True:
        print("Chon cac lua chon sau day: ")
        print("1. Doc va hien thi danh sach san pham")
        print("2. Luu danh sach san pham vao file JSON")
        print("3. Thoat")
        choice = input("Lua chon cua ban la: ")

        if choice == "1":
            products = read_product_from_file(filename)
            if products:
                display_products(products)
            else:
                print("Khong co san pham hop le de hien thi")
        elif choice == "2":
            products = read_product_from_file(filename)
            if products:
                save_products_to_json(products, output_file)
            else:
                print("Khong co san pham hop le de luu")
        elif choice == "3":
            print("Thoat")
            break
        else:
            print("Lua chon khong hop le. Vui long chon lai")

if __name__ == "__main__":
    main()