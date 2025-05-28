def dao_nguoc_list(lst):
    return lst[::-1]
#Nhập danh sách số từ người dùng
lst = input("Nhập danh sách số (phân tách bởi dấu ,):")
number = list(map(int, lst.split(',')))
#Đảo ngược danh sách số và in ra kết quả
reverse_lst = dao_nguoc_list(number)
print("Danh sách sau khi đảo ngược là: ", reverse_lst)
