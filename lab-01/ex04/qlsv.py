from sinh_vien import SinhVien

class QuanLySinhVien:
    listSV = []
    def generateID(self):
        maxID = 1
        if(self.soLuongSinhVien() > 0):
            maxID = self.listSV[-1].id + 1
        return maxID
    def soLuongSinhVien(self):
        return len(self.listSV)
    def XepLoaiHocLuc(self,sv:SinhVien):
        if(sv.diemTB >= 8):
            sv.hocLuc = "Gioi"
        elif(sv.diemTB >= 6.5):
            sv.hocLuc = "Kha"
        elif(sv.diemTB >= 5):
            sv.hocLuc = "Trung Binh"
        else:
            sv.hocLuc = "Yeu"
    def themSinhVien(self):
        id = self.generateID()
        name = input("Nhập tên sinh viên:")
        sex = input("Nhập giới tính sinh viên:")
        major = input("Nhập chuyên ngành:")
        diemTB = float(input("Nhập điểm trung bình:"))
        sv = SinhVien(id,name,sex,major,diemTB)
        self.XepLoaiHocLuc(sv)
        self.listSV.append(sv)  


    def xoaSinhVien(self,ID):
        for i in range(self.soLuongSinhVien()):
            if(self.listSV[i].id == ID):
                self.listSV.pop(i)
                return True
        return False
    

    def timSinhVienByName(self,name):
        for i in range(self.soLuongSinhVien()):
            if(self.listSV[i].name == name):
                return self.listSV[i]
        return None
                

    def timSinhVienByID(self,ID):
        for i in range(self.soLuongSinhVien()):
            if(self.listSV[i].id == ID):
                return self.listSV[i]
        return None
    

    def updateSinhVien(self,ID):
        SvID:SinhVien = self.timSinhVienByID(ID)
        if(SvID != None):
            name = input("Nhập tên sinh viên:")
            sex = input("Nhập giới tính sinh viên:")
            major = input("Nhập chuyên ngành:")
            diemTB = float(input("Nhập điểm trung bình:"))
            SvID.name = name
            SvID.sex = sex
            SvID.major = major
            SvID.diemTB = diemTB
            self.XepLoaiHocLuc(SvID)
        else:
            print("Không tìm thấy sinh viên")
            return
    def sortByID(self):
        self.listSV.sort(key=lambda x: x.id, reverse=False)
    def sortByMajor(self):
        self.listSV.sort(key=lambda x: x.major, reverse=False)
    def sortByDiemTB(self):
        self.listSV.sort(key=lambda x: x.diemTB, reverse=False)
    def ShowSinhVien(self,ListSV):
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format("ID","Tên","Giới Tính","Chuyên Ngành","Điểm TB","Học Lực"))
        if(len(ListSV) > 0):
            for sv in ListSV:
                print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format(sv.id,sv.name,sv.sex,sv.major,sv.diemTB,sv.hocLuc))
        print("\n")
    def getListSv(self):
        return self.listSV