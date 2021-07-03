## Tool lấy khoá học từ ngoaingu24h

### Hướng dãn cài đặt:
1. Cài đặt python
2. Cài đặt các thư viên python cần thiết:
```bash
pip install -r requirements.txt
```
### Hướng dẫn sử dụng:
#### 1. Lấy tài liệu từ ID khoá học:
Bước 1: Mở file `document.py`

Bước 2: Lấy ID khoá học từ website
> Click vào 1 khoá học => ID của khoá học là 1 con số sẽ hiển thị phía trên đường dẫn

> Ví dụ: https://ngoaingu24h.vn/khoa-hoc-5958158015004672

> Vậy ID của khoá học là `5958158015004672`

Bước 4: Lấy ID khoá học cho vào hàm `GetAllDocsInCourseById`
> Ví dụ:  GetAllDocsInCourseById("`5958158015004672`")

Bước 3: Chạy với file python
```bash
python document.py
```
#### 2. Lấy video từ ID khoá học:
Thực hiện các bước như ở mục trên.

Riêng ở video khoá học thì cần phải có phần mềm để chuyển đổi từ `m3u8` sang `mp4`

Ví dụ: VLC, FFMPEG,... hoặc các trang web có bộ chuyển đổi.

