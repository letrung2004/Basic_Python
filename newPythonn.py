# sử dụng if/elif/else, while/else, for/else cho python
# reformat your code in PyCharm ctlr+alt+L
b: int = 15

if b >= 15 and b % 2 == 0:
    print("Hello Trung")
    print(b ** 2)  # b**2 có nghĩa là b mũ 2
elif b % 2 == 0:
    print("Test")
else:
    print("Hello")
    print(b + 10)

# &&=and; ||=or; !=not

# Vong lap WHILE
i = 1
while i <= 10:
    if i == 10:
        break
    print("%d x 2=%d" % (i, i * 2))
    i = i + 1
else:  # else của vòng lập while được thực thi khi điều kiện chạy hết ElSE giúp LTV phát hiện được vòng lập bị ngắt giữa chừng
    print("test while else")

# Vong lap FOR
for i in range(1, 10, 2):  # for(int i=0;i < 10;i+=2) chạy từ 1 đến nhỏ hơn 10 chứ không bằng 10 và cách nhau 2 đơn vị
    print("%d x 3= %d" % (i, i * 3))
else:
    print("test for else")  # tương tự else của while





# try/except trong python
print("GIAI VA BIEN LUAN PHUONG TRINH BAC 1: ax + b = 0")
while True:
    try:
        a = float(input("Nhap a= "))
        b = float(input("Nhap b= "))
    except:
        print("CO LOI ROI NHAP LAI")
    else:
        print("ELSE")
        if a == 0:
            if b == 0:
                print("PT VO SO NGHIEM")
            else:
                print("PT VO NGHIEM")
        else:
            x = -b / a
            print("NGHIEM: x=%f" % (x))
        break
    finally:
        print("DONE")
