# List, Tuple, Set, Dictionnary
# [],   (),    {},   {K:V}

# 1. LIST ->  '[]'  các biến trong mảng phải cùng kiểu dữ liệu
a = [3, 4, 5, 6, 7]

print(len(a))  # số ptu mảng a
print(a[1])  # 4
print(a[1:3])  # [4, 5]  -> lấy từ 1 đến nhỏ hơn 3

a = a + [23, 44]
print(a)  # [3, 4, 5, 6, 7, 23, 44]
print(a * 2)  # [3, 4, 5, 6, 7, 23, 44, 3, 4, 5, 6, 7, 23, 44]

# them ptu vao cuoi mang
a.append(1012)
print(a)  # [3, 4, 5, 6, 7, 23, 44, 1012]

# them ptu vao vtri bat ky
a.insert(2, -1606)
print(a)  # [3, 4, -1606, 5, 6, 7, 23, 44, 1012]

# lay ra ptu X cuoi cung va xoa X khoi mang
x = a.pop()
print(x)  # 1012
print(a)  # [3, 4, -1606, 5, 6, 7, 23, 44]

# lay ra ptu X o vtri bat ky va xoa X khoi mang
y = a.pop(2)
print(y)  # -1606
print(a)  # [3, 4, 5, 6, 7, 23, 44]

# sap xep mang tang dan
a.sort()
print(a)  # [3, 4, 5, 6, 7, 23, 44]

# sap xep mang giam dan
a.sort(reverse=True)
print(a)  # [44, 23, 7, 6, 5, 4, 3]

# tim kiem ptu X va in ra chi so
print(a.index(6))

try:
    a.index(5)
except:
    print("Khong tim thay")
else:
    print(a.index(5))
finally:
    print("DONE")

# xoa ptu biet truoc trong mang
a.remove(44)
print(a)  # [23, 7, 6, 5, 4, 3]

# xoa tai vi tri nao do
del a[0]
print(a)  # [7, 6, 5, 4, 3]

# duyet cac phan tu trong a
print("DUYET DANH SACH CACH 1")
for x in a:
    print(x)
print("DUYET DANH SACH CACH 2")
for i in range(len(a)):
    print(a[i])

# 2.TUPLE  -> '()' tương tự như mảng nhưng KHÔNG ĐƯỢC PHÉP THAY ĐỔI GIÁ TRỊ CÁC PHẦN TỬ TRONG TUPLE
t = (2, 4, 6, 8)
print(t)

# 3.SET (Tập hợp) -> '{}' tương tự như mảng nhưng có ràng buộc là các phần tử không được trùng lập nhau và thứ tự có thể thay đổi bất kỳ
s = {2, 4, 5, 4}
print(s)  # {2, 4, 5} các phần tự trùng nhau sẽ được lược bớt

s1 = "aaaahshhaaaabsbbscca"
print(set(s1))  # {'h', 'a', 'b', 'c', 's'} -> ép kiểu chuổi s1 thành tập hợp và lược bỏ các pt trùng lặp nhau
print("".join(set(s1)))  # bscah -> nối lại thành chuổi đã được lược bỏ các phần tử trùng lập

m = {2, 3, 5, 6}
n = {4, 3, 5, 7}
print(m - n)  # {2, 6} -> thuộc m nhưng không thuộc n
print(m | n)  # {2, 3, 4, 5, 6, 7} -> thuộc cả m và n
print(m & n)  # {3, 5} ->giao của m và n
print(m ^ n)  # {2, 4, 6, 7} -> chỉ in ra pt nào thuộc 1 tập hợp không in pt thuộc cả hai tập hợp

# DICTIONARY (Quan trọng nhất) ->'{key:value}
student = {
    "name": "LE QUOC TRUNG",
    "location": "HCM"
}
print(len(student))
# Them vao
student["gender"] = "NAM"
print(student)  # {'name': 'LE QUOC TRUNG', 'location': 'HCM', 'gender': 'NAM'}

# Xoa
del student["location"]
print(student)  # {'name': 'LE QUOC TRUNG', 'gender': 'NAM'}

print(student.keys())  # dict_keys(['name', 'gender'])
print(student.values())  # dict_values(['LE QUOC TRUNG', 'NAM'])

for k,v in student.items():
    print(k,", ",v)
