
# ===============================
# LƯU Ý VỀ HÀM (FUNCTION) TRONG PYTHON
# ===============================

# | Nội dung | Cú pháp / Ví dụ | Ghi chú |
# |----------|-----------------|--------|
# | Khai báo hàm | def ten_ham(): | dùng từ khóa def |
# | Tham số (parameter) | def add(a, b): | a, b là tham số |
# | Gọi hàm | add(2,3) | truyền đối số |
# | Giá trị trả về | return a + b | return kết thúc hàm |
# | Hàm không return | def hello(): print("Hi") | mặc định trả về None |
# | Tham số mặc định | def hello(name="Python"): | dùng khi không truyền |
# | Keyword argument | hello(name="An") | truyền theo tên |
# | Positional argument | hello("An") | truyền theo vị trí |
# | *args | def sum_all(*args): | nhận nhiều đối số dạng tuple |
# | **kwargs | def info(**kwargs): | nhận nhiều key=value dạng dict |
# | Hàm trong hàm | def outer(): | nested function |
# | Lambda function | lambda x: x*2 | hàm 1 dòng |
# | Docstring | """Mô tả hàm""" | dùng để giải thích hàm |
# | Type hint | def add(a:int,b:int)->int | gợi ý kiểu dữ liệu |
# | Scope biến | local / global | phạm vi biến |
# | global keyword | global x | sửa biến global |
# | nonlocal keyword | nonlocal x | sửa biến ngoài hàm con |
# | Hàm là object | f = add | có thể gán cho biến |
# | Hàm làm tham số | map(func, list) | truyền hàm vào hàm |
# | Decorator | @decorator | mở rộng chức năng hàm |


##y = abs(x) trả outcome là y là trị tuyệt đối của x

