#Eg1: Có bao nhiêu giây đã trôi qua tính từ 12:00 AM 01-01-1970???

import sys
import time

sys.stdout.reconfigure(encoding='utf-8') #terminal Python use UTF-8 để print, nên các ký tự tiếng Việt ko còn gây lỗi UnicodeEncodeError nữa

# tichs = time.time()#tichs == tích tắc (đồng hồ quả lắc) = sec
# # print(f'sec hay còn gọi là tichs == {tichs}')
# # print(type(tichs))

# # nowtime1 = time.localtime(1773580) ##time 1970 hiện tại
# # print(nowtime1)
# # print(type(nowtime1))

# nowtime = time.localtime(tichs) #outcome time ở khu vực hiện tại(eg:Việt Nam = GMT + 7 hours) ##time hiện tại 1773580299,..
# # print(nowtime)
# # print(type(nowtime))

# # nowtime2 = time.gmtime(tichs) #outcome time year,month,day theo UTC(giờ quốc tế) = GMT
# # print(nowtime2)
# # print(type(nowtime2))

# ## nowtime, nowtime2 trả về 1 tuple
# # chuyển sang dạng dễ đọc use: time.asctime() =>> time về string
# ## lưu ý phải đưa vào dữ liệu kiểu tuple should not đưa tichs vào đc

# ##cách 1: 
# # lấy số sec(tichs) --> nowtime(tuple)=time.localtime() -->time.asctime(nowtime) -->now time string
# timeread = time.asctime(nowtime)
# # print(timeread)
# # print(type(timeread))

# ##cách 2: lấy số sec(tichs) --> time.ctime()
# timeread2 = time.ctime(tichs)
# # print(timeread2)
# # print(type(timeread2))



# """
# ######Date and Time: Module Time:
# # time.time() time(sec) --> use time.ctime() --> time(string)
# # time.time() time(sec) --> use time.localtime() or time.gmtime() --> time(tuple) -->use time.asctime() --> time(string)
# # time.time() time(sec) --> use time.localtime() or time.gmtime() --> time(tuple) -->use time.strftime() --> time(format)
# # time.time() time(sec) <-- use time.mktime() <-- time(tuple) <--use time.strptime() <-- time (format)
# _____________________________________________________________________________________________________________________________________
# | # | Luồng command Python                                                     | Kết quả cuối                                        |
# | - | ------------------------------------------------------------------------ | --------------------------------------------------- |
# | 1 | `time.time()` → `time.ctime()`                                           | `time(sec)` → `time(string)`                        |
# | 2 | `time.time()` → `time.localtime()` / `time.gmtime()` → `time.asctime()`  | `time(sec)` → `time(tuple)` → `time(string)`        |
# | 3 | `time.time()` → `time.localtime()` / `time.gmtime()` → `time.strftime()` | `time(sec)` → `time(tuple)` → `time(format string)` |
# | 4 | `time.strptime()` → `time.mktime()`                                      | `time(format string)` → `time(tuple)` → `time(sec)` |
# -------------------------------------------------------------------------------------------------------------------------------------
# """
# # print(tichs)
# # print(type(tichs))
# # time_sec = time.mktime(nowtime)
# # print(time_sec)
# # print(type(time_sec))

# tichs = time.time()#tichs == tích tắc (đồng hồ quả lắc) = sec
nowtime = time.localtime()
# print(nowtime)
# print(type(nowtime))

time_format = (
    f"{time.strftime('%Y', nowtime)} \"năm 4 chữ số\" - \n"
    f"{time.strftime('%y', nowtime)} \"năm 2 chữ số\" - \n"
    f"{time.strftime('%m', nowtime)} \"tháng dạng số\" - \n"
    f"{time.strftime('%B', nowtime)} \"tên tháng đầy đủ\" - \n"
    f"{time.strftime('%b', nowtime)} \"tên tháng viết tắt\" - \n"
    f"{time.strftime('%d', nowtime)} \"ngày trong tháng\" - \n"
    f"{time.strftime('%A', nowtime)} \"thứ đầy đủ trong tuần\" - \n"
    f"{time.strftime('%a', nowtime)} \"thứ viết tắt\" - \n"
    f"{time.strftime('%H', nowtime)} \"giờ hệ 24h\" - \n"
    f"{time.strftime('%I', nowtime)} \"giờ hệ 12h\" - \n"
    f"{time.strftime('%p', nowtime)} \"AM hoặc PM\" - \n"
    f"{time.strftime('%M', nowtime)} \"phút\" - \n"
    f"{time.strftime('%S', nowtime)} \"giây\" - \n"
    f"{time.strftime('%z', nowtime)} \"độ lệch múi giờ so với UTC\" - \n"
    f"{time.strftime('%Z', nowtime)} \"tên múi giờ\" - \n"
    f"{time.strftime('%j', nowtime)} \"ngày thứ bao nhiêu trong năm\" - \n"
    f"{time.strftime('%U', nowtime)} \"số tuần trong năm (tuần bắt đầu chủ nhật)\" - \n"
    f"{time.strftime('%W', nowtime)} \"số tuần trong năm (tuần bắt đầu thứ hai)\" - \n"
    f"{time.strftime('%c', nowtime)} \"ngày giờ đầy đủ theo hệ thống\" - \n"
    f"{time.strftime('%x', nowtime)} \"định dạng ngày\" - \n"
    f"{time.strftime('%X', nowtime)} \"định dạng giờ\" - \n"
    "%% \"ký tự phần trăm\""
)

print(time_format)
print(type(time_format))
print("\n")

time_tuple = nowtime
print(time_tuple)
print(type(time_tuple))
