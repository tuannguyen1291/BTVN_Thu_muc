import random
danhsach = []
for i in range(1000):
    danhsach.append(random.randint(-1000, 1000))
def tao_danh_sach_in_phan_tu():
    check = 0
    tenfile = input("Nhập tên file: ")
    f = open(tenfile, 'w')
    for i in danhsach:
        if check < 9:
            chuoikytu = str(i) + ','
            f.write(chuoikytu)
            check = check + 1
        else:
            f.write(str(i) + "\n")
            check = 0
    f.close()
    f = open(tenfile, 'r')
    a = f.readlines()
    for i in a:
     print(i.replace(",", "\t"))
    f.close()
e=tao_danh_sach_in_phan_tu()
