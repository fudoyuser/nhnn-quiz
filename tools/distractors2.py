#!/usr/bin/env python3
"""Lượt 2: kéo dài một phương án nhiễu để đáp án đúng không còn là phương án dài nhất."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
P = {"vbhn117": {
10:(2,"Khai thác, tinh luyện vàng của doanh nghiệp và chế tác vàng trang sức, mỹ nghệ"),
18:(1,"Có, phải có Giấy chứng nhận đủ điều kiện sản xuất do NHNN cấp trước khi hoạt động"),
32:(3,"Được, nếu có văn bản cam kết không tái phạm và được Thanh tra Chính phủ xác nhận đã nộp đủ tiền phạt"),
39:(2,"Hạn mức hằng năm do NHNN cấp, phân bổ theo quy mô vốn điều lệ và năng lực sản xuất của doanh nghiệp"),
42:(2,"Không phải làm thủ tục hải quan, không chịu thuế giá trị gia tăng và thuế thu nhập doanh nghiệp"),
44:(1,"Có vốn điều lệ từ 1.000 tỷ đồng, có Giấy phép sản xuất vàng miếng do NHNN cấp còn hiệu lực và hạn mức nhập khẩu"),
53:(1,"Giá vàng thế giới quy đổi theo tỷ giá trung tâm, cập nhật hằng ngày làm căn cứ tham chiếu cho thị trường"),
55:(1,"Bộ Công Thương, phối hợp với Ngân hàng Nhà nước"),
56:(1,"Cấp Giấy phép sản xuất vàng miếng và phân bổ hạn mức nhập khẩu vàng nguyên liệu hằng năm cho doanh nghiệp"),
66:(2,"Hạn mức được chia đều cho mọi doanh nghiệp được cấp phép, không tính đến năng lực sản xuất và nhu cầu thực tế"),
68:(3,"Ngưỡng mâu thuẫn với nghĩa vụ niêm yết giá công khai và nghĩa vụ lập hóa đơn của doanh nghiệp kinh doanh vàng"),
70:(1,"Giao toàn bộ thẩm quyền thanh tra kinh doanh vàng cho Bộ Công an và Thanh tra Chính phủ, NHNN chỉ phối hợp khi được yêu cầu"),
71:(1,"Doanh nghiệp không thể nhập khẩu vàng nguyên liệu để sản xuất vàng miếng vì không xác định được hàm lượng"),
72:(1,"Vì Điều 11 đã bị Nghị định 390/2026 bãi bỏ toàn bộ nhưng văn bản hợp nhất chưa thể hiện chú thích bãi bỏ"),
73:(2,"Vì toàn bộ vàng trang sức đã chuyển sang do NHNN trực tiếp quản lý sản xuất và phân phối qua ngân hàng thương mại"),
74:(3,"Hoạt động này do Bộ Công Thương cấp phép theo pháp luật về sở giao dịch hàng hóa, NHNN chỉ quản lý thanh toán ký quỹ"),
},"vbhn118": {
4:(2,"Vụ trưởng Vụ Pháp chế (TL. Thống đốc), theo ủy quyền"),
5:(3,"Ngân hàng Nhà nước chi nhánh vùng kinh tế trọng điểm"),
8:(2,"Vụ trưởng Vụ Tài chính - Kế toán, sau khi thống nhất với Cục"),
11:(1,"NHNN chi nhánh Khu vực tại TP. Hồ Chí Minh, cạnh Kho tiền Trung ương"),
17:(2,"Hệ thống máy cắt hủy tiền giấy chuyên dùng, có bộ phận nghiền riêng"),
19:(1,"Một Phó Thống đốc NHNN phụ trách công tác phát hành và kho quỹ"),
23:(3,"4 (một thư ký tại mỗi tổ chuyên trách của Cụm phía Bắc)"),
26:(2,"Thống đốc NHNN, theo đề nghị của Cục Phát hành và Kho quỹ"),
30:(3,"Bó (túi) do Hội đồng giám sát chỉ định ngẫu nhiên khi giao nhận, theo tỷ lệ cố định 10%"),
41:(1,"Vụ Tài chính - Kế toán, theo lệnh điều chuyển của Cục Phát hành và Kho quỹ"),
42:(1,"Vụ Tài chính - Kế toán, theo đề nghị của Hội đồng tiêu hủy"),
58:(1,"Theo từng kiểm ngân và từng ca làm việc, có xác nhận của Tổ trưởng Tổ 2 và công chức giám sát"),
71:(2,"Hội đồng giám sát, để thẩm định trước khi trình Thống đốc"),
75:(1,"Vụ Tài chính - Kế toán, để hạch toán và lưu hồ sơ"),
79:(1,"Vụ Kiểm toán nội bộ, phối hợp với Cục Phát hành và Kho quỹ"),
80:(1,"Vụ Tài chính - Kế toán, sau khi có ý kiến Hội đồng giám sát"),
81:(3,"Vụ Tài chính - Kế toán, phối hợp với Vụ Tổ chức cán bộ"),
84:(1,"Thống đốc trực tiếp điều hành mọi tổ chuyên trách mà không qua Hội đồng tiêu hủy và Hội đồng giám sát"),
86:(1,"Hội đồng tiêu hủy buộc phải kiểm đếm lại toàn bộ số tiền đã cắt hủy trong năm trước để đối chiếu số liệu"),
88:(2,"Phế liệu phải được lưu kho vĩnh viễn tại Kho tiền Trung ương để phục vụ thanh tra, kiểm toán sau tiêu hủy"),
89:(2,"Biên bản giao nhận và sổ theo dõi giao nhận nội bộ giữa các tổ chuyên trách, có ký nhận đầy đủ"),
90:(1,"Tiền phải được cắt hủy ngay trong ngày nhận nên không đủ thời gian kiểm đếm theo tỷ lệ đã được phê duyệt"),
92:(1,"Vì cho phép bỏ qua hoàn toàn việc kiểm đếm đối với các loại tiền có mệnh giá nhỏ và tiền kim loại"),
94:(1,"Khiến Thông tư không có hiệu lực cho đến khi toàn bộ văn bản hướng dẫn được đăng Công báo và Cổng thông tin"),
}}
for doc, patches in P.items():
    p = ROOT / "data" / f"{doc}.json"; D = json.loads(p.read_text("utf-8"))
    for i,(j,t) in patches.items():
        o = D["qs"][i]["o"]; assert 1 <= j <= 3 and t not in o; o[j] = t
        assert len(t) > len(o[0]), (doc, i, len(t), len(o[0]))
    p.write_text(json.dumps(D, ensure_ascii=False, indent=1), "utf-8")
    print(doc, len(patches))
