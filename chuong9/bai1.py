class HocVien:
    # a) Khởi tạo class với các thuộc tính
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        info = (
            f"--- Thông tin học viên ---\n"
            f"Họ tên: {self.ho_ten}\n"
            f"Ngày sinh: {self.ngay_sinh}\n"
            f"Email: {self.email}\n"
            f"Điện thoại: {self.dien_thoai}\n"
            f"Địa chỉ: {self.dia_chi}\n"
            f"Lớp: {self.lop}\n"
            f"--------------------------"
        )
        return info

    # c) Phương thức change_info với tham số mặc định
    def change_info(self, dia_chi='Hà Nội', lop='IT12.x'):
        self.dia_chi = dia_chi
        self.lop = lop
        print(f"!! Đã cập nhật địa chỉ thành: {dia_chi} và lớp thành: {lop}")

# d) Chương trình chính
if __name__ == "__main__":
    # Tạo đối tượng học viên mới
    hv1 = HocVien(
        ho_ten="Ngô Đình Nam", 
        ngay_sinh="0/12/2004", 
        email="ngodinhnam2110@gmail.com", 
        dien_thoai="0987654***", 
        dia_chi="Hà nội", 
        lop="IT11.A"
    )

    # Gọi phương thức show_info ban đầu
    print("Dữ liệu ban đầu:")
    print(hv1.show_info())

    # Gọi phương thức change_info (sử dụng giá trị mặc định)
    hv1.change_info()

    # Hiển thị lại thông tin sau khi cập nhật
    print("\nDữ liệu sau khi cập nhật:")
    print(hv1.show_info())
    