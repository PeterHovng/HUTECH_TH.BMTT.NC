import re

# Chuỗi đầu vào
s = "-100#^sdfkj8902w3ir021@swf-20"

# Tìm tất cả số nguyên (dương và âm)
numbers = [int(num) for num in re.findall(r'-?\d+', s)]

# Tính tổng số dương và âm
positive_sum = sum(num for num in numbers if num > 0)
negative_sum = sum(num for num in numbers if num < 0)

# In kết quả
print(f"Giá trị dương: {positive_sum}")
print(f"Giá trị âm: {negative_sum}")