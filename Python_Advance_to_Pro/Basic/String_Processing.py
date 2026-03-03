"""
'choise (s) -> trả về 1 ký tự ngẫu nhiên trong s'
from random import choice
s = "abcd efgh ỊKLMN OPQRST UVWXYZ XXXX"
print(id(s))
print(type(s))
print(choice(s))
z = choice(s)
's.center(width, fillchar) căn lề giữa'
z = s.center(20,"*")
print(z)
print("\n")
's.ljust(width, fillchar) left just -> căn lề giữa'
z = s.ljust(30,'#')
print(z)
print("\n")
's.rjust(width, fillchar) right just -> căn lề phải'
z = s.rjust(30,'^')
print(z)
's.lower() -> chuỗi mới và tất cả các kỹ tự đều là chữ thường'
z = s.lower()
print(z)
's.upper() --> tạo chuỗi mới là chữ HOA'
z = s.upper()
print(z)
's.swapcase() -> tạo chuỗi mới, đảo HOA <--> thường'
z = s.swapcase()
print(z)
"s.title() --> tạo chuỗi mới, viết HOA chữ cái đầu mỗi từ"
z = s.title()
print(z)
's.count(s1, k1, k2) Đếm xem trong chuỗi s,'
'từ vị trí k1 đến k2, có bao nhiêu lần xuất hiện chuỗi s1'
'Nếu ko có trả về giá trị 0'
z = s.count('X')
print(z)

"s.find(s1, k1, k2) Tìm xem trg chuỗi s,"
"từ vị trí k1 đến k2"
"Có xuất hiện chuỗi s1 không, nếu không trả về -1"
"Nễu có  thì trả về chỉ vị trí xuất hiện phần tử đó đầu tiên"
m = s.find('X')
print(m)

"s.index(s1, k1, k2) giống s.find(), khác: nếu không tìm thấy báo lỗi"
m = s.index('X')
print(m)
"Tìm từ phải qua trái có hàm sau:"
"s.rfind(s1,k1,k2) và tương tự có s.rindex(s1,k1,k2)"
"s.startswith(s1)  s.endswith(s1) ếu đúng trả về True nếu không đúng trả về False"
m = s.startswith("a")
print(m)
m = s.endswith("s")
print(m)
"""
"""
s = "0++++++++++abc++++++++++0 \t 0++++++++++abc++++++++++0 \t 0++++++++++abc++++++++++0"
print(s)
s1 = ["thai", "luon vui tuoi", "2025"]
print(s1)
"s1 là 1 list, 1 set, 1 tuple gồm nhiều phần tử kiểu str"
"nối các phần tử trg s1 để tạo thành 1 str duy nhất "
"sử dụng chuỗi s làm cầu nối"
m =  s.join(s1)
print(m)

"len(s) Trả về độ dài của chuỗi s"
m = len(s)
print(m)
"s.replace(old,new,count) Thay chuỗi old trong s bằng chuỗi new vs count lần thay thế"
m = s.replace("+++++", "12321", 4)
print(m)

"s.strip(chars)  Loại bỏ ký tự char ở 2 đầu chuối s"
m = s.strip("+")
print(m)

"s.lstrip(chars) loại bỏ ký tự char ở bên trái chuỗi s"
m = s.lstrip("+")
print(m)
"s.rstrip(chars) loại bỏ ký tự char ở bên phải chuỗi s"
m = s.rstrip("+")
print(m)

"s.split(s1,k) Chia nhỏ chuỗi s ra, vị trí chia: gặp s1, xóa ký tự s1 đi; số lần chia k lần"
m = s.split("+")
print(m)

"s.splitlines(keepends) keepends(keep ends) True-False"
m = s.splitlines(False)
print(m)
m = s.splitlines(True)
print(m)
"s.zfill(width) zero fill điền đầy kỹ tự 0 vào bên trái cho đủ width"
m = s.zfill(100)
print(m)

"s.expandtabs(tabsize) mở rộng tab (\t) bằng tabsize(độ rộng của nó) "
m = s.expandtabs(100)
print(m)
"""

"""
s = "qwertyuiopasdfghjklzxcvbnm,./;'[]-=~`()_+{}<>?\|"
a = "qưertyuiopasdfghjklzxcvbnm"
b = "1234567890"
c = "1234567890⓪①②③④⑤⑥⑦⑧⑨"
d = "1234567890⓪①②③④⑤⑥⑦⑧⑨½⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅐⅛⅜⅝⅞⅑⅒↉⅟一二三"
e ="ABCDEG"

print(s)

"s.encode(encoding) mã hóa theo các kiểu utf-8, utf-16, utf-32"
"s.decode(decoding) giải mã ngược lại của encode "

s1 = s.encode("utf-16")
s2 = s1.decode("utf-16")

print(s1)
print(s2)

"max(str) trả về ký tự có mã ASCII lớn nhất"
"min(str) trả về ký tự có mã ASCII nhỏ nhất"

s1 = max(s)
s2 = min(s)
print(s1)
print(s2)
print("\n")

"s.isalpha() is alpabetic(ký tự là chữ)? tất cả ký tự trong s là chữ -> True"
m = s.isalpha()
m1 = a.isalpha()
print(m)
print(m1)
print("\n")

"s.isdecimal() is decimal(kỹ tự số thập phân)? tất cả chỉ chứ số từ 0,1,2,...,9 -> Trả về True/ko thì trả về false"
m = a.isdecimal()
m1 = b.isdecimal()
print(m)
print(m1)
print("\n")

"s.isdigit() is digital? các ký tự giá trị digital từ 0,1,2,3,...,9 & ⓪①②③④⑤⑥⑦⑧⑨ -> True/ còn lại False"
m1 = a.isdigit()
m2 = b.isdigit()
m3 = c.isdigit()
print(m1)
print(m2)
print(m3)
print("\n")

"s.isnumeric() is numeric? giống isdigit ngoài ra có thêm ½⅓⅔¼¾⅕⅖⅗⅘⅙⅚⅐⅛⅜⅝⅞⅑⅒↉⅟ + ký tự tượng hình như chữ trung "

m1 = a.isnumeric()
m2 = b.isnumeric()
m3 = c.isnumeric()
m4 = d.isnumeric()
print(m1)
print(m2)
print(m3)
print(m4)
print("\n")
"s.isalnum() is alphabetic + numberic"
m1 = a.isalnum()
m2 = b.isalnum()
m3 = c.isalnum()
m4 = d.isalnum()
print(m1)
print(m2)
print(m3)
print(m4)
print("\n")
"s.islower() trả về True nếu ko có chữ viết HOA"
m = s.islower()
m5 = e.islower()
print(m)
print(m5)
print("\n")
"s.isupper() trả về True nếu ko có chữ thường"
m = s.isupper()
m5 = e.isupper()
print(m)
print(m5)
print("\n")

f = "                              "
g = "                             1"
h = "Hom nay troi nang to"
i = "Hom Nay Troi Nang To"

"s.isspace() is True nếu tất cả đều là space"
m = f.isspace()
m1 = g.isspace()
print(m)
print(m1)
print("\n")

"s.istitle() trả về True nếu các chữ cái đầu của từng TỪ trg list viết HOA"
m2 = h.istitle()
m3 = i.istitle()
print(m2)
print(m3)
print("\n")
"""


