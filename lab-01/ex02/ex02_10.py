def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
#Su dung ham dao_nguoc_chuoi
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print(f"Chuỗi sau khi đảo ngược là: {dao_nguoc_chuoi(input_string)}")