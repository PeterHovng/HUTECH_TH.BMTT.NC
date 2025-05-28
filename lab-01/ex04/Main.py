from qlsv import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("Chương trình quản lý sinh viên")
    print("=====================================")
    print("1. Them sinh vien")
    print("2. Cap nhap thong tin sinh vien boi ID")
    print("3. Xoa sinh vien boi ID")
    print("4. Tim sinh vien boi ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("=====================================")
    choice = input("Nhap lua chon cua ban:")
    if choice == "1":
        qlsv.themSinhVien()
        print("Them sinh vien thanh cong")
    elif choice == "2":
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhap thong tin sinh vien boi ID:")
            id = int(input("Nhap ID sinh vien muon cap nhap:"))
            qlsv.updateSinhVien(id)
        else:
            print("\nDanh sach sinh vien rong")
    elif choice == "3":
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien boi ID:")
            id = int(input("Nhap ID sinh vien muon xoa:"))
            if(qlsv.xoaSinhVien(id)):
                print("Xoa thanh cong sinh vien co ID:",id) 
            else:
                print("Khong tim thay sinh vien co ID:",id)
        else:
            print("\nDanh sach sinh vien rong")
    elif choice == "4":
        if(qlsv.soLuongSinhVien() > 0):
            name = input("Nhap ten sinh vien muon tim:")
            sv = qlsv.timSinhVienByName(name)
            if(sv != None):
                print(sv)
            else:
                print("Khong tim thay sinh vien")
        else:
            print("\nDanh sach sinh vien rong")
    elif choice == "5":
        if(qlsv.soLuongSinhVien() >0):
            print("\n5. Sap xep sinh vien theo diem trung binh:")
            qlsv.sortByDiemTB()
            qlsv.ShowSinhVien(qlsv.getListSv())
        else:
            print("\nDanh sach sinh vien rong")
    elif choice == "6":
        if(qlsv.soLuongSinhVien() >0):
            print("\n6. Sap xep sinh vien theo chuyen nganh:")
            qlsv.sortByMajor()
            qlsv.ShowSinhVien(qlsv.getListSv())
        else:
            print("\nDanh sach sinh vien rong")
    elif choice == "7":
        if(qlsv.soLuongSinhVien() >0):
            print("\n7. Hien thi danh sach sinh vien:")
            qlsv.ShowSinhVien(qlsv.getListSv())
        else:
            print("\nDanh sach sinh vien rong")
    elif choice == "0":
        break
    else:
        print("Lua chon khong hop le")