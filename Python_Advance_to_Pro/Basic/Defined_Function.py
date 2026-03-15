
# ===============================
# LƯU Ý VỀ HÀM (FUNCTION) TRONG PYTHON
# ===============================

# | Nội dung | Cú pháp / Ví dụ | Ghi chú |
# |----------|-----------------|--------|
# | Khai báo hàm | def ten_ham(): | dùng từ khóa def |
# | Tham số (parameter) | def add(a, b): | a, b là tham số |
# | Gọi hàm | add(2,3) | truyền đối số |
# | Giá trị trả về | return a + b | return kết thúc hàm |
# | Hàm không return | def hello(): print("Hi") | mặc định trả về None |
# | Tham số mặc định | def hello(name="Python"): | dùng khi không truyền |
# | Keyword argument | hello(name="An") | truyền theo tên |
# | Positional argument | hello("An") | truyền theo vị trí |
# | *args | def sum_all(*args): | nhận nhiều đối số dạng tuple |
# | **kwargs | def info(**kwargs): | nhận nhiều key=value dạng dict |
# | Hàm trong hàm | def outer(): | nested function |
# | Lambda function | lambda x: x*2 | hàm 1 dòng |
# | Docstring | """Mô tả hàm""" | dùng để giải thích hàm |
# | Type hint | def add(a:int,b:int)->int | gợi ý kiểu dữ liệu |
# | Scope biến | local / global | phạm vi biến |
# | global keyword | global x | sửa biến global |
# | nonlocal keyword | nonlocal x | sửa biến ngoài hàm con |
# | Hàm là object | f = add | có thể gán cho biến |
# | Hàm làm tham số | map(func, list) | truyền hàm vào hàm |
# | Decorator | @decorator | mở rộng chức năng hàm |


##y = abs(x) trả outcome là y là trị tuyệt đối của x

from math import * ## lấy tất cả thư viện math

# def tri_tuỵet_doi(x):
#     if x >= 0:
#         y = x
#     else:
#         y = -x
#     return y
# def print_vision(z):
#     print(z)
#     return

# x = -5
# y = tri_tuỵet_doi(x)
# print_vision(f'giá trị tuyệt đối của x là: {y}')



# #
# #a = hypot(3,4) a# cạnh huyền của tam giác vuông
# b = 3
# c = 4

# def canh_huyen_tamgiac(b, c):
#     a = sqrt(b*b + c*c)
#     return a

# a = canh_huyen_tamgiac(b, c)
# print(f'cạnh huyền là: {a}')


### tham số truyền: 

##Eg1: truyền theo kiểu giá trị
# def hamxx(v):
#     v=3 # immutable ô nhớ số 1
#     return v
# m = 2 #mutable ô nhớ số 2
# y = hamxx(m)
# print("giá trị hàm xx trả về là:", y)#=3 ko có j thay đổi

# print("giá trị của m là:", m)#2 ko thay đổi

#Eg2:  truyền theo kiểu tham chiếu đến ô nhớ đó
# u = 3
# def hamxx(t):
#     t.append(u) ## thêm giá trị vào ô nhớ mutable
#     return t
# n = [1, 2] # ô nhớ số 1
# l = hamxx(n) #truyền n vào hàm có phương thức append thêm vào ô nhớ trg hàm
# print("giá trị hàm xx trả về là:", l)#giá trị đã thay đổi

# print("giá trị của n là:", n)#giá trị đã thay đổi



#required argument(bắt buộc đúng theo thứ tự tham số truyền vào)

# #required: quan trọng ở thứ tự 
# def ham(v, k):
#     v.append(k)
#     return v

# #y = ham(m, 3)####nếu đổi ngc lại y = ham(3, m) sẽ lỗi vì thứ tự rất quan trọng 
# m = [1, 2, 3, 4]
# k = [6, 7]
# y = ham(m, k)#### đổi ngc lại ko bị lỗi nhưng thứ tự sẽ bị thay đổi
# print("giá trị hàm xx trả về là:", y)#giá trị đã thay đổi

# print("giá trị của n là:", m)#giá trị đã thay đổi

#argument: ko quan tâm đến thứ tự gàn thêm tên argument

# def ham(v, k):
#     v.append(k)
#     return v

# #y = ham(m, 3)####nếu đổi ngc lại y = ham(3, m) sẽ lỗi vì thứ tự rất quan trọng 
# m = [1, 2, 3, 4]
# kk = [6, 7]
# y = ham(k=kk, v = m)#### đổi ngc lại ko bị lỗi nhưng thứ tự sẽ bị thay đổi
# print("giá trị hàm xx trả về là:", y)#giá trị đã thay đổi

# print("giá trị của n là:", m)#giá trị đã thay đổi


##đefault argument: khi gọi hàm nếu ko truyền sẽ lấy giá trị mặc định

# def ham(v, k = 3):#k = 3 là default
#     v.append(k)
#     return v

# #y = ham(m, 3)####nếu đổi ngc lại y = ham(3, m) sẽ lỗi vì thứ tự rất quan trọng 
# m = [1, 2, 3, 4]
# kk = [6, 7]
# y = ham( v = m)#### đổi ngc lại ko bị lỗi nhưng thứ tự sẽ bị thay đổi
# print("giá trị hàm xx trả về là:", y)#giá trị đã thay đổi

# print("giá trị của n là:", m)#giá trị đã thay đổi
