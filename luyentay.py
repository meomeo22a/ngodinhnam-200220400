class NhanVien:
    'Lớp mô tả cho mọi nhân viên'
    dem = 0

    def __init__(self, name, salary):
        # Sử dụng một dấu gạch dưới _name nếu muốn báo hiệu là biến nội bộ 
        # Hoặc không dùng gạch dưới để truy cập trực tiếp dễ dàng
        self.name = name
        self.salary = salary
        NhanVien.dem += 1

    def hien_thi_so_luong(self):
        print("Tổng số nhân viên được tạo: %d" % NhanVien.dem)

    def hien_thi_nhan_vien(self):
        print("Tên: ", self.name, ", Lương: ", self.salary)

    def cap_nhat(self, name=None, salary=None):
        if name:
            self.name = name
        if salary:
            self.salary = salary

# --- Khởi tạo đối tượng ---
nhan_vien_dev = NhanVien('Nguyen Van A', 1000)
nhan_vien_test = NhanVien('Nguyen Van B', 1200)

# --- Truy cập vào method của Class ---
nhan_vien_dev.hien_thi_nhan_vien()
nhan_vien_test.hien_thi_nhan_vien()

# --- Truy cập vào biến của Class (Số lượng tổng) ---
print(f"Số lượng nhân viên: {nhan_vien_dev.dem}")

# --- Truy cập vào thuộc tính (attribute) của Class ---
# Bây giờ các dòng này sẽ hoạt động vì không còn bị lỗi "Private"
print(f"Tên nhân viên dev: {nhan_vien_dev.name}")
print(f"Tên nhân viên test: {nhan_vien_test.name}")