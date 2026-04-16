import sys
import sqlite3
from PyQt6 import QtWidgets
# Import class giao diện từ file ui_quanlynhansu.py bạn vừa tạo
from quanlynhansu import Ui_MainWindow

class QuanLyNhanSuApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        
        self.db_name = 'nhansu_data.db'
        self.tao_bang_neu_chua_co()

        self.btnThem.clicked.connect(self.them_nhan_su)
        self.btnSua.clicked.connect(self.sua_nhan_su)
        self.btnXoa.clicked.connect(self.xoa_nhan_su)
        self.btnTim.clicked.connect(self.tim_kiem)
        
    
        self.tableNhanSu.cellClicked.connect(self.do_du_lieu_len_form)
        
       
        self.load_du_lieu()



    def tao_bang_neu_chua_co(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NhanSu (
                cccd TEXT PRIMARY KEY,
                hoten TEXT NOT NULL,
                ngaysinh TEXT,
                gioitinh TEXT,
                diachi TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def load_du_lieu(self, query="SELECT * FROM NhanSu", params=()):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        
  
        self.tableNhanSu.setRowCount(0)
        
  
        for row_idx, row_data in enumerate(rows):
            self.tableNhanSu.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.tableNhanSu.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    def lay_thong_tin_tu_form(self):
        cccd = self.txtCCCD.text().strip()
        hoten = self.txtHoTen.text().strip()
        ns = self.txtNgaySinh.text().strip()
        gt = self.txtGioiTinh.text().strip()
        dc = self.txtDiaChi.text().strip()
        return cccd, hoten, ns, gt, dc

    def xoa_trang_form(self):
        self.txtCCCD.clear()
        self.txtHoTen.clear()
        self.txtNgaySinh.clear()
        self.txtGioiTinh.clear()
        self.txtDiaChi.clear()
        self.txtCCCD.setFocus() 

    def do_du_lieu_len_form(self, row, column):
        self.txtCCCD.setText(self.tableNhanSu.item(row, 0).text())
        self.txtHoTen.setText(self.tableNhanSu.item(row, 1).text())
        self.txtNgaySinh.setText(self.tableNhanSu.item(row, 2).text())
        self.txtGioiTinh.setText(self.tableNhanSu.item(row, 3).text())
        self.txtDiaChi.setText(self.tableNhanSu.item(row, 4).text())



    def them_nhan_su(self):
        cccd, hoten, ns, gt, dc = self.lay_thong_tin_tu_form()
        if not cccd or not hoten:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập ít nhất CCCD và Họ tên!")
            return

        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO NhanSu VALUES (?, ?, ?, ?, ?)", (cccd, hoten, ns, gt, dc))
            conn.commit()
            conn.close()
            
            self.load_du_lieu()
            self.xoa_trang_form()
            QtWidgets.QMessageBox.information(self, "Thành công", "Đã thêm nhân sự thành công!")
        except sqlite3.IntegrityError:
            QtWidgets.QMessageBox.critical(self, "Lỗi", "Số CCCD này đã tồn tại trong hệ thống!")

    def sua_nhan_su(self):
        cccd, hoten, ns, gt, dc = self.lay_thong_tin_tu_form()
        if not cccd:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn hoặc nhập CCCD cần sửa!")
            return
            
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE NhanSu SET hoten=?, ngaysinh=?, gioitinh=?, diachi=? WHERE cccd=?", 
                       (hoten, ns, gt, dc, cccd))
        conn.commit()
        
        if cursor.rowcount == 0:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Không tìm thấy CCCD này để sửa!")
        else:
            self.load_du_lieu()
            self.xoa_trang_form()
            QtWidgets.QMessageBox.information(self, "Thành công", "Cập nhật thông tin thành công!")
        conn.close()

    def xoa_nhan_su(self):
        cccd = self.txtCCCD.text().strip()
        if not cccd:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng chọn nhân sự cần xóa!")
            return

        # Xác nhận trước khi xóa
        reply = QtWidgets.QMessageBox.question(self, 'Xác nhận', 
                                               f'Bạn có chắc chắn muốn xóa nhân sự có CCCD {cccd} không?',
                                               QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No, 
                                               QtWidgets.QMessageBox.StandardButton.No)
        if reply == QtWidgets.QMessageBox.StandardButton.Yes:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("DELETE FROM NhanSu WHERE cccd=?", (cccd,))
            conn.commit()
            conn.close()
            
            self.load_du_lieu()
            self.xoa_trang_form()
            QtWidgets.QMessageBox.information(self, "Thành công", "Đã xóa nhân sự!")

    def tim_kiem(self):
       
        tu_khoa, ok = QtWidgets.QInputDialog.getText(self, "Tìm kiếm", "Nhập CCCD, Tên hoặc Địa chỉ cần tìm:")
        
        if ok and tu_khoa:
            query = "SELECT * FROM NhanSu WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?"
            param = f"%{tu_khoa}%"
            self.load_du_lieu(query, (param, param, param))
        elif ok and not tu_khoa: 
            self.load_du_lieu()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QuanLyNhanSuApp()
    window.show()
    sys.exit(app.exec())