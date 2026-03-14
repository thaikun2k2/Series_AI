#mutable là có thể thay đổi được, có thể thêm, sửa, xóa phần tử
#immutable là không thể thay đổi được, không thể thêm, sửa, xóa phần tử
# sư khác nhau của set, list, tuple:
# set không có thứ tự, không có index, không có phần tử trùng lặp
# list có thứ tự, có index, có phần tử trùng lặp

#Eg:
# set = {1, 2, "a"}
# list = [1, 2, "a", 1]
# tuple = (1, 2, "a", 1)


# set1 = {4, 2, "a"}
# list1 = [4, 2, "a", 4]
# tuple = (4, 2, "a", 4)

#tuple cho phép chứa phần tử: 
#1.immutable (không thể thay đổi được) => tuple: immutable
#2.mutable (có thể thay đổi được) => tuple: mutable

#list cho phép chứa phần tử:
#1.immutable (không thể thay đổi được) => bản thân nó là mutable
#2.mutable (có thể thay đổi được) => bản thân nó là mutable

#set cho phép chứa phần tử:
#1.immutable (không thể thay đổi được) => set: immutable bản thân nó là mutable
#2. ko cho phép chứa mutable

#tuple chứa: set, list, tuple
#list chứa: set, list, tuple
#set chứa: ko cho phép chứa set, tuple, ko chứa list

### #eg tuple:
# x = (1, 2, 3, "a")
# a = {1, 2, 3, "a"}
# b = [1, 2, 3, "a"]
# y = (4, 5, 6, "ab", x, a, b)
# print(x)
# print(y)
# print(type(x))
# print(type(a))
# print(type(b))
# print(type(y))

#eg list:
# x = (1, 2, 3, "a")
# a = {1, 2, 3, "a"}
# b = [1, 2, 3, "a"]
# y = [4, 5, 6, "ab", x, a, b]
# print(x)
# print(y)
# print(type(x))
# print(type(a))
# print(type(b))
# print(type(y))

### #eg set: set chứa: tuple, ko cho phép chứa set, ko chứa list
# x = (1, 2, 3, "a")
# a = {1, 2, 3, "a"}
# b = [1, 2, 3, "a"]
# y = {4, 5, 6, "ab", x}
# # y = {4, 5, 6, "ab", x, a} # lỗi vì set không cho phép chứa set
# # y = {4, 5, 6, "ab", x, b} # lỗi vì set không cho phép chứa list
# # y = {4, 5, 6, "ab", x, a, b} # lỗi vì set không cho phép chứa set, list
# print(x)
# print(y)
# print(type(x))
# print(type(a))
# print(type(b))
# print(type(y))

# for i in y:
#     print(i) # kết quả ko có thứ tự vì set không có thứ tự, không có index, không có phần tử trùng lặp


#Toán tử trên list: [n], [n:m], [n:m:k],+, *, in, not in
#Toán tử trên tuple: [n], [n:m], [n:m:k],+, *, in, not in
#Toán tử trên set: +, *, in, not in
#trên set không có toán tử [n], [n:m], [n:m:k], +, * vì set không có thứ tự, không có index, không có phần tử trùng lặp
#trên list và tuple có toán tử [n], [n:m], [n:m:k] vì list và tuple có thứ tự, có index
#list,tuple có: index, count(), sort(), reverse(),
#set không có: index, count(), sort(), reverse() vì set không có thứ tự, không có index, không có phần tử trùng lặp





###########################################################################

#set tập hợp nhiều phần tử - ko có thứ tự - ko có index - ko có phần tử trùng lặp - mutable --->>>> same list[]

# a =[1, 2, 3, "a", 1]
# #print(type(a))
# b =(1, 2, 3, "a", 1)
# #print(type(b))
# y ="abcabcabcabcabc"
# #print(type(y))
# kk = {1, 2, 3, "a", 1}
# #print(type(kk))
# tt= {4, 5, 6, "ab"}
# m = set(y)
# print(m) # kết quả: {'a', 'b', 'c'} vì set không có phần tử trùng lặp   
# #cách thêm 1 phần tử vào list: a.append("b")
# #cách thêm 1 phần tử vào set: kk.add("b") 
# print(id(kk))


# kk.add("b")
# print(kk) # kết quả: {'a', 'b', 'c'} vì set không có phần tử trùng lặp, nếu thêm phần tử đã tồn tại thì sẽ không thêm vào set nữa
# #print(id(kk)) # id của set kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử

#cách thêm n phần tử vào list: x.extend(tt) vs tt là tập hợp nhiều phần tử
#cách thêm n phần tử vào set: kk.update(tt) and m = kk.union(tt) vs tt là tập hợp nhiều phần tử

# kk.update(tt)
# print(kk) # kết quả: {'a', 'b', 'c', 1, 2, 3, 4, 5, 6, 'ab'} vì set không có phần tử trùng lặp, nếu thêm phần tử đã tồn tại thì sẽ không thêm vào set nữa
#print(id(kk)) # id của set kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử

# m = kk.union(tt) # tạo set mới là m
# #union chấp nhận thêm cả list, tuple, set, string bằng cách chuyển thành type == set và thêm vào set mới m nhưng sẽ loại bỏ phần tử trùng lặp
# # còn update chỉ chấp nhận thêm set vào set cũ kk và sẽ loại bỏ phần tử trùng lặp
# print(m) # kết quả: {'a', 'b', 'c', 1, 2, 3, 4, 5, 6, 'ab'} vì set không có phần tử trùng lặp, nếu thêm phần tử đã tồn tại thì sẽ không thêm vào set nữa
# print(id(m)) # id của set m khác với id của set kk vì m là một set mới được tạo ra từ set kk và set tt, còn kk là set cũ đã được cập nhật thêm phần tử từ set tt nên id của kk vẫn giữ nguyên, còn id của m là id của set mới được tạo ra.

# #list, tuple khi xóa 1 phần tử có del["a"], kk.remove("a")
# #set khi xóa 1 phần tử có kk.remove("a"), kk.discard("a") 
# kk.remove("a") # nếu phần tử "a" tồn tại trong set kk thì sẽ xóa phần tử "a" khỏi set kk
# # if phần tử "a" không tồn tại trong set kk thì sẽ báo lỗi KeyError: 'a'
# print(kk) # kết quả: {1, 2, 3, 'b'} vì phần tử "a" đã bị xóa khỏi set kk
# print(id(kk)) # id của set kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử

# kk.discard("b") # nếu phần tử "b" tồn tại trong set kk thì sẽ xóa phần tử "b" khỏi set kk
# #if nếu phần tử "b" không tồn tại trong set kk thì sẽ không báo lỗi mà sẽ bỏ qua lệnh discard
# print(kk) # kết quả: {1, 2, 3} vì phần tử "b" đã bị xóa khỏi set kk
# print(id(kk)) # id của set kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử











######################################################################################



# a =[1, 2, 3, "a", 1]
# #print(type(a))
# b =(1, 2, 3, "a", 1)
# #print(type(b))
# y ="abcabcabcabcabc"
#print(type(y))
#kk = {1, 2, 3, "a", 1}
#print(id(kk))
#print(type(kk))
# tt= {4, 5, 6, "ab"}
# m = set(y)
# print(m) # kết quả: {'a', 'b', 'c'} vì set không có phần tử trùng lặp   
#cách thêm 1 phần tử vào list: a.append("b")
#cách thêm 1 phần tử vào set: kk.add("b") 



#list xóa biến là del x[n]
#set xóa biến là del kk

#list xóa vùng nhớ x.clear()
#set xóa vùng nhớ kk.clear()    

#list copy toàn bộ là x.copy()
#set copy toàn bộ là kk.copy()

# del kk # xóa biến kk khỏi bộ nhớ, nếu muốn xóa phần tử trong set kk thì dùng kk.clear() để xóa tất cả phần tử trong set kk nhưng vẫn giữ biến kk tồn tại trong bộ nhớ, còn del kk sẽ xóa biến kk khỏi bộ nhớ nên không thể truy cập được biến kk nữa.
# print(kk) # lỗi NameError: name 'kk' is not defined vì biến kk


# kk.clear() # xóa tất cả phần tử trong set kk nhưng vẫn giữ biến kk tồn tại trong bộ nhớ
# print(kk) # kết quả: set() vì set kk đã bị xóa tất cả phần tử nhưng vẫn tồn tại trong bộ nhớ nên có thể truy cập được biến kk và kết quả là set() vì set kk đã bị xóa tất cả phần tử nên kết quả là set().
# print(id(kk)) # id của set kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử nhưng vẫn giữ biến kk tồn tại trong bộ nhớ nên id của kk vẫn giữ nguyên.

# o = kk.copy() # tạo set mới là kk_copy có cùng phần tử với set kk nhưng có id khác với set kk vì kk_copy là một set mới được tạo ra từ set kk nên id của kk_copy khác với id của kk, còn kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử nhưng vẫn giữ biến kk tồn tại trong bộ nhớ nên id của kk vẫn giữ nguyên.
# print(o) # kết quả: {1, 2, 3} vì set o có cùng phần tử với set kk nhưng có id khác với set kk vì o là một set mới được tạo ra từ set kk nên kết quả là {1, 2, 3} vì set kk có phần tử là 1, 2, 3.
# print(id(o)) # id của set o khác với id của set kk vì o là một set mới được tạo ra từ set kk nên id của o khác với id của kk, còn kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử nhưng vẫn giữ biến kk tồn tại trong bộ nhớ nên id của kk vẫn giữ nguyên.



#lấy 1 phần tử trong list a bằng cách dùng hàm o = a.pop() vì list có thứ tự, có index nên có thể lấy phần tử theo index được bằng cách dùng hàm pop() để lấy phần tử cuối cùng trong list a, nếu list a rỗng thì sẽ báo lỗi IndexError: pop from empty list vì không thể lấy phần tử từ một list rỗng được.
#lấy 1 phần tử bất kỳ trong set kk bằng cách dùng hàm o = kk.pop() vì set không có thứ tự, không có index nên không thể lấy phần tử theo index được mà phải dùng hàm pop() để lấy phần tử bất kỳ trong set kk, nếu set kk rỗng thì sẽ báo lỗi KeyError: 'pop from an empty set' vì không thể lấy phần tử từ một set rỗng được.

# m = kk.pop() # lấy 1 phần tử bất kỳ trong set kk và xóa phần tử đó khỏi set kk, nếu set kk rỗng thì sẽ báo lỗi KeyError: 'pop from an empty set' vì không thể lấy phần tử từ một set rỗng được.
# print(m) # kết quả: 1 hoặc 2 hoặc 3 hoặc 'a'
# print(kk) # kết quả: {2, 3, 'a'} hoặc {1, 3, 'a'} hoặc {1, 2, 'a'} hoặc {1, 2, 3} vì phần tử m đã bị xóa khỏi set kk nên kết quả là set kk còn lại sau khi đã xóa phần tử m khỏi set kk.
# print(id(m)) # id của phần tử m khác với id của set kk vì m là một phần tử trong set kk nên id của m khác với id của kk, còn kk vẫn giữ nguyên vì set là mutable, có thể thay đổi được, có thể thêm, sửa, xóa phần tử nhưng vẫn giữ biến kk tồn tại trong bộ nhớ nên id của kk vẫn giữ nguyên.



#################################################################################################################



# #list dùng max,min để lấy phần tử lớn nhất, nhỏ nhất trong list a vì list có thứ tự, có index nên có thể lấy phần tử theo index được bằng cách dùng hàm max() để lấy phần tử lớn nhất trong list a và hàm min() để lấy phần tử nhỏ nhất trong list a, nếu list a rỗng thì sẽ báo lỗi ValueError: max() arg is an empty sequence hoặc ValueError: min() arg is an empty sequence vì không thể lấy phần tử từ một list rỗng được.
# #set dùng max,min để lấy phần tử lớn nhất, nhỏ nhất trong set kk vì set không
# x = [1, 2, 3, 4, 5, 6, 1, 2, 3] # list x có phần tử là 1, 2, 3, 4, 5, 6 vì list có thứ tự, có index nên có thể lấy phần tử theo index được bằng cách dùng hàm max() để lấy phần tử lớn nhất trong list x và hàm min() để lấy phần tử nhỏ nhất trong list x, nếu list x rỗng thì sẽ báo lỗi ValueError: max() arg is an empty sequence hoặc ValueError: min() arg is an empty sequence vì không thể lấy phần tử từ một list rỗng được.
# kk = {1, 2, 3, 4, 5, 6, 1, 2, 3} # set kk có phần tử là 1, 2, 3, 4, 5, 6 vì set không có phần tử trùng lặp nên phần tử 1, 2, 3 chỉ được lưu trữ một lần trong set kk.
# print(type(x)) # kết quả: <class 'list'> vì x là một list.
# print(type(kk)) # kết quả: <class 'set'> vì kk là một set


# i = max(kk) # lấy phần tử lớn nhất trong set kk, nếu set kk rỗng thì sẽ báo lỗi ValueError: max() arg is an empty sequence vì không thể lấy phần tử từ một set rỗng được.
# print(i) # kết quả: 3 vì phần tử lớn nhất trong set kk là 3.
# u = min(kk) # lấy phần tử nhỏ nhất trong set kk, nếu set kk rỗng thì sẽ báo lỗi ValueError: min() arg is an empty sequence vì không thể lấy phần tử từ một set rỗng được.
# print(u) # kết quả: 2 vì phần tử nhỏ nhất trong set kk là 2.
# # điều kiện là các phần tử trong kk phải cùng kiểu dữ liệu với nhau

# trg list z =sum(x) để lấy tổng các phần tử trong list x vì list có thứ tự, có index nên có thể lấy phần tử theo index được bằng cách dùng hàm sum() để lấy tổng các phần tử trong list x, nếu list x rỗng thì sẽ trả về 0 vì tổng của một list rỗng là 0.
# trg set z =sum(kk) để lấy tổng các phần tử trong set kk vì set không có thứ tự, không có index nên không thể lấy phần tử theo index được mà phải dùng hàm sum() để lấy tổng các phần tử trong set kk, nếu set kk rỗng thì sẽ trả về 0 vì tổng của một set rỗng là 0.

# z = sum(x) # lấy tổng các phần tử trong list x, nếu list x rỗng thì sẽ trả về 0 vì tổng của một list rỗng là 0.
# print(z) # kết quả: 27 vì tổng của các phần tử trong list x là 1 + 2 + 3 + 4 + 5 + 6 + 1 + 2 + 3 = 27.

# z = sum(kk) # lấy tổng các phần tử trong set kk, nếu set kk rỗng thì sẽ trả về 0 vì tổng của một set rỗng là 0.
# print(z) # kết quả: 21 vì tổng của các phần tử trong set kk là 1 + 2 + 3 + 4 + 5 + 6 = 21.


# list sử dụng x.sort() để sắp xếp các phần tử trong list x theo thứ tự tăng dần vì list có thứ tự, có index nên có thể lấy phần tử theo index được bằng cách dùng hàm sort() để sắp xếp các phần tử trong list x theo thứ tự tăng dần, nếu list x rỗng thì sẽ không có phần tử nào để sắp xếp nên kết quả là một list rỗng.
# set không có hàm sort() để sắp xếp các phần tử trong set kk vì set không có thứ tự, không có index nên không thể lấy phần tử theo index được mà phải dùng hàm sort() để sắp xếp các phần tử trong set kk, nếu set kk rỗng thì sẽ không có phần tử nào để sắp xếp nên kết quả là một set rỗng.

# e = sorted(x) # sắp xếp các phần tử trong list x theo thứ tự tăng dần và trả về một list mới đã được sắp xếp, nếu list x rỗng thì sẽ trả về một list rỗng.
# print(e) # kết quả: [1, 1, 2, 2, 3, 3, 4, 5, 6] vì các phần tử trong list x đã được sắp xếp theo thứ tự tăng dần.

# e = sorted(kk) # sắp xếp các phần tử trong set kk theo thứ tự tăng dần và trả về một list mới đã được sắp xếp, nếu set kk rỗng thì sẽ trả về một list rỗng.
# print(e) # kết quả: [1, 2, 3, 4, 5, 6] vì các phần tử trong set kk đã được sắp xếp theo thứ tự tăng dần và trả về một list mới đã được sắp xếp.







#################################################################################################################


######các phép toán tập hợp dùng set: 
##gọi A và B là 2 tập hợp, thì có các phép toán tập hợp sau:
# intersection(A giao B), union(A hợp B), difference(hiệu:A - B, A/B), symmetric_difference(phần ko trung của A và B: A hợp B - A giao B)

# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}



# C = A & B # giao của A và B là tập hợp các phần tử chung của A và B, nếu A và B không có phần tử chung thì giao của A và B là một tập hợp rỗng.
# #= C = A.intersection(B) # giao của A và B là tập hợp các phần tử chung của A và B, nếu A và B không có phần tử chung thì giao của A và B là một tập hợp rỗng.
# #= C = B.intersection(A) # giao của B và A là tập hợp các phần tử chung của B và A, nếu B và A không có phần tử chung thì giao của B và A là một tập hợp rỗng.
# print(C) # kết quả: {4, 5} vì phần tử chung của A và B là 4 và 5.

# D = A | B # hợp của A và B là tập hợp các phần tử thuộc A hoặc thuộc B hoặc thuộc cả A và B, nếu A và B không có phần tử chung thì hợp của A và B là tập hợp các phần tử của A và tập hợp các phần tử của B.
# #= D = A.union(B) # hợp của A và B là tập hợp các phần tử thuộc A hoặc thuộc B hoặc thuộc cả A và B, nếu A và B không có phần tử chung thì hợp của A và B là tập hợp các phần tử của A và tập hợp các phần tử của B.
# #= D = B.union(A) # hợp của A và B là tập hợp các phần tử thuộc A hoặc thuộc B hoặc thuộc cả A và B, nếu A và B không có phần tử chung thì hợp của A và B là tập hợp các phần tử của A và tập hợp các phần tử của B.
# print(D) # kết quả: {1, 2, 3, 4, 5, 6, 7, 8} vì phần tử thuộc A hoặc thuộc B hoặc thuộc cả A và B là 1, 2, 3, 4, 5, 6, 7, 8.

# E = A - B # hiệu của A và B là tập hợp các phần tử thuộc A nhưng không thuộc B, nếu A và B không có phần tử chung thì hiệu của A và B là tập hợp các phần tử của A.
# #= E = A.difference(B) # hiệu của A và B là tập hợp các phần tử thuộc A nhưng không thuộc B, nếu A và B không có phần tử chung thì hiệu của A và B là tập hợp các phần tử của A.
# H = B - A # hiệu của B và A là tập hợp các phần tử thuộc B nhưng không thuộc A, nếu B và A không có phần tử chung thì hiệu của B và A là tập hợp các phần tử của B.
# # khác H = B.difference(A) # hiệu của B và A là tập hợp các phần tử thuộc B nhưng không thuộc A, nếu B và A không có phần tử chung thì hiệu của B và A là tập hợp các phần tử của B.
# print(E) # kết quả: {1, 2, 3} vì phần tử thuộc A nhưng không thuộc B là 1, 2, 3.
# print(H) # kết quả: {6, 7, 8} vì phần tử thuộc B nhưng không thuộc A là 6, 7, 8.


# G = A ^ B # phần không trung của A và B là tập hợp các phần tử thuộc A hoặc thuộc B nhưng không thuộc cả A và B, nếu A và B không có phần tử chung thì phần không trung của A và B là tập hợp các phần tử của A và tập hợp các phần tử của B.
# #= G = A.symmetric_difference(B) # phần không trung của A và B là tập hợp các phần tử thuộc A hoặc thuộc B nhưng không thuộc cả A và B, nếu A và B không có phần tử chung thì phần không trung của A và B là tập hợp các phần tử của A và tập hợp các phần tử của B.
# #= G = B.symmetric_difference(A) # phần không trung của B và A là tập hợp các phần tử thuộc B hoặc thuộc A nhưng không thuộc cả B và A, nếu B và A không có phần tử chung thì phần không trung của B và A là tập hợp các phần tử của B và tập hợp các phần tử của A.
# print(G) # kết quả: {1, 2, 3, 6, 7, 8} vì phần tử thuộc A hoặc thuộc B nhưng không thuộc cả A và B là 1, 2, 3, 6, 7, 8.


# M = A.difference_update(B) 
# # hiệu cập nhật của A và B là tập hợp các phần tử thuộc A nhưng không thuộc B
# # sau khi thực hiện hiệu cập nhật thì tập hợp A sẽ được cập nhật thành tập hợp các phần tử thuộc A nhưng không thuộc B
# # nếu A và B không có phần tử chung thì hiệu cập nhật của A và B là tập hợp các phần tử của A.
# # khác M = A.difference_update(B) # hiệu cập nhật của A và B là tập hợp các phần tử thuộc A nhưng không thuộc B, sau khi thực hiện hiệu cập nhật thì tập hợp A sẽ được cập nhật thành tập hợp các phần tử thuộc A nhưng không thuộc B, nếu A và B không có phần tử chung thì hiệu cập nhật của A và B là tập hợp các phần tử của A.
# print(M) # kết quả: None vì hàm difference_update() không trả về giá trị nào mà chỉ cập nhật tập hợp A thành tập hợp các phần tử thuộc A nhưng không thuộc B, nên kết quả là None.
# print(A) # kết quả: {1, 2, 3} vì sau khi thực hiện hiệu cập nhật thì tập hợp A đã được cập nhật thành tập hợp các phần tử thuộc A nhưng không thuộc B, nên kết quả là {1, 2, 3} vì phần tử thuộc A nhưng không thuộc B là 1, 2, 3.

# O = A.intersection(B)
# print(O) # kết quả: {4, 5} vì phần tử chung của A và B là 4 và 5.
# print(A) # kết quả: {1, 2, 3, 4, 5} vì sau khi thực hiện giao của A và B thì tập hợp A vẫn giữ nguyên vì hàm intersection() trả về một tập hợp mới là giao của A và B nhưng không cập nhật tập hợp A thành giao của A và B nên tập hợp A vẫn giữ nguyên là {1, 2, 3, 4, 5}.
# N = A.intersection_update(B)
# # giao cập nhật của A và B là tập hợp các phần tử thuộc A và thuộc B
# # sau khi thực hiện giao cập nhật thì tập hợp A sẽ được cập nhật thành tập hợp các phần tử thuộc A và thuộc B
# # nếu A và B không có phần tử chung thì giao cập nhật của A và B là một tập hợp rỗng.
# # khác N = A.intersection(B) # giao cập nhật của A và B là tập hợp các phần tử thuộc A và thuộc B, sau khi thực hiện giao cập nhật thì tập hợp A sẽ được cập nhật thành tập hợp các phần tử thuộc A và thuộc B, nếu A và B không có phần tử chung thì giao cập nhật của A và B là một tập hợp rỗng.
# print(N) # kết quả: None vì hàm intersection_update() không trả về giá trị nào mà chỉ cập nhật tập hợp A thành tập hợp các phần tử thuộc A và thuộc B, nên kết quả là None.
# print(A) # kết quả: set() vì sau khi thực hiện giao cập nhật thì tập hợp A đã được cập nhật thành tập hợp các phần tử thuộc A và thuộc B, nên kết quả là set() vì A và B không có phần tử chung nên giao của A và B là một tập hợp rỗng.

# K = A.symmetric_difference(B)
# print(K) # kết quả: {1, 2, 3, 6, 7, 8} vì phần tử thuộc A hoặc thuộc B nhưng không thuộc cả A và B là 1, 2, 3, 6, 7, 8. 
# print(A) # kết quả: {1, 2, 3, 4, 5} vì sau khi thực hiện phần không trung của A và B thì tập hợp A vẫn giữ nguyên vì hàm symmetric_difference() trả về một tập hợp mới là phần không trung của A và B nhưng không cập nhật tập hợp A thành phần không trung của A và B nên tập hợp A vẫn giữ nguyên là {1, 2, 3, 4, 5}.
# print(B) # kết quả: {4, 5, 6, 7, 8} vì sau khi thực hiện phần không trung của A và B thì tập hợp B vẫn giữ nguyên vì hàm symmetric_difference() trả về một tập hợp mới là phần không trung của A và B nhưng không cập nhật tập hợp B thành phần không trung của A và B nên tập hợp B vẫn giữ nguyên là {4, 5, 6, 7, 8}.
# A.symmetric_difference_update(B)
# print(A) # kết quả: {1, 2, 3, 6, 7, 8} vì sau khi thực hiện phần không trung cập nhật thì tập hợp A đã được cập nhật thành tập hợp các phần tử thuộc A hoặc thuộc B nhưng không thuộc cả A và B, nên kết quả là {1, 2, 3, 6, 7, 8} vì phần tử thuộc A hoặc thuộc B nhưng không thuộc cả A và B là 1, 2, 3, 6, 7, 8. 
# print(B) # kết quả: {4, 5, 6, 7, 8} vì sau khi thực hiện phần không trung cập nhật thì tập hợp B vẫn giữ nguyên vì hàm symmetric_difference_update() chỉ cập nhật tập hợp A thành phần không trung của A và B nhưng không cập nhật tập hợp B nên tập hợp B vẫn giữ nguyên là {4, 5, 6, 7, 8}.



# L = A.isdisjoint(B) # kiểm tra xem A và B có phần tử chung hay không, nếu A và B không có phần tử chung thì trả về True, ngược lại trả về False.
# print(L) # kết quả: False vì A và B có phần tử chung là 4 và 5 nên A và B không rời rạc với nhau nên kết quả là False.
# P = A.issubset(B) # kiểm tra xem A có phải là tập con của B hay không, nếu A là tập con của B thì trả về True, ngược lại trả về False.
# print(P) # kết quả: False vì A không phải là tập con của B vì A có phần tử 1, 2, 3 không thuộc B nên A không phải là tập con của B nên kết quả là False.
# T = A.issuperset(B) # kiểm tra xem A có phải là tập cha của B hay không, nếu A là tập cha của B thì trả về True, ngược lại trả về False.
# print(T) # kết quả: False vì A không phải là tập cha của B vì A có phần tử 4, 5 thuộc B nhưng A không có phần tử 6, 7, 8 thuộc B nên A không phải là tập cha của B nên kết quả là False.



