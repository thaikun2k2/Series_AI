#######################################################################################################


###List là dùng []
###Tuple là dùng ()

# ls = ["a", 5, 4, 8]
# tp = ("a", 5, 4, 8, 5, 1, 4)
# tp1 = ("b", 6, 7, 9)
# strr = "abcde"


# print(ls)
# print(type(ls))

# print(tp)
# print(type(tp))
# print(id(tp))
# print("\n")

# x = tp[0]
# print(x)
# print(type(x))
# print("\n")
# print(id(x))

# x1 = tp + tp1
# print(x1)
# print(type(x1))
# print(id(x1))

# x2 = tp*3
# print(x2)
# print(type(x2))
# print(id(x2))

# z = tp[0:2]
# print(z)
# print(type(z))
# print("\n")

# x = 5 in tp
# print(x)

# for i in tp:
#     print(i)


##########Sự =! : immutable and mutable 
###immutable: không thể thay đổi được giá trị của nó sau khi đã được tạo ra eg như kiểu tuple()
###mutable: có thể thay đổi được giá trị của nó sau khi đã được tạo ra eg như kiểu list[]

####->> list thay đổi, còn tuple cố định : giá trị, thứ tự, kích thước (cùng ô nhớ (id) )
### tuple ko thể dùng remove, append, insert, pop, clear,... như list
### tuple có thể dùng count, index, len,... như list

# g = tuple(strr)
# print(g)

# e = tuple(tp)
# print(e)

# print(len(tp))
# print(tp.count(5)) ## số lần xuất hiện của 5 trong tp

# print(tp.index(4))## vị trí của 4 trong tp
# print(tp.index(5, 1, 6)) ## tìm vị trí của 5 trong tp từ vị trí 1 đến vị trí 6
# print("\n")
# #list, str, tuple cho phép trùng lặp
# i = 0
# x = 3
# y = 6

# if i in tp[x:y]:
#     x = tp.index(i, x, y) ###kiểm tra ko thấy sẽ báo lỗi, nên cần có vòng if để ktra
#     print(x)
# else:
#     print(f'ko có {i} trong tp từ vị trí {x} đến vị trí {y}')


# ###lưu ý: khi khai báo tuple có 1 phần tử thì phải có dấu phẩy sau phần tử đó để phân biệt với kiểu dữ liệu khác
# tp2 = (5,)
# print(tp2)
# print(type(tp2))

# tp3 = (5)
# print(tp3)
# print(type(tp3))


#######################################################################################################

x = [2, 4, "a"]
y = [2, 4, "a"]
print(x == y) ## so sánh giá trị của x và y
print(x is y) ## so sánh địa chỉ hay còn gọi là có trùng nhau hay ko của x và y, != ở ô nhớ 



## x is y  <=> id(x) == id(y) and x == y
### các kiểu dữ liệu mutable như list, dict, set, byteaarray,...
### các kiểu dữ liệu immutable như int, float, str, tuple,... 
### ở tuple a và b đều chỉ lưu ở cùng 1 ô nhớ nên a is b sẽ trả về True


a = (2, 4, "a")
b = (2, 4, "a")
print(a == b) ## so sánh giá trị của a và b
print(a is b) ## so sánh địa chỉ hay còn gọi là có trùng nhau
print(id(a))
print(id(b))


# 2 phần tử ở 2 danh sách co kiểu khác nhau là mutable thì sẽ không cùng 1 ô nhớ nữa!

c = (2, 4, [1, 3])
d = (2, 4, [1, 3])
print(c == d) ## so sánh giá trị của c và d
print(c is d) ## so sánh địa chỉ hay còn gọi là có trùng nhau
print(id(c))
print(id(d))





