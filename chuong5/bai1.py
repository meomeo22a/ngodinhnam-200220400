def doc_n_dong(ten_file, n):
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            print(f"--- {n} dòng đầu tiên của file ---")
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                print(line.strip())
    except FileNotFoundError:
        print("Không tìm thấy file!")

# Nhập n từ bàn phím
n = int(input("Nhập số dòng n cần đọc: "))
doc_n_dong('test.txt', n) 