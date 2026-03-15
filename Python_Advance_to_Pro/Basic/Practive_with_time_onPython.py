#Eg1: Có bao nhiêu giây đã trôi qua tính từ 12:00 AM 01-01-1970???

import time

tichs = time.time()#tichs == tích tắc (đồng hồ quả lắc) = sec
# print(f'sec hay còn gọi là tichs == {tichs}')
# print(type(tichs))

# nowtime1 = time.localtime(1773580) ##time 1970 hiện tại
# print(nowtime1)
# print(type(nowtime1))

nowtime = time.localtime(tichs) #outcome time ở khu vực hiện tại(eg:Việt Nam = GMT + 7 hours) ##time hiện tại 1773580299,..
print(nowtime)
print(type(nowtime))

nowtime2 = time.gmtime(tichs) #outcome time year,month,day theo UTC(giờ quốc tế) = GMT
print(nowtime2)
print(type(nowtime2))
