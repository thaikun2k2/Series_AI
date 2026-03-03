"---------------------------"
"||       TOÁN TỬ %       ||"
"---------------------------"

x=12.33
#y = str(int(x))
#str = %
#int = i
#=="%i%
#1.x-> đổi sang integer
#2.Tiếp tục đổi sang string
y = "%i" %(x)
print(y, type(y))
a = "nguyen van thai"
b = 10042002
x =  "Anh %s sinh vào thoi gian %i"  %(a, b)
print(x)
print("f'{a} sinh vào thoi gian {b}') + f'{x}'")

#%s  (->str->str)
#%i  (->int->str) có dấu i = integer
#%d  (->int->str) có dấu d = decimal
#%u  (->int->str) ko dấu u = unsigned != signed decimal integer(có âm dương)
#%x  (->hex->str) hex cơ số 16
#%e  (->exp->str) exp = lũy thừa
#%f  (->float->str) float = số thực



