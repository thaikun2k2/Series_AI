"[] là list, () là set, {} là tuple"
y = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
w = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(y)
print("kiểu dữ liệu của list",type(y))
print(id(y))

x = ["a",1,2,3,4,5,y,w]
print(x)
print("kiểu dữ liệu của list",type(x))
print(id(x))
"list trong list"
print("-----------------")
a = x[0]
print("lấy phần tử 1 của chuỗi x là",a)

b = x[7]
print("lấy phần tử 8 của chuỗi x là",b)

c = x[7][4]
print("lấy phần tử 5 trong danh sách con số 8 trg danh sách x là", c)

"lấy từ phần tử số 1 đến trc phần tử số 3"
d = x[1:3]
print(d)
print(type(d))
print("\n")

"lấy từ phần tử số 1 đến hết"
e = x[1:]
print(e)
print("\n")

"lấy 3 phần tử đầu"
g = x[:3]
print(g)
print("\n")

"lấy toàn bộ list"
f = x[:]
print(f)
print("\n")

h = y + w
print(h)
print("\n")

i = y * 2
print(i)
print("\n")

print("-----------------")

z = len(x)
print("độ dài của list x là",z,"phần tử")
print("\n")

'-------------------------------------'
"cùng kiểu dữ liệu new dùng đc min,max"
'-------------------------------------'

a = min(y)
b = max(y)
print(a)
print(b)
print("/////////////////////////////////////////////////////")
"toán tử in kiểm tra phần tử có tồn tại trong danh sách hay không? true,false"
k = 2 in x
r = "q" in y
print(k)
print(r)
j = z in y
print(j)
print("\n")

"duyệt danh sách dùng for"
for i in x:
    print(i)
    print(id(i))
print("\n")

"delete phần tử 2 cách"
print(x)
print(id(x))
"cách 1"
"ko thay đổi vị trí nhớ, ko thay đổi ô nhớ"
del x[0]
print(x)
print(id(x))

"cách 2"
"xóa vị trí ban đầu lúc chưa delete"
x.remove(2)
print(x)
print(id(x))


if 30 <len(x):
    x.remove(30)
    print(x)
else:
    print("lỗi")

print("\n")
print(id(x))
"update phần tử i: x[i] = new value"
x[0] = "zzzz"
print(x)
print(id(x))
print("\n")

"thêm phần tử hay giá trị vào cuối danh sách x.append(value)"
x.append("xxx")
print(x)
print(id(x))
print("\n")
"mở rộng thêm phần tử của list khác x.extend()"

print(id(x))

x.extend([1, 2, 3])
print(x)
x.extend(y)
print(x)
print(id(x))

"lưu vào vùng ô nhớ khác nên id khác nhau"
"ko thực hiện đc vs set() và tuper{}"
x = x + y
print(x)
print(id(x))

print("\n")


