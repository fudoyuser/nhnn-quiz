#!/usr/bin/env python3
"""Lượt 3: cân độ dài phương án cho các câu mới bổ sung."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
P = {"vbhn117": {
75:(1,"Không, vì đơn vị đã từng bị xử phạt vi phạm hành chính về kinh doanh vàng thì không được cấp Giấy phép sản xuất vàng miếng"),
77:(2,"Chưa, vì doanh nghiệp xin kinh doanh mua, bán vàng miếng phải có vốn điều lệ từ 1.000 tỷ đồng"),
78:(3,"Chỉ giao dịch buổi chiều phải chuyển khoản, vì chính giao dịch này làm tổng giá trị trong ngày vượt ngưỡng 05 triệu đồng"),
79:(1,"Có, phải có Giấy chứng nhận đủ điều kiện sản xuất vàng trang sức, mỹ nghệ do NHNN cấp và đăng ký lại với cơ quan đăng ký kinh doanh"),
80:(1,"Có, vì sản phẩm đã qua gia công, chế tác hoàn chỉnh để phục vụ nhu cầu trang sức"),
81:(1,"Công ty phải có Giấy phép kinh doanh mua, bán vàng miếng, vốn điều lệ từ 100 tỷ đồng và mạng lưới từ 3 tỉnh"),
82:(1,"Giấy phép nhập khẩu từng lần do NHNN cấp, nằm trong hạn mức nhập khẩu vàng nguyên liệu hằng năm"),
83:(1,"Bán lẻ cho cá nhân có nhu cầu tích trữ vàng nguyên liệu dạng thỏi"),
85:(1,"Được, nếu mỗi đại lý đăng ký và được NHNN chấp thuận bằng văn bản trước"),
88:(1,"Hợp pháp, vì hai bên tự nguyện thỏa thuận trao đổi tài sản"),
89:(1,"Bộ Công Thương (Quản lý thị trường)"),
93:(1,"Có từ Nghị định 24/2012, sau đó được Nghị định 232/2025 sửa đổi lại mức ngưỡng"),
99:(1,"Cho phép ngân hàng thương mại được sản xuất vàng miếng lần đầu tiên kể từ năm 2012"),
112:(1,"Kinh nghiệm từ 2 năm và không bị xử phạt hành chính về kinh doanh vàng trong 2 năm gần nhất"),
113:(3,"Tỷ lệ tối thiểu số vàng nguyên liệu nhập khẩu phải được dùng để sản xuất vàng miếng"),
114:(2,"05 triệu: mức phạt tối thiểu; 500 triệu: mức phạt tối đa đối với hành vi kinh doanh mua, bán vàng miếng không có giấy phép"),
117:(1,"Sản xuất vàng miếng của ngân hàng thương mại có vốn điều lệ từ 50.000 tỷ đồng trở lên"),
120:(2,"Ký quy chế phối hợp hằng năm do NHNN chủ trì soạn thảo, trình Thủ tướng phê duyệt"),
121:(2,"Biến động vốn điều lệ, cơ cấu cổ đông và danh sách khách hàng mua vàng trang sức trong nước"),
122:(3,"Kiểm toán Nhà nước, phối hợp NHNN"),
123:(1,"Cấp giấy phép mang vàng khi xuất cảnh, nhập cảnh vượt mức quy định cho cá nhân tại cửa khẩu"),
},"vbhn118": {
99:(1,"Lập biên bản tại chỗ và giao ngay bao tiền đó sang Tổ 2 để kiểm đếm tờ (miếng), xử lý thừa thiếu"),
100:(3,"Rút tờ tiền giả ra, thay bằng tờ tiền lấy từ quỹ tạm ứng rồi đóng bó, niêm phong mới, cuối ngày báo cáo Tổ trưởng Tổ 2"),
101:(1,"Kiểm ngân được ở lại phòng để trông giữ bó tiền đang đếm dở; Tổ trưởng khóa cửa ngoài, niêm phong và giữ chìa khóa đến hết giờ nghỉ"),
102:(1,"Tiêu hủy luôn cùng bó tiền đang kiểm đếm để bảo đảm khớp số tờ ghi trên niêm phong, có xác nhận của Hội đồng giám sát"),
103:(2,"Có văn bản cử đi công tác của Vụ Pháp chế và có công chức giám sát của Hội đồng giám sát đi cùng suốt thời gian khảo sát"),
104:(1,"Để lại trong phòng cắt hủy đã khóa, niêm phong cửa có chữ ký của Tổ trưởng Tổ 3 và công chức giám sát, hôm sau tiếp tục cắt hủy"),
106:(1,"Bồi thường 100% giá trị tài sản thiếu và bị kỷ luật cảnh cáo nếu là vi phạm lần đầu, tái phạm thì buộc thôi việc"),
109:(1,"Có, vì ông P là ủy viên Hội đồng tiêu hủy nên đủ điều kiện được Phó Chủ tịch ủy quyền kiểm kê"),
116:(3,"Nghị định 16/2017/NĐ-CP, được sửa đổi, bổ sung bởi Nghị định 26/2025/NĐ-CP"),
117:(2,"Bỏ Cụm tiêu hủy phía Nam, tập trung toàn bộ công tác tiêu hủy tại Cục Phát hành và Kho quỹ ở Hà Nội"),
131:(2,"Thời hạn gửi biên bản thừa, thiếu cho NHNN chi nhánh Khu vực, Sở Giao dịch NHNN kể từ ngày kiểm đếm"),
136:(3,"Quyết định thành viên tham gia quản lý kho tiền tiêu hủy và cử người thay thế khi thành viên nghỉ làm việc"),
137:(1,"Vụ Tài chính - Kế toán và Thanh tra NHNN"),
138:(2,"Chủ tịch Hội đồng giám sát tiêu hủy tiền"),
139:(1,"Quy chế riêng do Chủ tịch Hội đồng tiêu hủy ban hành cho từng đợt tiêu hủy, có ý kiến của Hội đồng giám sát"),
140:(1,"Lập lệnh điều chuyển gửi Cục Phát hành và Kho quỹ và Vụ Tài chính - Kế toán"),
141:(2,"Sổ theo dõi tiền thừa, thiếu, sổ theo dõi tạm ứng của Tổ 2 và sổ theo dõi tiền giả phát hiện qua kiểm đếm"),
143:(3,"Quy chế khen thưởng do Hội đồng tiêu hủy ban hành cho mỗi đợt tiêu hủy tiền"),
144:(2,"Chánh Thanh tra NHNN và Chủ tịch Hội đồng giám sát"),
}}
for doc, patches in P.items():
    p = ROOT / "data" / f"{doc}.json"; D = json.loads(p.read_text("utf-8"))
    for i,(j,t) in patches.items():
        o = D["qs"][i]["o"]
        if t in o: continue
        o[j] = t
        assert len(t) > len(o[0]), (doc, i, len(t), len(o[0]))
    p.write_text(json.dumps(D, ensure_ascii=False, indent=1), "utf-8")
    print(doc, len(patches))
