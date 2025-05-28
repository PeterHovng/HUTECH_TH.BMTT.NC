def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 
#Nhập vào 1 số kiểm tra số nguyên tố và in ra kết quả
n = int(input("Nhập 1 số: "))
if kiem_tra_so_nguyen_to(n):
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")