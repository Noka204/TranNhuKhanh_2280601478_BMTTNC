so_gio_lam = float(input("Nhập số giờ làm mỗi tuần :"))
luonng_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn :"))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan*luonng_gio + gio_vuot_chuan*luonng_gio*1.5
print(f"Số thực lĩnh của nhân viên : {thuc_linh}")