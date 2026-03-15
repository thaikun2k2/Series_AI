#kiểu dữ liệu Dictionary là một kiểu dữ liệu có thể lưu trữ nhiều giá trị khác nhau, được định nghĩa bằng cặp key-value (khóa-giá trị). Mỗi key phải là duy nhất trong dictionary và được sử dụng để truy cập giá trị tương ứng.
#kết hợp ưu điểm giữa list và set, dictionary cho phép lưu trữ dữ liệu theo cặp key-value, trong đó key là một chuỗi hoặc một số, và value có thể là bất kỳ kiểu dữ liệu nào, bao gồm cả list hoặc dictionary khác.
# tập hợp không có thứ tự, có thể thay đổi, và cho phép trùng lặp. Dictionary được sử dụng rộng rãi trong Python để lưu trữ và quản lý dữ liệu phức tạp, như thông tin người dùng, cấu hình, hoặc kết quả của các phép tính.
#dictionary có chỉ số cho mỗi giá trị.


#list = ["đào", "hồng", "bưởi", "đào"]
########   0      1       2        3
#set = {"đào", "hồng", "bưởi"}


#dictionary = [0: "đào", 1: "hồng", 2: "bưởi", 3: "đào"]
#dictionary = [ 2: "bưởi",0: "đào", 1: "hồng", 3: "đào"]
###########    key: value
##==>>>>> x = {key1:value1, key2:value2, key3:value3,...} ===> kiểu dictionary
### 1 value có thể có nhiểu key khác nhau nhưng 1 key chỉ có thể có 1 value duy nhất



#####-----Practice-----#####
#Cách tạo một dictionary:
# dict = {0: "đào", 1: "hồng", 2: "bưởi", 3: "đào"}
# print(f'dict = {dict}')
# print(f'kiểu dữ liệu của dict == {type(dict)}')

# a = dict[1]
# print(f'a = {a}')

## set(mutable) + list(mutable) ==>> dict
#trường hợp 1: Dict mutable ko thứ tự, dấu {}, phtử: immutable, ko trùng lặp
#==>>>>> dict = {key1:value1, key2:value2, key3:value3,..., keyn:valuen} ===> kiểu dictionary
##dict : mutable

###-----key: -----###
# immutable -->> list,set,dict ko thể dùng làm key
# --> int, float, str, tuple.. có thể dùng làm key

###-----value: -----###
# immutable và mutable  ===>> ALL kiểu dữ liệu
# cho phép trùng lặp



#eg:
# #set: {}, dict: {}
# a = {}
# print(type(a))

# b = set() #phải khai báo thế này vì set và dict có cùng kiểu {}
# print(type(b))




#c = {"Ho va ten":"Nguyễn Văn Tón", "Ngay Sinh": "10 - 04 -2002", "so dt": 386188386}
#c = {1:"Nguyễn Văn Tón", 2: "10 - 04 -2002", 3: 386188386}
# c = {(1, 2, 3):"Nguyễn Văn Tón", 2: "10 - 04 -2002", "so dt": 386188386}
# ### ko thể để key == list[], set{}, dict{} vì là mutable: unhashable
# ### có thể để là kiểu tuple()
# ###Key ko đc trùng lặp nhau nếu ko sẽ bỏ đi các phần tử trùng lặp từ trái qua phải chỉ giữ lại 1 phần tử cuối cùng bên phải 

# print(f'c == {c}')
# print(f'type == {type(c)}')





########------------so sánh các phương thức của list anđ dict------------########

###----------LIST----------###
##khi có 1 List là: x =["a", "b", "c"]
#Toán tử truy cập: x[n], x[n:m]
#Toán tử !=: +, *, in, not in
#Xóa 1 phtu: del x[n], x.remove(), x.pop(index)
#Xóa biển: del[x]
#Xóa vùng nhớ: x.clear() xóa cả biến cả vùng nhớ
#Copy ALL: x.copy()
#Lấy 1 PhTu: z = x.pop(index)
#đếm số PhTu: len(x)
#max,min: max(x), min(x)
#update: x[n]  new value
#add 1 PhTu: x.append() , x.insert()
#Add N PhTu: x.extend()
#chuyển đổi type: str(), tuple(), set(), list()
#get all key: -----------not have



###----------DICT----------###
#khi có 1 Dict là: d = {0 : "a", 1 : "b", 2 : "c"}
#Toán tử truy cập: d[key] if ko tồn tại sẽ báo lỗi, z = d.get(key,default) nếu key ko tồn tại sẽ trả về giá trị default nếu ko thiết lập sẽ là None, ko có d[n:m]
#z = d.setdefault(key,default) có 2 chức năng là: thêm 1 PhTu, trả về PhTu search
#Toán tử !=: in, not in; nhưng ko có +, *
#Xóa 1 phtu: del d[key], x.pop(key); nhưng ko có d.remove()
#Xóa 1 phtu cuối cùng: e.popitem() nhưng do dict ko theo thứ tự nên sẽ có lúc ko xóa đc
#Xóa biển: del x ##ko ảnh hưởng đến vùng nhớ
#Xóa vùng nhớ: d.clear() còn biến vẫn còn nhưng là rỗng
#Copy ALL: d.copy() --> tạo 1 dict mới lưu ở ô nhớ mới
#Lấy 1 PhTu: z = d.pop(key) lấy phần tử có KEY như vậy ra, z = d.popitem() chỉ lấy phần tử cuối
#đếm số PhTu: len(d)
#max,min: max(d), min(d) ==>>trả về key max và key min lưu ý phải cùng 1 kiểu dữ liệu
#update: d[key] = new value
#add 1 PhTu: d[new key] = value, d.setdefault(key,default) nếu đưa vào key mới thì tạo bthg, nếu đưa vào key cũ sẽ ko thay đổi j cả
#Add N PhTu: d.update()
#chuyển đổi type: dict(), constructor
#get all key: z = d.key()  with z: class dict_keys
# get all value: z = d.values() with z: class dict_values



#--------------------------------------------------------------------------------#


#######-----------Eg:-----------#######
#
# d = {0:"Nguyễn Văn Tón", 1: "10 - 04 -2002", 2: 386188386}
# e = {"Full Name":"Nguyễn Văn Tón", "Birthday": "10 - 04 -2002", "Numbers Phone": 386188386}


#z = d[3]#báo lỗi "KeyError: 3"
#có cách != là d.get(key,default=none) là khi ko có key trong dict d sẽ trả về giá trị là None
#z = d[0]
#z = d.get(3)# ko có key ==3 trg dict sẽ trả về giá trị là: None,type == NoneType

# z = d.get(3,"key ko tồn tại trg dict")#nếu muốn trả về nội dung là gì khi key ko tồn tại thì thêm vào
# print(f'z = {z}')
# print(f'type z là: {type(z)}')

# ###TH1: kiểm tra tồn tại
# y = 0 in d
# print(y)

# x = 3 in e
# print(x)

# ###TH2: duyệt qua key
# for i in e:
#     print(i," : ", e[i])

# ###TH2: duyệt qua value(giá trị)

# for i in e.values():
#     print(i)


####-------------Xóa 1 PhTu-------------####

###---------Del e[]---------###
# print(f'e== {e}')
# print(f'id == {id(e)}')
# del e["Full Name"]

# print(f'e== {e}')
# print(f'id == {id(e)}')## ko thay dổi ID ==> ko thay đổi ô nhớ
###-------------------------###

###---------e.pop()---------###
# print(f'e== {e}')
# print(f'id == {id(e)}')
# e.pop("Full Name")

# print(f'e== {e}')
# print(f'id == {id(e)}')#ko thay dổi ID ==> ko thay đổi ô nhớ
###-------------------------###


###---------e.popitem()---------###
# print(f'e== {e}')
# print(f'id == {id(e)}')
# e.popitem()

# print(f'e== {e}')
# print(f'id == {id(e)}')#ko thay dổi ID ==> ko thay đổi ô nhớ
###-------------------------###

####------------------------------------####


####-------------Xóa 1 biến-------------####

# print(f'e== {e}')
# print(f'id == {id(e)}')
# del e

# #print(f'e== {e}') #ko tìm thấy nữa sẽ hiện "NameError: name 'e' is not defined"


####------------------------------------####

####-------------Xóa 1 Vùng nhớ-------------####

# print(f'e== {e}')
# print(f'id == {id(e)}')
# e.clear()

# print(f'e== {e}') #hiện ra 1 dict rỗng chỉ xóa ô nhớ, ko xóa PhTu
# print(f'id == {id(e)}')#ko thay dổi ID ==> ko thay đổi ô nhớ

####----------------------------------------####

####-------------Copy ALL-------------####

# print(f'e== {e}')
# print(f'id == {id(e)}')
# u = e.copy()

# print(f'u== {u}') #hiện ra 1 dict mới
# print(f'id u == {id(u)}')#thay dổi ID new ==> thay đổi sang ô nhớ new

####-----------------------------------####


######-------------GET 1 PhTu-------------######
# ##GET PhTu theo key
# print(f'e== {e}')
# print(f'id == {id(e)}')
# z = e.pop("Birthday")

# print(f'z== {z}') #hiện ra 1 PhTu đc GET ra dựa theo key
# print(f'id z == {id(z)}')#thay dổi ID new ==> thay đổi sang ô nhớ new
# print(type(z)) #type = str gồm value


# ##GET PhTu cuối của dict
# print(f'e== {e}')
# print(f'id == {id(e)}')
# y = e.popitem()

# print(f'y== {y}') #hiện ra 1 PhTu cuối của dict e
# print(f'id y == {id(y)}')#thay dổi ID new ==> thay đổi sang ô nhớ new
# print(type(y)) #type = tuple gồm key, value

######------------------------------------######

# ###-------Đếm số PhTu
# print(f'e== {e}')
# print(f'id == {id(e)}')
# s = len(e)

# print(f's== {s}') #hiện ra kết quả là có 3 PhTu trg dict e
# print(type(s)) #type = int

###-------MAX, MIN
###lưu ý nếu trong 1 dict có  >= 1 key khác kiểu thì sẽ ko dùng đc max, min
###key = String sẽ max sẽ là dài nhất,  tương tụ với min.
###key = int sẽ hiện max là số to nhất, tương tụ với min.
# r = max(e)
# t = min(e)
# print(f'r== {r}') #hiện ra kết quả là có 3 PhTu trg dict e
# print(type(r)) #type = int
# print(f't== {t}') #hiện ra kết quả là có 3 PhTu trg dict e
# print(type(t)) #type = int

###-------UPDATE

# e["Full Name"] = "Nguyễn Văn Thái"
# print(f'e== {e}') #
# print(type(e)) #type = dict


###-------Thêm 1 PhTu
#e[new key] = value
# e["Work"] = "IT"
# print(f'e== {e}') #
# print(type(e)) #type = dict

#e.setdefault(key,default)
# #key new thì thêm mới bthg
# e.setdefault("Work", "IT")
# print(f'e== {e}') #
# print(type(e)) #type = dict

# #key old sẽ ko thay đổi j cả
# e.setdefault('Full Name', 'Nguyễn Văn Thái')
# print(f'e== {e}') #
# print(type(e)) #type = dict



###-------Thêm N PhTu
# #e.update()
#lưu ý ko đc thêm phần tử có key same vs key trong dict

# print(id(e))
# e.update(d)
# print(f'e== {e}') #
# print(type(e)) #type = dict
# print(id(e))## id ko ảnh hưởng j cả

#Toán tử truy cập:
# # z = d.get(key,default) nếu key ko tồn tại sẽ trả về giá trị default nếu ko thiết lập sẽ là None

# print(id(e))
# o = e.get(0,"ko tồn tại phần tử")
# print(f'o== {o}') # trả về là: ko tồn tại phần tử
# print(type(o)) #type = str
# print(id(o))## id đã thay đổi 

# j = e.get(0) # trả về là: None
# print(f'j== {j}') #
# print(type(o)) #type = str

#z = d.setdefault(key,default)

# p = e.setdefault("Full Name") #  
# print(f'p== {p}') # trả về là: "Nguyễn Văn Tón" đã có trg dict
# print(type(p)) #type = str
# print(f'e== {e}')

# print(id(e))
# k = e.setdefault(0,"ko tồn tại phần tử")
# print(f'k== {k}') # trả về là: ko tồn tại phần tử
# print(f'e== {e}') #do ko tìm thấy PhTu đó nên nó đã thêm PhTu vào trong e dict là: ""0: 'ko tồn tại phần tử'""
# print(id(k))## id đã thay đổi 
# print(id(e))## id đã ko thay đổi 

###############################################################


################## set: {}, dict: {}
##### s : list -->> dict want key: value, use (), [], {}
### xx = [0,"a", 1, "b", 2, "c"] if xx is list or tuple or set,not support dict but dict need key:value


# xx = [(0,"a"), (1, "b"), (2, "c")] #đang là 1 list
# x_x = dict(xx)
# #print(xx)
# print(type(xx))#list

# #print(x_x)
# print(type(x_x))# dict
# print("\n")
# #
# aa = [{0, "a"}, {1, "b"}, {2, "c"}] #đang là 1 list
# a_a = dict(aa)
# #print(aa)
# print(type(aa))#list

# #print(a_a)
# print(type(a_a))#dict
# print("\n")

# bb = [[0, "a"], [1, "b"], [2, "c"]]
# b_b = dict(bb)
# #print(bb)
# print(type(bb))

# #print(b_b)
# print(type(b_b))
# print("\n")


#### set -->> dict want key: value, use () and not use [], {}
##set is immutable; list and set is mutable should set down support list when -->> dict
##not support when dd = {[0, "a"], [1, "b"], [2, "c"]} d_d =dict(dd) -->>> outcome: TypeError: unhashable type: 'list'
##not support when dd = {{0, "a"}, {1, "b"}, {2, "c"}} d_d =dict(dd) -->>> outcome: TypeError: unhashable type: 'set'

### ===>>> set -->> dict  want key: value, use () and not use [], {}

##eg
# ee = {(0,"a"), (1, "b"), (2, "c")} #đang là 1 set
# e_e = dict(ee)
# #print(ee)
# print(type(ee))#set

# #print(e_e)
# print(type(e_e))#dict


#####tuple -->> dict want key: value, use (), [], {}

# ff = ((0,"a"), (1, "b"), (2, "c")) #đang là 1 tuple
# f_f = dict(ff)
# #print(ff)
# print(type(ff))#tuple

# #print(f_f)
# print(type(f_f))# dict
# print("\n")
# #
# gg = ({0, "a"}, {1, "b"}, {2, "c"}) #đang là 1 tuple
# g_g = dict(gg)
# #print(gg)
# print(type(gg))#tuple

# #print(g_g)
# print(type(g_g))#dict
# print("\n")

# hh = ([0, "a"], [1, "b"], [2, "c"])
# h_h = dict(hh)
# #print(hh)
# print(type(hh))

# #print(h_h)
# print(type(h_h))
# print("\n")


##===>>> tuple suport -->> dict want key: value, use (), [], {}

# kk = {0 : "a", 1 : "b", 2 : "c"}
# k1 = list(kk) ## chuyển đc nhưng kết quả chỉ thu đc key của dict
# print(k1)
# print(type(k1))

# k2 = set(kk) ## chuyển đc nhưng kết quả chỉ thu đc key của dict
# print(k2)
# print(type(k2))

# k3 = tuple(kk) ## chuyển đc nhưng kết quả chỉ thu đc key của dict
# print(k3)
# print(type(k3))

#####################GET all key
ll = {0 : "thai", 1 : "ngoc", 2 : "anh"}
l1 = ll.keys()

print(ll)

print(l1)
print(type(l1))

l2 = ll.values()
print(l2)
print(type(l2))