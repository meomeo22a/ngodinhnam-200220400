import math

# 1. Viet ham tinh tong 2 so truyen vao
def tinh_tong_hai_so(a, b):
    return a + b

# 2. Viet ham tinh tong cac so truyen vao
def tinh_tong_nhieu_so(*args):
    return sum(args)

# 3. Viet ham kiem tra mot so nguyen to
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Viet chuong trinh tim cac so nguyen to trong khoan [a, b]
def liet_ke_so_nguyen_to(a, b):
    ket_qua = []
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            ket_qua.append(i)
    return ket_qua

# 5. Viet ham kiem tra so hoan hao
def la_so_hoan_hao(n):
    if n < 1:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# 6. Viet chuong trinh tim cac so hoan hao trong khoan [a, b]
def liet_ke_so_hoan_hao(a, b):
    ket_qua = []
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            ket_qua.append(i)
    return ket_qua

# => Viet chuong trinh menu chon thuc thi cac ham o tren
def hien_thi_menu():
    while True:
        print("\n--- CHUONG TRINH LUYEN TAP ---")
        print("1. Tinh tong 2 so")
        print("2. Tinh tong nhieu so (cach nhau boi dau cach)")
        print("3. Kiem tra so nguyen to")
        print("4. Liet ke so nguyen to trong khoang [a, b]")
        print("5. Kiem tra so hoan hao")
        print("6. Liet ke so hoan hao trong khoang [a, b]")
        print("0. Thoat")
        
        luon_chon = input("Moi ban chon chuc nang (0-6): ")

        if luon_chon == '1':
            x = float(input("Nhap so thu nhat: "))
            y = float(input("Nhap so thu hai: "))
            print(f"Tong la: {tinh_tong_hai_so(x, y)}")

        elif luon_chon == '2':
            day_so = input("Nhap cac so cach nhau boi dau cach: ").split()
            day_so = [float(i) for i in day_so]
            print(f"Tong day so la: {tinh_tong_nhieu_so(*day_so)}")

        elif luon_chon == '3':
            n = int(input("Nhap so can kiem tra: "))
            if la_so_nguyen_to(n):
                print(f"{n} la so nguyen to.")
            else:
                print(f"{n} khong phai la so nguyen to.")

        elif luon_chon == '4':
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print(f"Cac so nguyen to trong [{a}, {b}] la: {liet_ke_so_nguyen_to(a, b)}")

        elif luon_chon == '5':
            n = int(input("Nhap so can kiem tra: "))
            if la_so_hoan_hao(n):
                print(f"{n} la so hoan hao.")
            else:
                print(f"{n} khong phai la so hoan hao.")

        elif luon_chon == '6':
            a = int(input("Nhap a: "))
            b = int(input("Nhap b: "))
            print(f"Cac so hoan hao trong [{a}, {b}] la: {liet_ke_so_hoan_hao(a, b)}")

        elif luon_chon == '0':
            print("Tam biet!")
            break
        else:
            print("Lua chon khong hop le, vui long chon lai.")

if __name__ == "__main__":
    hien_thi_menu()