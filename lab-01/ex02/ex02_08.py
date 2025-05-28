#Hàm kiểm tra số nhị phân có chia hết cho 5 không
def chia_het_cho_5(so_nhi_phan):
    # Chuyển số nhị phân sang thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    # Kiểm tra số thập phân có chia hết cho 5 không
    if so_thap_phan % 5 == 0:
        return True
    else:
        return False
#Nhập chuỗi số nhị phân từ bàn phím phân tách bởi dấu ,
so_nhi_phan = input("Nhập chuỗi số nhị (phân phân tách bởi dấu ,): ").split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan if chia_het_cho_5(so)]
if len(so_chia_het_cho_5) == 0:
    print("Không có số nào chia hết cho 5")
else:
    print("Các số nhị phân chia hết cho 5 là: ", ','.join(so_chia_het_cho_5))