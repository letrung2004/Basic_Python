def tong(a, b, c=10):
    print("HAM TINH TONG")
    return a + b + c


t = tong(4, 5, 7)
print(t)

t1 = tong(4, 5)
print(t1)


# luu y DANH SACH MAC DINH phai nam LIEN TIEP tu ben PHAI

# truyền số lương tham só bất kỳ
def sum(a, b, *args):
    print("SUM")
    sum = a + b
    for x in args:
        sum += x
    return sum


t = sum(3, 4, 5, 6, 7, 89)
print(t)


##
def sum1(a, b, *args, **kwargs):
    print("KEYWORDARGS")
    s = a + b
    for x in args:
        s += x
    if kwargs.get("my_number"):
        s += kwargs['my_number']
    return s


t2 = sum1(1, 2, 34, 43, 3, my_number=1234)
print(t2)

# cach su dung LAMDA
print("cach su dung LAMDA")
m = lambda x, y, z: x * y * z
print(m(3, 4, 5))
