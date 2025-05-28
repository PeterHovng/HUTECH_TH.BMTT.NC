# Nhập thông tin người dùng
print("Nhập thông tin người dùng (Nhập 'done' để kết thúc):")
line =  []
while True:
    user_input = input()
    if user_input.lower() == 'done':
        break
    line.append(user_input)
    #Chuyển các dòng thành chữ in hoa và in ra màn hình
for i in line:
    print(i.upper())