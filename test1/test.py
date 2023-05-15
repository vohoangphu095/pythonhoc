while True:
    luong1h=int(input(' nhap tien luong tra cho 1h '))
    if luong1h >0:
        break
while True:
    gioLam=int(input('nhap tong so gio lam' ))
    if gioLam >0:
        break
if  gioLam<=40:
    print('luong tuan nay la',luong1h*gioLam)
elif gioLam>40:
    luong150=(gioLam-40)*1.5*luong1h
    print('luong tuan nay la: ',40*luong1h+luong150)