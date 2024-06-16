import string

s1 = 'STRING IN PYTHON'
s2 = "STRING IN PYTHON TOO"
s3 = '''
    STRING IN PYTHON 
    THIS IS SIMPLE
'''
# print(s1)
# print(s2)
# print(s3)

# LAY CHIEU DAI CUA CHUOI
s = 'Python is simple'
print(len(s))
print(s[3])

# chỉ số dương bắt đầu từ bên trái qua 0,1,2....m
# chỉ số âm bắt đầu từ bên phải qua -1,-2,...-n
print(s[10:16])  # in ra 'simple'
print(s[-2])  # in ra 'l'

# tìm trong s có chữ 'simple' không và in ra chỉ số
print(s.find("simple"))  # in ra 10

# đếm tần số xuất hiện của 'i' trong s (Có thể sử dụng với cả chữ)
print(s.count("i"))  # in ra 2

# thay đổi 'i' thành 'I' trong s (Có thể sử dụng với cả chữ)
s = s.replace("i", "I")
print(s)

# cắt chuỗi tại ví trí yêu cầu thành các mảng
print(s.split(" "))  # kết quả ra ['Python', 'Is', 'sImple']

# in ra màng hình ----------THISCENTER----------
print("THISCENTER".center(30, "-"))

# muốn in ra màng hình *****
print("*" * 5)

# format trong Python
a, b, c = 10, 8, 9
newS = str.format("{} + {} + {}= {}", a, b, c, a + b + c)
print(newS)  # in ra màng hinh '10 + 8 + 9= 27'
newS1 = str.format("{1} + {0} + {2}= {3}", a, b, c, a + b + c)
print(newS1)  # in ra màng hinh '8 + 10 + 9= 27'
print(str.format("{0:.2f}", 6762.232323))  # in ra màng hinh '6762.23'

# muốn in ra màng hình *****
#                      *****
#                      *****
#                      *****
print(("*" * 5 + "\n") * 4)
