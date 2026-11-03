# Quiz Văn bản NHNN

Website trắc nghiệm và phản biện, ôn tập văn bản quy phạm pháp luật và văn bản chỉ đạo của Ngân hàng Nhà nước Việt Nam. Mỗi đáp án kèm trích dẫn Điều, Khoản và nguyên văn quy định.

Xem trực tuyến: https://fudoyuser.github.io/nhnn-quiz/

## Văn bản hiện có

| Số hiệu | Nội dung | Số câu |
|---|---|---|
| 117/2026/VBHN-NĐ-NHNN | Nghị định về quản lý hoạt động kinh doanh vàng (hợp nhất NĐ 24/2012, NĐ 232/2025, NĐ 390/2026) | 130 |
| 118/2026/VBHN-TT-NHNN | Thông tư quy định về tiêu hủy tiền của NHNN (hợp nhất TT 03/2020 và TT 42/2026) | 153 |

## Dạng câu hỏi

| Mức độ | Dạng | Mã `ty` |
|---|---|---|
| Ghi nhớ | Ghi nhớ quy định | `nho` |
| Ghi nhớ | Phân biệt con số dễ nhầm | `so` |
| Ghi nhớ | So sánh trước/sau sửa đổi | `ss` |
| Vận dụng | Tình huống (`sc` là đoạn tình huống) | `th` |
| Vận dụng | Nhiều nhận định (`st` là danh sách nhận định) | `nd` |
| Vận dụng | Sắp xếp quy trình (`k: "order"`, `items` theo đúng thứ tự) | `order` |
| Vận dụng | Nối cặp (`k: "match"`, `pairs` là các cặp đúng) | `match` |
| Phân tích | Phản biện | `pb` |

Câu trắc nghiệm có `o[0]` là đáp án đúng; thứ tự được xáo khi hiển thị. Phương án nhiễu được viết dài tương đương đáp án đúng để không đoán được bằng độ dài.

## Tính năng

- Lọc theo phạm vi (chương, điểm sửa đổi), mức độ và dạng câu hỏi.
- Chế độ Luyện tập, Thi thử (20 câu, 15 phút, không gồm câu phản biện), Ôn câu sai.
- Thẻ **Phản biện** cho từng văn bản: điểm hợp lý, cần làm rõ, bất cập, hướng hoàn thiện và câu hỏi thảo luận.
- Lưu điểm và câu sai trong trình duyệt (localStorage).

## Cấu trúc và build

```
data/<id>.json   dữ liệu từng văn bản: thông tin, chương, câu hỏi (qs), phản biện (crit)
src/             head.html, body.html, app.js
build.py         kiểm tra dữ liệu và ghép thành index.html
tools/           các script một lần dùng để bổ sung, chỉnh sửa câu hỏi
```

```bash
python3 build.py
```

Thêm văn bản mới: tạo `data/<id>.json` theo cấu trúc hiện có, thêm `<id>` vào `ORDER` trong `build.py`, rồi build lại. Câu hỏi mới nối vào cuối mảng `qs` để không làm lệch danh sách câu sai đã lưu trong trình duyệt người dùng.

> Văn bản hợp nhất dùng để tra cứu. Khi áp dụng, đối chiếu với văn bản gốc. Phần phản biện là phân tích học thuật, không phải quan điểm chính thức của NHNN.
