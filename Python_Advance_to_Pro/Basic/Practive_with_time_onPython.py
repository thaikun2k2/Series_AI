#Eg1: Có bao nhiêu giây đã trôi qua tính từ 12:00 AM 01-01-1970???

import time

tichs = time.time()#tichs == tích tắc (đồng hồ quả lắc) = sec
# print(f'sec hay còn gọi là tichs == {tichs}')
# print(type(tichs))

# nowtime1 = time.localtime(1773580) ##time 1970 hiện tại
# print(nowtime1)
# print(type(nowtime1))

nowtime = time.localtime(tichs) #outcome time ở khu vực hiện tại(eg:Việt Nam = GMT + 7 hours) ##time hiện tại 1773580299,..
# print(nowtime)
# print(type(nowtime))

# nowtime2 = time.gmtime(tichs) #outcome time year,month,day theo UTC(giờ quốc tế) = GMT
# print(nowtime2)
# print(type(nowtime2))

## nowtime, nowtime2 trả về 1 tuple
# chuyển sang dạng dễ đọc use: time.asctime() =>> time về string
## lưu ý phải đưa vào dữ liệu kiểu tuple should not đưa tichs vào đc

##cách 1: 
# lấy số sec(tichs) --> nowtime(tuple)=time.localtime() -->time.asctime(nowtime) -->now time string
timeread = time.asctime(nowtime)
print(timeread)
print(type(timeread))

##cách 2: lấy số sec(tichs) --> time.ctime()
timeread2 = time.ctime(tichs)
print(timeread2)
print(type(timeread2))




######Date and Time: Module Time:
# time.time() time(sec) --> use time.ctime() --> time(string)
# time.time() time(sec) --> use time.localtime() or time.gmtime() --> time(tuple) -->use time.asctime() --> time(string)
# time.time() time(sec) --> use time.localtime() or time.gmtime() --> time(tuple) -->use time.strftime() --> time(format)
# time.time() time(sec) <-- use time.mktime() <-- time(tuple) <--use time.strptime() <-- time (format)
"""
| # | Luồng command Python                                                     | Kết quả cuối                                        |
| - | ------------------------------------------------------------------------ | --------------------------------------------------- |
| 1 | `time.time()` → `time.ctime()`                                           | `time(sec)` → `time(string)`                        |
| 2 | `time.time()` → `time.localtime()` / `time.gmtime()` → `time.asctime()`  | `time(sec)` → `time(tuple)` → `time(string)`        |
| 3 | `time.time()` → `time.localtime()` / `time.gmtime()` → `time.strftime()` | `time(sec)` → `time(tuple)` → `time(format string)` |
| 4 | `time.strptime()` → `time.mktime()`                                      | `time(format string)` → `time(tuple)` → `time(sec)` |
"""
