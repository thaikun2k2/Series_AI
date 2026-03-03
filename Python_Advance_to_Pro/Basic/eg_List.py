#######Eg 1 nhập 2 số a,b nguyên đương cấch nhau bởi dấu ',' hiển thị số chẵn nằm giữa 2 số trên cách nahu bỉ dấu ','

"""
a = int(input("Nhập vào số nguyên dương a ="))
b = int(input("Nhập vào số nguyên dương b ="))

outcome = []
for i in range(a,b):
    if i%2 == 0:
        outcome.append(str(i))

x = ','
out = x.join(outcome)
print("==>> Các số chắn nằm giữa %s và %s là: " %(a,b), out)

"""
"""

ab = input("Nhập vào 2 số nguyên dương a và b cách nhau bởi dấu ',' là: ")
x = ab.split(',')
a = int(x[0])
b = int(x[1])
print(a)
print(b)

outcome = []
for i in range(a,b):
    if i%2 == 0:
        outcome.append(str(i))

x = ','
out = x.join(outcome)
print("==>> Các số chắn nằm giữa %s và %s là: " %(a,b), out)
"""
"""
a, b = map(int, input("Nhập vào 2 số nguyên dương a và b cách nhau bởi dấu ',' là: ").split(','))
if a>b:
    a,b = b,a

outcome = []
for i in range(a,b + 1):
    if i%2 == 0:
        outcome.append(str(i))

print("==>> Các số chắn nằm giữa %s và %s là: " %(a,b), ','.join(outcome))
"""
"""

### Eg2: Nhập 1 password kiểm tra tính hợp lệ của password đk1: 6 ký tự <= password <= 12 ký tự
#đk2+3+4: có ít nhất 1 chữ thường, chữ hoa, số. có ít nhất 1 ký tự đặc biệt '@','#','$'
x = str(input("Nhập vào mật khẩu cần kiểm tra: "))

out = False
out1 = False
out2 = False
out3 = False
out4 = False

if 6 <= len(x) and len(x) <= 12: # độ dài
    for i in x:
        if i.isupper() == True: # chữ thường
            out1 = True
        if i.islower() == True:# chữ HOA
            out2 = True
        if i.isdecimal() == True: # ký tự số
            out3 = True
        if i == "@" or i == "#" or i == "$" or i == "%": # ký tự đacwj biệt
            out4 = True
    if out1 == True and out2 == True and out3 == True and out4 == True:
            out = True

if out == True:
    print("Mật khẩu kiểm tra HỢP LỆ!!!!")
else:
    print("Mật Khẩu ko hợp lệ vui lòng nhập lại mật khẩu != !!!!")
"""

