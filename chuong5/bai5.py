# Đếm số lượng từ trong file
noi_dung_mau = "Dem so luong tu xuat hien abc abc abc 12 12 it it eaut"
with open('demo_file2.txt', 'w', encoding='utf-8') as f:
    f.write(noi_dung_mau)

def dem_tu_trong_file(ten_file):
    dem_dict = {}
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            # doc toàn bộ nội dung file và tách thành các từ
            noi_dung = f.read()
            cac_tu = noi_dung.split()
            
            # Duyệt qua từng từ trong danh sách
            for tu in cac_tu:
                # Nếu từ đã có trong dict, tăng số đếm lên 1
                if tu in dem_dict:
                    dem_dict[tu] += 1
                # Nếu chưa có, khởi tạo giá trị là 1
                else:
                    dem_dict[tu] = 1
        return dem_dict
    except FileNotFoundError:
        return "File không tồn tại!"

# Thực thi và in kết quả
ket_qua = dem_tu_trong_file('demo_file2.txt')
print(f"Kết quả trả về: {ket_qua}")