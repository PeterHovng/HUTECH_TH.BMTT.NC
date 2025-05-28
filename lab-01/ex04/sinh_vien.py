class SinhVien:
    def __init__(self, id, name,sex, major, diemTB):
        self.id = id
        self.name = name
        self.sex = sex
        self.major = major
        self.diemTB = diemTB
        self.hocLuc = ""
    def __str__(self):
        return "{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format(self.id, self.name, self.sex, self.major, self.diemTB, self.hocLuc)