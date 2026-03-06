list = ["a","b","c","d",1,2,3,4,5,6,7,8,9,0]
print(list)
print(id(list))
inter = [2,3,4,5,9,1,6,7,8,0,9]
print(inter)
print(id(inter))

"""
#chèn 1 phân tử trg 1 vitri trg List
'ảnh hưởng đến ptư sau sẽ bị đẩy về sau. eg chèn vị trí 4 thì ptu 4 trc đó sẽ thành phần tử 5 trg List'
list.insert(4,"e")
print(list)
print(id(list))
#id ko thay đổi =>ô nhớ ko thay đổi

#chèn 1 ptu vào cuối list
list.append("e")
print(list)
print(id(list))
#id ko thay đổi =>ô nhớ ko thay đổi

#lấy mất phần tử thứ index ra khỏi list
#new list --> mấy ptu đó, thay đổi id so vs ban đầu
x = list.pop(4)
print(x)
print(id(x))
#Hiển thị ra phần tử đã lấy trong list
print(list)
#Hiển thị ra List sau khi thay đổi
print(id(list))
#id của list sau khi pop sẽ ko thay đổi

### != của pop và del là: pop print ra đc phần tử đã lấy đi còn del thì ko####

del list[1]
print(list)
#delete ptu thứ index ra khỏi list
print(id(list))
#id sau khi thực hiện sẽ ko thay đổi

#đảo ngc list dùng reverse
list.reverse()
print(list)
print(id(list))
#id sau khi thực hiện sẽ ko thay đổi

### lưu ý phần tử phải cùng kiểu dữ liệu eg: str,int,v.v...###

#sắp sếp theo giá trị tăng dần giá trị phần tử trong 1 list
#inter.sort()
'<=>'
inter.sort(key=None,reverse=False)
print(inter)
print(id(inter))
#id sau khi thực hiện sẽ ko thay đổi

#sắp sếp theo giá trị giảm dần giá trị phần tử trong 1 list
inter.sort(key=None,reverse=True)
print(inter)
print(id(inter))
#id sau khi thực hiện sẽ ko thay đổi

#remove all các phần tử trg list
inter.clear()
print(inter)
print(id(inter))
#id sau khi thực hiện sẽ ko thay đổi

#copy từ 1 list ra list!=
x = inter.copy()
print(x)
print(id(x))
#id sau khi thực hiện đã thay đổi
#-->đã copy ra 1 list != nằm ở vùng khác ở trg bộ nhớ

#trả về giá trị index của phần tử value đc tìm thấy đầu tiên từ left--->right & đc tìm thấy trg vùng từ start --> stop trg list
#x = inter.index(value,start,stop)

x = inter.index(9,1,5)
print(x)
print(id(inter))

#đếm số lần xuất hiện phần tử trg list
s = inter.count(9)
print(s)
print(id(s))
"""





