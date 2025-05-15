def average_and_maximum(numbers):
    average = sum(numbers)/len(numbers)
    maximum = max(numbers)
    return average, maximum

def user_input():
    while True:
        numbers = []
        print("Nhap danh sach : ")
        try:
            user_input = input(">>> ")
            numbers = [float(num) for num in user_input.strip().split()]
            if not numbers:
                raise ValueError("Danh sach rong. Vui long nhap dau vao vao danh sach")
            return numbers
        except ValueError as e:
            print(f"Loi: {e}")

def main():
    numbers = user_input()
    average, maximum = average_and_maximum(numbers)
    print("Trung binh cua danh sach la: ",average)
    print("So lon nhat cua danh sach la: ",maximum)

if __name__ == "__main__":
    main()