# Hệ Thống Tự Động Kiểm Tra Vi Phạm Giao Thông

Dự án này là một công cụ tự động kiểm tra thông tin vi phạm giao thông thông qua website [CSGT.vn](https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html). Chương trình sẽ tự động nhập biển số xe, loại phương tiện và giải mã CAPTCHA để tra cứu thông tin vi phạm.

## Tính năng

- Tự động điền thông tin biển kiểm soát
- Tự động chọn loại phương tiện (mặc định là xe máy)
- Tự động xử lý và giải mã CAPTCHA
- Lên lịch kiểm tra hàng ngày (mặc định lúc 6:00 sáng và 17:46 chiều)
- Hiển thị kết quả tra cứu

## Yêu cầu hệ thống

- Python 3.6 hoặc cao hơn
- Google Chrome
- ChromeDriver tương thích với phiên bản Chrome đang sử dụng
- Tesseract OCR

## Cài đặt

### Bước 1: Cài đặt Python

Nếu chưa có Python, tải và cài đặt từ [python.org](https://www.python.org/downloads/).

### Bước 2: Cài đặt Tesseract OCR

1. **Windows**:
   - Tải Tesseract OCR từ [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Cài đặt và đảm bảo thêm Tesseract vào biến môi trường PATH
   - Đường dẫn mặc định thường là: `C:\Program Files\Tesseract-OCR`

2. **macOS**:
   ```
   brew install tesseract
   ```

3. **Linux**:
   ```
   sudo apt install tesseract-ocr
   ```

### Bước 3: Cài đặt ChromeDriver

1. Kiểm tra phiên bản Chrome của bạn (Menu > Trợ giúp > Giới thiệu về Google Chrome)
2. Tải ChromeDriver tương ứng từ [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
3. Giải nén và đặt tệp chromedriver vào một thư mục trong PATH

### Bước 4: Cài đặt các thư viện Python

Cài đặt các thư viện cần thiết bằng pip:

```
pip install -r requirements.txt
```

## Cách sử dụng

1. Chỉnh sửa thông tin biển kiểm soát trong file `kiemtra.py` (biến `value_bienkiensat`)
2. Chạy chương trình:
   ```
   python kiemtra.py
   ```
3. Chương trình sẽ tự động chạy theo lịch đã cài đặt (6:00 sáng và 17:46 chiều hàng ngày)

## Tùy chỉnh lịch chạy

Để thay đổi lịch chạy, chỉnh sửa các dòng sau trong file `kiemtra.py`:

```python
schedule.every().day.at("06:00").do(run_task)  # Chạy lúc 6h sáng
schedule.every().day.at("17:46").do(run_task)  # Chạy lúc 5h46 chiều
```

## Ghi chú

- Tỷ lệ nhận dạng CAPTCHA có thể không hoàn hảo. Nếu cần độ chính xác cao hơn, bạn có thể cải thiện phần xử lý hình ảnh hoặc sử dụng các dịch vụ giải CAPTCHA chuyên nghiệp.
- Nếu website thay đổi cấu trúc, bạn có thể cần cập nhật các selector trong mã nguồn.

## Giấy phép

MIT License