# 2.3 giai pt ax+b=0
a = int(input('nhap a '))
b = int(input('nhap b '))
x = -b / a
print('kq pt ax+b=0 -> x= ', x)

# 2.4 giai pt ax2+b+c=0 vs a khac 0
from math import sqrt

while True:
    a = int(input("nhap a, a#0: "))
    if a != 0:
        break
b = int(input('nhap b '))
c = int(input('nhap c '))
delta = b * b - 4 * a * c
if delta < 0:
    print('pt vo nghiem ')
elif delta == 0:
    x1 = -b / 2 * a
    print('pt co nghiem kep x1=x2=-b/2*a ', x1)
elif delta > 0:
    x1 = (-b + sqrt(delta)) / 2 * a
    print('pt co 2 nghiem pb ')
    print('nghiem x1=x2=', x1)

# bai 2.5
from datetime import datetime

luongCB = int(input('nhap luong co ban '))
namCT = int(input(' nhap so nam cong tac '))
if namCT < 5:
    print('luong thang cua ban la : ', luongCB)
else:
    phucapTN = luongCB * (namCT / 100)
    print('luong thang cua ban la: ', luongCB + phucapTN)

# bai 2.6
from datetime import datetime

namHT = datetime.now().year
while True:
    namSinh = int(input(' nhap nam sinh cua ban (nam sinh phai < nam hien tai) '))
    if namSinh < namHT:
        break
print('tuoi ban la ', namHT - namSinh)

# 2.7 Giá cước taxi được tính theo công thức: 1km đầu tiên tính
# từ lúc lên xe: 13000 đồng. Mỗi km tiếp theo được tính theo đơn giá
# là 12000 đồng. Từ km 30 trở lên, mỗi km được tính là 9000 đồng. --> tinh tien

while True:
    soKM = int(input("nhap so km di dc "))
    if soKM >0:
        break
if soKM>0 and soKM <= 1:
    print('ban het 13k vnd ')
elif soKM>1 and soKM<30:
    print('ban di het ',13000+(soKM-1)*12000)
else:
    print('ban di het ', 13000 + 29*12000 + (soKM-30)*9000)


# 2.8 nhap tien luong cua 1 h tinh tien luong (vuot 40h , moi gio hon x1.5)

while True:
    luong1h=int(input(' nhap tien luong tra cho 1h '))
    if luong1h >0:
        break
while True:
    gioLam=int(input('nhap tong so gio lam ' ))
    if gioLam >0:
        break
if  gioLam<=40:
    print('luong tuan nay la',luong1h*gioLam)
elif gioLam>40:
    luong150=(gioLam-40)*1.5*luong1h
    print('luong tuan nay la: ',40*luong1h+luong150)
