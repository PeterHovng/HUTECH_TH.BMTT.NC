def xoa_phan_tu(dic,key):
    if key in dic:
        del dic[key]
        return True
    else:
        return False
# Test
dic = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print("Dic ban đầu là: ",dic)
if(xoa_phan_tu(dic,key)):
    print("Phần tử ",key," đã được xoá khỏi Dic. Dic sau khi xoá là ",dic)
else:
    print("Phần tử ",key," không có trong Dic")