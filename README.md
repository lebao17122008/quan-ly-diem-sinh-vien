# 🎓 Quản lý điểm sinh viên

Ứng dụng web được xây dựng bằng Python và Streamlit, hỗ trợ xem bảng điểm, tra cứu kết quả học tập và trực quan hóa điểm tổng kết của 10 sinh viên.

Dự án thực hiện theo yêu cầu bài thực hành **Quản lý điểm sinh viên và tạo Web App**.

## Tác giả

- **Họ và tên:** Lê Duy Bảo
- **MSSV:** 052208007506

## Chức năng

- Hiển thị bảng điểm gồm họ tên, chuyên cần, giữa kỳ, cuối kỳ, tổng kết và xếp loại.
- Tính điểm trung bình của lớp.
- Hiển thị sinh viên có điểm tổng kết cao nhất và thấp nhất, bao gồm các trường hợp đồng điểm.
- Đếm số sinh viên đạt và tính tỷ lệ đạt.
- Tra cứu điểm từng sinh viên bằng danh sách chọn.
- Vẽ biểu đồ cột bằng Matplotlib, sử dụng màu sắc tương ứng với từng mức xếp loại.
- Tải bảng điểm dưới dạng CSV.
- Hiển thị thông tin người thực hiện ở cuối trang.

## Công thức tính điểm

```text
Điểm tổng kết = 0.2 × Chuyên cần
              + 0.3 × Giữa kỳ
              + 0.5 × Cuối kỳ
```

Điểm tổng kết được giữ nguyên để tính toán và xếp loại; giao diện hiển thị hai chữ số thập phân.

| Điểm tổng kết | Xếp loại |
|---|---|
| Từ 8.5 trở lên | Giỏi |
| Từ 7.0 đến dưới 8.5 | Khá |
| Từ 5.0 đến dưới 7.0 | Trung bình |
| Dưới 5.0 | Yếu |

Sinh viên được tính là **đạt** khi điểm tổng kết từ **5.0** trở lên.

## Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| Python | Xử lý dữ liệu và xây dựng ứng dụng |
| Pandas | Quản lý bảng điểm và tính thống kê |
| Matplotlib | Vẽ biểu đồ |
| Streamlit | Xây dựng giao diện web |
| GitHub | Lưu trữ mã nguồn |
| Streamlit Community Cloud | Triển khai ứng dụng |

## Cấu trúc dự án

```text
quan-ly-diem-sinh-vien/
├── app.py              # Ứng dụng Streamlit
├── requirements.txt    # Các thư viện cần cài đặt
└── README.md           # Giới thiệu và hướng dẫn
```

## Chạy trên máy tính

Máy tính cần có Python và pip.

Tải mã nguồn, mở terminal tại thư mục dự án rồi chạy:

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Mở địa chỉ được hiển thị trong terminal để sử dụng ứng dụng.

## Triển khai trên Streamlit Community Cloud

1. Đưa `app.py` và `requirements.txt` lên GitHub.
2. Đăng nhập tại https://share.streamlit.io/.
3. Chọn **Create app**.
4. Chọn repository và nhánh chứa mã nguồn.
5. Đặt đường dẫn file chạy là `app.py`.
6. Chọn **Deploy**.

Sau khi triển khai thành công, bổ sung đường dẫn ứng dụng vào README này.
## Kết quả đối chiếu với dữ liệu mẫu

| Chỉ số | Giá trị |
|---|---|
| Tổng số sinh viên | 10 |
| Điểm trung bình lớp | 6.55 |
| Số sinh viên đạt | 7 |
| Tỷ lệ đạt | 70% |
| Sinh viên cao nhất | Hoàng Thị Hà — 9.70 |
| Sinh viên thấp nhất | Ngô Văn Phúc — 3.30 |

## Phạm vi dữ liệu

Ứng dụng sử dụng dữ liệu mẫu cố định phục vụ bài thực hành. Chức năng tải CSV xuất bảng điểm hiện có; ứng dụng chưa có chức năng nhập hoặc chỉnh sửa điểm.

## Hồ sơ bài thực hành

- Notebook Google Colab: `TenSTT_pythonproject`.
- Báo cáo PDF: `TenSTT_pythonproject.pdf`.
- Đường dẫn web app Streamlit có thể truy cập.

Thay `TenSTT` theo quy định đặt tên của lớp.
