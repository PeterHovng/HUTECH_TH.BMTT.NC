import math
# Hàm dịch vòng trái (left rotate) cho 1 giá trị 32-bit
def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

# Bảng hằng số K dùng trong MD5 (64 phần tử)
K = [int((2**32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]

# Bảng số lượng dịch trái (shift amounts)
s = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

# Hàm băm MD5 chính
def md5(message):
    # Khởi tạo các giá trị ban đầu (IV)
    a0 = 0x67452301
    b0 = 0xefcdab89
    c0 = 0x98badcfe
    d0 = 0x10325476

    # Tiền xử lý chuỗi (Padding)
    original_length = len(message) * 8  # Tính độ dài bit
    message += b'\x80'
    while (len(message) % 64) != 56:
        message += b'\x00'
    message += original_length.to_bytes(8, byteorder='little')  # Thêm độ dài (little endian)

    # Xử lý các khối 512-bit (64 byte)
    for offset in range(0, len(message), 64):
        block = message[offset:offset + 64]
        M = [int.from_bytes(block[i:i + 4], byteorder='little') for i in range(0, 64, 4)]

        A, B, C, D = a0, b0, c0, d0  # Sao chép giá trị ban đầu

        # Vòng lặp chính (64 bước)
        for i in range(64):
            if i < 16:
                F = (B & C) | (~B & D)
                g = i
            elif i < 32:
                F = (D & B) | (~D & C)
                g = (5 * i + 1) % 16
            elif i < 48:
                F = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                F = C ^ (B | ~D)
                g = (7 * i) % 16

            temp = (A + F + K[i] + M[g]) & 0xFFFFFFFF
            A, D, C, B = D, C, B, (B + left_rotate(temp, s[i])) & 0xFFFFFFFF

        # Cộng dồn vào kết quả
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF

    # Trả về kết quả dạng hex (little endian)
    digest = sum(x << (32 * i) for i, x in enumerate([a0, b0, c0, d0]))
    return ''.join(f'{digest >> (8 * i) & 0xFF:02x}' for i in range(16))

# ======= Chạy thử =========
input_string = input("Nhập chuỗi cần băm: ")
md5_hash = md5(input_string.encode('utf-8'))

print("Mã băm MD5 của chuỗi '{}' là: {}".format(input_string, md5_hash))
