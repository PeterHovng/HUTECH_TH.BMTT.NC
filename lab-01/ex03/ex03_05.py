def dem_so_lan_xuat_hien(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
#Nhập danh sách từ user
lst = input("Nhập danh sách các từ (cách nhau bằng dấu ,):").split(",")
print("Số lần xuất hiện của các phần tử: ",dem_so_lan_xuat_hien(lst))
         