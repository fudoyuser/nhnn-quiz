# Quiz Văn bản NHNN

Website trắc nghiệm ôn tập văn bản quy phạm pháp luật và văn bản chỉ đạo của Ngân hàng Nhà nước Việt Nam. Mỗi đáp án kèm trích dẫn Điều, Khoản và nguyên văn quy định.

## Văn bản hiện có

| Số hiệu | Nội dung | Số câu |
|---|---|---|
| 118/2026/VBHN-TT-NHNN | Thông tư quy định về tiêu hủy tiền của NHNN (hợp nhất TT 03/2020 và TT 42/2026) | 84 |

## Tính năng

- Lọc câu hỏi theo chương hoặc theo các điểm sửa đổi bởi Thông tư 42/2026.
- Ba chế độ: Luyện tập (xem đáp án ngay), Thi thử (20 câu, 15 phút, đạt từ 80%), Ôn câu sai.
- Lưu điểm và câu sai trong trình duyệt (localStorage).

## Chạy

Một file tĩnh `index.html`, không cần build. Mở trực tiếp trong trình duyệt hoặc bật GitHub Pages (Settings → Pages → Deploy from branch `main`, thư mục `/`).

## Thêm văn bản mới

Thêm một phần tử vào mảng `DOCS` trong `index.html`, gồm `no`, `title`, `date`, `signer`, `chain`, `chapters` và `qs`. Trong mỗi câu hỏi, `o[0]` là đáp án đúng (thứ tự được xáo khi hiển thị), `c` là căn cứ, `ex` là trích dẫn, `am: 1` đánh dấu nội dung sửa đổi.

> Văn bản hợp nhất dùng để tra cứu. Khi áp dụng, đối chiếu với văn bản gốc.
