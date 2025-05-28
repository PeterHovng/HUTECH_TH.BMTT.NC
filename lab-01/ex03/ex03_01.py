def tinh_tong_so_chan(lst):
    # Viết code tính tổng các số chẵn từ 1 đến n
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum
#Nhập danh sách số từ người dùng 
lst = input("Nhập danh sách số (phân tách bởi dấu ,):")
number = list(map(int, lst.split(',')))
#Tính tổng các số chẵn từ 1 đến n và in ra kết quả
tong_chan = tinh_tong_so_chan(number)
print("Tổng các số chẵn trong danh sách là: ", tong_chan)
