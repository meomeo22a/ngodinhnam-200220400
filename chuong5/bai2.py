ten_file = "output.txt"
noi_dung = "Chào mừng bạn đến với lập trình Python!\nĐây là dòng thứ hai."

with open(ten_file, 'w', encoding='utf-8') as f:
    f.write(noi_dung)
    print("Đã ghi file thành công.")

with open(ten_file, 'r', encoding='utf-8') as f:
    print("Nội dung file vừa ghi:")
    print(f.read())