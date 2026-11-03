#!/usr/bin/env python3
"""Một lần: viết lại phương án (o[0] vẫn là đáp án đúng) để độ dài các phương án tương đương.
Khóa là chỉ số câu trong data/<doc>.json; kiểm tra câu hỏi khớp tiền tố để tránh sửa nhầm."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent

P = {
"vbhn117": {
5: ("Theo Nghị định 232/2025, Công ty SJC", [
 "Vàng miếng SJC do chính Công ty SJC sản xuất trước ngày NĐ có hiệu lực, bị trầy xước hoặc bị đóng thêm ký hiệu lạ",
 "Vàng miếng của mọi thương hiệu trong nước bị trầy xước, nếu khách hàng đề nghị và có hóa đơn mua hợp lệ",
 "Vàng miếng SJC sản xuất sau ngày NĐ có hiệu lực, khi bị lỗi kỹ thuật được phát hiện trong quá trình lưu thông",
 "Vàng nguyên liệu nhập khẩu có hàm lượng từ 99,5% trở lên, để chuyển thành vàng miếng mang thương hiệu SJC"]),
6: ("Từ ngày Nghị định 390/2026 có hiệu lực, Giấy chứng nhận", [
 "Không còn là điều kiện để thực hiện hoạt động sản xuất vàng trang sức, mỹ nghệ",
 "Tiếp tục có hiệu lực đến hết thời hạn ghi trên Giấy chứng nhận, sau đó phải cấp lại",
 "Được chuyển đổi tự động thành Giấy phép sản xuất vàng miếng nếu đủ vốn điều lệ",
 "Hết hiệu lực, cơ sở phải ngừng sản xuất cho đến khi được Bộ Công Thương cấp phép"]),
7: ("Hồ sơ đề nghị cấp Giấy chứng nhận đủ điều kiện", [
 "NHNN chấm dứt việc giải quyết và thông báo cho người nộp hồ sơ",
 "NHNN tiếp tục giải quyết theo quy định trước ngày NĐ có hiệu lực",
 "NHNN chuyển hồ sơ sang Bộ Công Thương để tiếp tục giải quyết",
 "Hồ sơ được coi là đã chấp thuận, NHNN cấp Giấy chứng nhận ngay"]),
8: ("Giấy phép xuất khẩu, nhập khẩu vàng và hạn mức", [
 "Tiếp tục thực hiện theo nội dung, thời hạn ghi tại giấy phép, hạn mức, trừ khi bị điều chỉnh, thu hồi",
 "Hết hiệu lực từ ngày 16/10/2026, đơn vị phải nộp hồ sơ xin cấp mới theo quy định của Nghị định 390",
 "Tiếp tục thực hiện nhưng phải làm thủ tục xác nhận lại với NHNN trong thời hạn 12 tháng",
 "Được tự động gia hạn thêm 01 năm kể từ ngày hết hạn ghi trên giấy phép hoặc văn bản cấp hạn mức"]),
9: ("Nghị định về quản lý hoạt động kinh doanh vàng KHÔNG", [
 "Khai thác và tinh luyện vàng của doanh nghiệp khai thác vàng",
 "Sản xuất vàng miếng của ngân hàng thương mại được cấp phép",
 "Kinh doanh vàng trên tài khoản và hoạt động phái sinh về vàng",
 "Xuất khẩu, nhập khẩu vàng nguyên liệu của doanh nghiệp"]),
10: ("Phạm vi điều chỉnh nêu rõ", [
 "Kinh doanh vàng trên tài khoản và hoạt động phái sinh về vàng",
 "Cầm đồ bằng vàng và cho vay, huy động vốn bằng vàng",
 "Khai thác, tinh luyện vàng và chế tác vàng trang sức",
 "Ký gửi vàng và mua bán vàng qua đại lý ủy nhiệm"]),
12: ("Theo định nghĩa sau sửa đổi, vàng miếng có ký mã hiệu", [
 "Doanh nghiệp và ngân hàng thương mại được NHNN cho phép sản xuất",
 "Riêng Công ty SJC, là thương hiệu vàng miếng quốc gia duy nhất",
 "Mọi doanh nghiệp có Giấy phép kinh doanh mua, bán vàng miếng",
 "Tổ chức tín dụng có vốn điều lệ từ 3.000 tỷ đồng trở lên"]),
13: ("Vàng nguyên liệu được định nghĩa", [
 "Vàng dưới dạng khối, thỏi, hạt, miếng và các loại vàng khác",
 "Vàng có hàm lượng từ 99,99% trở lên, chưa qua gia công chế tác",
 "Vàng chưa qua tinh luyện, được khai thác trực tiếp tại mỏ vàng",
 "Vàng trang sức dạng bán thành phẩm và vàng dưới dạng muối vàng"]),
14: ("Hoạt động kinh doanh vàng trên tài khoản được hiểu", [
 "Kinh doanh vàng qua tài khoản, giao dịch ký quỹ, giá trị ròng định giá lại liên tục theo giá vàng",
 "Gửi vàng vào tài khoản tiết kiệm tại ngân hàng, hưởng lãi theo giá trị vàng tại ngày đáo hạn",
 "Mua bán vàng miếng qua ứng dụng ngân hàng, có giao nhận vàng vật chất tại quầy giao dịch",
 "Thanh toán mua bán vàng bằng chuyển khoản qua tài khoản thanh toán của khách hàng"]),
16: ("Sau sửa đổi bởi NĐ 390/2026, quản lý hoạt động kinh doanh vàng", [
 "Phát triển ổn định và bền vững thị trường vàng",
 "Chống vàng hóa nền kinh tế và ổn định tỷ giá",
 "Huy động nguồn lực vàng trong dân vào sản xuất",
 "Tăng quy mô dự trữ ngoại hối nhà nước bằng vàng"]),
17: ("Hoạt động sản xuất vàng miếng, kinh doanh mua, bán vàng miếng", [
 "Kinh doanh có điều kiện, phải được NHNN cấp Giấy phép",
 "Độc quyền nhà nước, chỉ NHNN được tổ chức thực hiện",
 "Kinh doanh tự do, chỉ cần Giấy chứng nhận đăng ký doanh nghiệp",
 "Thuộc danh mục hạn chế kinh doanh, cần Thủ tướng cho phép"]),
20: ("Tổ chức, cá nhân chỉ được thực hiện", [
 "Sau khi được Thủ tướng Chính phủ cho phép và NHNN cấp Giấy phép",
 "Sau khi được NHNN cấp Giấy phép, không cần ý kiến Thủ tướng",
 "Sau khi đăng ký với Bộ Công Thương và được NHNN chấp thuận",
 "Sau khi có Giấy chứng nhận đăng ký doanh nghiệp phù hợp"]),
22: ("Hoạt động mua, bán vàng miếng của tổ chức, cá nhân chỉ", [
 "Tổ chức tín dụng và doanh nghiệp được NHNN cấp Giấy phép kinh doanh mua, bán vàng miếng",
 "Mọi cửa hàng vàng bạc có Giấy chứng nhận đăng ký doanh nghiệp và niêm yết giá công khai",
 "Doanh nghiệp có Giấy phép sản xuất vàng miếng, kể cả khi chưa có Giấy phép kinh doanh mua, bán",
 "Sàn giao dịch vàng do NHNN tổ chức và các đại lý ủy nhiệm của tổ chức tín dụng"]),
25: ("Điều kiện về số thuế đã nộp", [
 "Từ 500 triệu đồng/năm trở lên trong 2 năm liên tiếp gần nhất, có xác nhận cơ quan thuế",
 "Từ 1 tỷ đồng/năm trở lên trong 3 năm liên tiếp gần nhất, có xác nhận cơ quan thuế",
 "Từ 500 triệu đồng trở lên trong năm gần nhất, có báo cáo tài chính đã kiểm toán",
 "Từ 200 triệu đồng/năm trở lên trong 2 năm liên tiếp gần nhất, có xác nhận cơ quan thuế"]),
32: ("Đơn vị từng bị xử phạt vi phạm hành chính", [
 "Được, nếu đã khắc phục xong hậu quả và thực hiện các kiến nghị có thời hạn của thanh tra, kiểm tra",
 "Không, đơn vị từng bị xử phạt về kinh doanh vàng thì không đủ điều kiện được cấp Giấy phép",
 "Được, nhưng chỉ sau 05 năm kể từ ngày chấp hành xong quyết định xử phạt vi phạm hành chính",
 "Được, nếu có văn bản cam kết không tái phạm và được Thanh tra Chính phủ xác nhận"]),
36: ("Đơn vị kinh doanh mua, bán vàng miếng phải niêm yết", [
 "Tại địa điểm giao dịch hoặc trên trang thông tin điện tử, và kết nối giá niêm yết cho NHNN",
 "Chỉ trên trang thông tin điện tử của NHNN, đơn vị không được tự niêm yết tại quầy",
 "Tại trụ sở chính và gửi bảng giá cho Sở Công Thương nơi đặt trụ sở trước 9 giờ hằng ngày",
 "Tại địa điểm giao dịch, và đăng ký trước với NHNN khung giá mua bán trong tháng"]),
37: ("Hệ thống thông tin lưu trữ dữ liệu giao dịch", [
 "Thông tin căn cước (cá nhân), mã số thuế (doanh nghiệp), khối lượng và giá trị giao dịch",
 "Số hóa đơn, tổng giá trị giao dịch trong ngày và số dư tài khoản thanh toán của khách hàng",
 "Họ tên, số điện thoại, địa chỉ email và nguồn gốc tiền mua vàng của khách hàng",
 "Nghề nghiệp, thu nhập bình quân và mục đích mua vàng của từng khách hàng"]),
38: ("Hệ thống thông tin dữ liệu vàng miếng được sản xuất", [
 "Thông tin nguyên liệu đầu vào, thời gian sản xuất, sản phẩm đầu ra",
 "Danh sách khách hàng mua vàng miếng và giá bán theo từng lô sản xuất",
 "Giá thành, lợi nhuận và số thuế phải nộp của từng lô sản xuất",
 "Số lượng nhân công, công suất máy móc và định mức hao hụt"]),
39: ("Xuất khẩu, nhập khẩu vàng trang sức, mỹ nghệ được thực hiện", [
 "Giấy chứng nhận đăng ký kinh doanh hoặc Giấy chứng nhận đăng ký doanh nghiệp",
 "Giấy phép từng lần do NHNN cấp cho mỗi lô hàng xuất khẩu, nhập khẩu",
 "Hạn mức hằng năm do NHNN cấp theo quy mô vốn điều lệ của doanh nghiệp",
 "Quyết định của Thủ tướng Chính phủ cho phép từng doanh nghiệp cụ thể"]),
40: ("NHNN cấp hạn mức hằng năm và Giấy phép từng lần", [
 "Doanh nghiệp, ngân hàng thương mại được cấp Giấy phép sản xuất vàng miếng",
 "Mọi doanh nghiệp, tổ chức tín dụng có Giấy phép kinh doanh mua, bán vàng miếng",
 "Tổ chức tín dụng có vốn điều lệ từ 3.000 tỷ đồng và mạng lưới từ 5 tỉnh",
 "Doanh nghiệp có vốn đầu tư nước ngoài có đăng ký sản xuất vàng trang sức"]),
42: ("Hoạt động xuất khẩu, nhập khẩu vàng nguyên liệu của NHNN", [
 "Miễn thuế xuất khẩu, thuế nhập khẩu theo quyết định của Thủ tướng Chính phủ",
 "Giảm 50% thuế nhập khẩu theo quyết định của Bộ trưởng Bộ Tài chính",
 "Không phải làm thủ tục hải quan và không chịu thuế giá trị gia tăng",
 "Không có ưu đãi riêng, nộp thuế như doanh nghiệp được cấp phép"]),
43: ("Giấy phép xuất khẩu vàng nguyên liệu do doanh nghiệp khai thác", [
 "Doanh nghiệp có vốn đầu tư nước ngoài có Giấy phép khai thác vàng, vàng khai thác trong nước",
 "Mọi doanh nghiệp khai thác vàng trong nước, kể cả doanh nghiệp không có vốn nước ngoài",
 "Doanh nghiệp đầu tư khai thác vàng ở nước ngoài, với vàng được phân chia theo thỏa thuận",
 "Ngân hàng thương mại sản xuất vàng miếng mua vàng từ doanh nghiệp khai thác trong nước"]),
44: ("Doanh nghiệp đầu tư khai thác vàng ở nước ngoài", [
 "Có đăng ký khai thác vàng trong Giấy chứng nhận đầu tư; vàng do mình khai thác hoặc được chia ở nước ngoài",
 "Có vốn điều lệ từ 1.000 tỷ đồng và có Giấy phép sản xuất vàng miếng do NHNN cấp còn hiệu lực",
 "Có Giấy phép kinh doanh mua, bán vàng miếng và có hợp đồng bán lại toàn bộ số vàng cho NHNN",
 "Có Giấy phép khai thác vàng trong nước và có vốn đầu tư nước ngoài từ 51% trở lên"]),
45: ("Vàng nguyên liệu dạng bột, dung dịch", [
 "Giấy chứng nhận đăng ký doanh nghiệp, pháp luật hải quan và pháp luật chuyên ngành",
 "Giấy phép từng lần của NHNN, trong phạm vi hạn mức nhập khẩu vàng nguyên liệu hằng năm",
 "Hạn mức hằng năm do NHNN cấp theo năng lực sản xuất của doanh nghiệp",
 "Quyết định của Thủ tướng Chính phủ và Giấy phép của Bộ Công Thương"]),
46: ("Vàng dùng làm nguyên liệu sản xuất loại sản phẩm nào", [
 "Linh kiện điện tử, thiết bị điện tử, thiết bị y tế, dụng cụ y tế",
 "Vàng miếng của ngân hàng thương mại được cấp Giấy phép sản xuất",
 "Vàng trang sức, mỹ nghệ thành phẩm để bán tại thị trường trong nước",
 "Đồ mỹ nghệ xuất khẩu và vàng miếng phục vụ hội chợ, triển lãm"]),
48: ("Hằng năm, NHNN xem xét cấp Giấy phép nhập khẩu vàng nguyên liệu cho doanh nghiệp có vốn", [
 "Năng lực sản xuất, việc thực hiện hợp đồng gia công/xuất khẩu và báo cáo xuất khẩu năm trước",
 "Vốn điều lệ, số thuế đã nộp trong 2 năm gần nhất và mạng lưới chi nhánh tại Việt Nam",
 "Tổng hạn mức nhập khẩu vàng của cả nước và thứ tự nộp hồ sơ của doanh nghiệp",
 "Giá vàng thế giới năm trước và tỷ lệ sở hữu của nhà đầu tư nước ngoài trong doanh nghiệp"]),
52: ("NHNN cấp hạn mức hằng năm cho từng doanh nghiệp", [
 "Quy mô vốn điều lệ, tình hình xuất nhập khẩu các năm trước và nhu cầu của đơn vị",
 "Thứ tự nộp hồ sơ và số lượng chi nhánh, điểm bán hàng của doanh nghiệp",
 "Thị phần vàng trang sức và số thuế nộp ngân sách của năm trước",
 "Chia đều tổng hạn mức cho các đơn vị được cấp Giấy phép sản xuất vàng miếng"]),
53: ("NHNN đăng tải giá vàng nào", [
 "Giá mua, bán vàng miếng do doanh nghiệp, tổ chức tín dụng được cấp phép cung cấp",
 "Giá vàng thế giới quy đổi theo tỷ giá trung tâm, cập nhật hằng ngày",
 "Giá trần và giá sàn vàng miếng do NHNN tự xác định cho từng tháng",
 "Giá vàng trang sức bình quân do Hiệp hội Kinh doanh vàng tổng hợp"]),
56: ("Bộ Tài chính chủ trì nội dung nào", [
 "Chính sách thuế với kinh doanh vàng; hướng dẫn cấp Giấy chứng nhận đăng ký doanh nghiệp",
 "Cấp Giấy phép sản xuất vàng miếng và hạn mức nhập khẩu vàng nguyên liệu hằng năm",
 "Kiểm định phương tiện đo lường và quản lý chất lượng vàng trong lưu thông",
 "Thanh tra hoạt động sản xuất, kinh doanh vàng trang sức, mỹ nghệ trên cả nước"]),
57: ("Ai chỉ đạo công tác thanh tra, kiểm tra", [
 "Chủ tịch Ủy ban nhân dân tỉnh, thành phố trực thuộc trung ương",
 "Giám đốc NHNN chi nhánh Khu vực nơi có hoạt động kinh doanh vàng",
 "Giám đốc Sở Công Thương, phối hợp với Thanh tra tỉnh",
 "Chánh Thanh tra Chính phủ, thông qua Thanh tra tỉnh"]),
60: ("Nội dung nào thuộc chế độ báo cáo", [
 "Tình hình mua, bán, sử dụng, tồn kho và bán vàng nguyên liệu nhập khẩu",
 "Danh sách khách hàng mua vàng trang sức có giá trị từ 05 triệu đồng",
 "Lương bình quân và số lượng lao động của bộ phận kinh doanh vàng",
 "Kế hoạch mở chi nhánh, điểm bán hàng mới trong năm tiếp theo"]),
62: ("Vì sao phân tích phản biện cho rằng ngưỡng vốn", [
 "Ngưỡng 50.000 tỷ (ngân hàng) và 1.000 tỷ đồng (doanh nghiệp) chỉ ít chủ thể lớn đáp ứng",
 "Nghị định chỉ cho phép một doanh nghiệp nhà nước được sản xuất vàng miếng như trước đây",
 "Vàng miếng của mọi đơn vị sản xuất vẫn bắt buộc phải mang thương hiệu SJC",
 "NHNN đã ngừng cấp Giấy phép sản xuất vàng miếng mới kể từ năm 2025"]),
63: ("Theo phân tích, chỉ tiêu nào nên được theo dõi công khai", [
 "Chênh lệch giá vàng miếng trong nước so với giá thế giới",
 "Số lượng cửa hàng vàng trang sức trên địa bàn cả nước",
 "Tổng vốn điều lệ của các ngân hàng thương mại sản xuất vàng",
 "Số thuế thu được từ hoạt động kinh doanh vàng trang sức"]),
64: ("Mâu thuẫn nào được chỉ ra tại Điều 21", [
 "Vẫn yêu cầu xin Giấy chứng nhận đủ điều kiện sản xuất vàng trang sức, dù NĐ 390 đã bỏ",
 "Quy định ngày hiệu lực của Nghị định sớm hơn ngày ký ban hành văn bản hợp nhất",
 "Cho phép doanh nghiệp kinh doanh vàng miếng thông qua đại lý ủy nhiệm trong 12 tháng",
 "Trái với Điều 112 Luật Các tổ chức tín dụng về hoạt động phái sinh vàng"]),
65: ("Câu “các giấy phép sản xuất vàng miếng hết hiệu lực”", [
 "Dễ bị hiểu là áp dụng cho Giấy phép sản xuất vàng miếng mới cấp theo Điều 11a",
 "Dễ bị hiểu là cấm mọi hoạt động mua bán vàng miếng kể từ ngày Nghị định có hiệu lực",
 "Dễ bị hiểu là bãi bỏ Giấy phép kinh doanh mua, bán vàng miếng của tổ chức tín dụng",
 "Dễ bị hiểu là NHNN không còn được tổ chức sản xuất vàng miếng trong từng thời kỳ"]),
66: ("Vì sao cách phân bổ hạn mức xuất nhập khẩu vàng", [
 "Phân bổ theo vốn điều lệ và lịch sử xuất nhập khẩu, có lợi cho đơn vị lớn, đơn vị đã có mặt",
 "Hạn mức được đấu giá công khai nên chỉ đơn vị trả giá cao nhất mới được phân bổ",
 "Hạn mức được chia đều cho mọi doanh nghiệp, không tính đến năng lực sản xuất thực tế",
 "Nghị định giao Bộ Công Thương phân bổ hạn mức mà không có tiêu chí cụ thể"]),
67: ("Hướng hoàn thiện nào được đề xuất cho cơ chế phân bổ hạn mức", [
 "Công khai tổng hạn mức và kết quả phân bổ; dành một phần cho đơn vị mới được cấp phép",
 "Bỏ hoàn toàn hạn mức nhập khẩu, để doanh nghiệp tự quyết định theo nhu cầu thị trường",
 "Giao Bộ Công Thương phân bổ hạn mức thay cho NHNN để tách bạch quản lý",
 "Chỉ cấp hạn mức cho ngân hàng thương mại nhà nước nhằm bảo đảm an toàn ngoại hối"]),
68: ("Mối lo nào được nêu về ngưỡng 05 triệu", [
 "Ảnh hưởng người cao tuổi, nông thôn; chưa rõ cách kiểm soát giao dịch chia nhỏ qua nhiều cửa hàng",
 "Ngưỡng quá cao so với giá vàng nên không có tác dụng phòng, chống rửa tiền trên thực tế",
 "Ngưỡng chỉ áp dụng cho tổ chức, không áp dụng cho cá nhân mua bán vàng trang sức",
 "Ngưỡng mâu thuẫn với nghĩa vụ niêm yết giá công khai của doanh nghiệp kinh doanh vàng"]),
69: ("Hướng hoàn thiện nào được đề xuất cho ngưỡng thanh toán", [
 "Cân nhắc ngưỡng riêng cho vàng trang sức hoặc điều chỉnh định kỳ theo giá vàng",
 "Bỏ hẳn yêu cầu thanh toán không dùng tiền mặt đối với mọi giao dịch mua bán vàng",
 "Chỉ áp dụng ngưỡng cho giao dịch vàng miếng thực hiện tại ngân hàng thương mại",
 "Nâng ngưỡng lên 1 tỷ đồng và chỉ áp dụng cho khách hàng là doanh nghiệp"]),
70: ("Điểm yếu của cơ chế phối hợp liên ngành tại Điều 18", [
 "Chỉ “căn cứ vào yêu cầu thực tế”, chưa có đầu mối, quy chế chia sẻ dữ liệu, kế hoạch thanh tra chung",
 "Giao toàn bộ thẩm quyền thanh tra kinh doanh vàng cho Bộ Công an và Thanh tra Chính phủ",
 "Loại NHNN khỏi hoạt động thanh tra, kiểm tra đối với doanh nghiệp kinh doanh vàng miếng",
 "Cấm các bộ, ngành chia sẻ thông tin về doanh nghiệp kinh doanh vàng với nhau"]),
71: ("Theo phân tích, việc thiếu tiêu chuẩn quốc gia", [
 "Vàng miếng các thương hiệu khó thay thế cho nhau, khó so sánh giá và mua bán chéo",
 "Doanh nghiệp không thể nhập khẩu vàng nguyên liệu để sản xuất vàng miếng",
 "Ngân hàng thương mại không được cấp Giấy phép sản xuất vàng miếng",
 "Giá vàng trang sức tăng mạnh do thiếu nguồn cung vàng nguyên liệu"]),
72: ("Vì sao tiêu chí mạng lưới", [
 "Giữ nguyên từ năm 2012, trong khi số lượng và quy mô đơn vị hành chính cấp tỉnh đã đổi",
 "Vì Điều 11 đã bị Nghị định 390/2026 bãi bỏ toàn bộ nhưng chưa được chú thích",
 "Vì tiêu chí này chỉ áp dụng cho doanh nghiệp có vốn đầu tư nước ngoài",
 "Vì Luật Các tổ chức tín dụng không cho phép mở chi nhánh tại nhiều tỉnh"]),
73: ("Vì sao việc bỏ điều kiện kinh doanh với vàng trang sức", [
 "Giảm thủ tục cho cơ sở nhỏ, vẫn quản lý qua luật chất lượng, đo lường, thuế, chống rửa tiền",
 "Vì vàng trang sức không còn được phép mua bán tự do tại thị trường Việt Nam",
 "Vì toàn bộ vàng trang sức đã chuyển sang do NHNN trực tiếp quản lý sản xuất",
 "Vì vàng trang sức được miễn mọi loại thuế và không cần hóa đơn chứng từ"]),
74: ("Khoảng trống pháp lý nào được chỉ ra đối với kinh doanh vàng trên tài khoản", [
 "Chưa có quy định về sàn, ký quỹ, bảo vệ nhà đầu tư; vẫn cần Thủ tướng cho phép từng trường hợp",
 "Hoạt động này đã bị cấm tuyệt đối nên không cần khung pháp lý riêng",
 "Hoạt động này chỉ cần Giấy chứng nhận đăng ký doanh nghiệp là được thực hiện",
 "Hoạt động này do Bộ Công Thương cấp phép theo pháp luật về sở giao dịch hàng hóa"]),
},
"vbhn118": {
4: ("Ai ký xác thực Văn bản hợp nhất", [
 "Phó Thống đốc Đoàn Thái Sơn (KT. Thống đốc)",
 "Cục trưởng Cục Phát hành và Kho quỹ",
 "Vụ trưởng Vụ Pháp chế (TL. Thống đốc)",
 "Chánh Văn phòng NHNN (TL. Thống đốc)"]),
6: ("Thông tư quy định về tiêu hủy những loại tiền", [
 "Tiền giấy (cotton, polymer), tiền kim loại không đủ tiêu chuẩn lưu thông, tiền đình chỉ lưu hành",
 "Chỉ tiền giấy polymer không đủ tiêu chuẩn lưu thông và tiền kim loại đã đình chỉ lưu hành",
 "Tiền giả, tiền nghi giả bị thu giữ và tiền không đủ tiêu chuẩn lưu thông do dân nộp",
 "Tiền mẫu, tiền lưu niệm, tiền in hỏng trong quá trình in đúc và tiền đình chỉ lưu hành"]),
10: ("Kế hoạch tiêu hủy tiền trình Thống đốc", [
 "Thời gian tiêu hủy, số lượng, giá trị từng loại tiền tiêu hủy",
 "Danh sách nhân sự, mức bồi dưỡng và trang phục cho người tham gia",
 "Phương án bán phế liệu và dự toán thu, chi phục vụ tiêu hủy tiền",
 "Địa điểm tiêu hủy và thành phần Hội đồng giám sát tiêu hủy tiền"]),
13: ("Ai quyết định tỷ lệ kiểm đếm", [
 "Chủ tịch Hội đồng tiêu hủy, căn cứ kết quả thừa, thiếu qua kiểm đếm tiền tiêu hủy hằng năm",
 "Thống đốc NHNN, căn cứ kế hoạch tiêu hủy tiền và đề nghị của Cục Phát hành và Kho quỹ",
 "Chủ tịch Hội đồng giám sát, căn cứ kết quả kiểm kê kho tiền tiêu hủy hằng tháng",
 "Phó Chủ tịch phụ trách cụm, căn cứ công suất máy móc và số lượng kiểm ngân hiện có"]),
14: ("Theo nguyên tắc tiêu hủy, tiêu hủy theo số tiền", [
 "Số tiền thực tế nhận từ Kho tiền Trung ương, sau khi có kết quả kiểm đếm, phân loại",
 "Số tiền ghi trên lệnh điều chuyển của Cục Phát hành và Kho quỹ gửi Kho tiền Trung ương",
 "Số tiền ghi trong kế hoạch tiêu hủy đã được Thống đốc NHNN phê duyệt cho năm đó",
 "Số tiền ghi trên niêm phong bó (túi) của tổ chức tín dụng, Kho bạc Nhà nước nộp về"]),
15: ("Yêu cầu đối với tiền sau khi đã tiêu hủy", [
 "Phải bảo đảm không thể khôi phục để sử dụng lại như tiền",
 "Phải được nhập lại Quỹ Dự trữ phát hành dưới dạng phế liệu",
 "Phải được lưu giữ tối thiểu 05 năm trước khi được bán ra",
 "Phải được chuyển giao cho Thanh tra NHNN kiểm tra lại"]),
16: ("Tiền giấy được tiêu hủy bằng phương pháp", [
 "Hệ thống máy cắt hủy chuyên dùng",
 "Đốt trong lò đốt chuyên dụng",
 "Nghiền ướt rồi ép thành kiện",
 "Nấu chảy hoặc máy hủy chuyên dùng"]),
20: ("Phó Chủ tịch thường trực Hội đồng tiêu hủy", [
 "Phó Cục trưởng Cục Phát hành và Kho quỹ trực tiếp phụ trách Cụm phía Bắc",
 "Chi cục trưởng Chi cục Phát hành và Kho quỹ tại TP. Hồ Chí Minh",
 "Phó Vụ trưởng Vụ Tài chính - Kế toán phụ trách công tác kế toán tiêu hủy",
 "Phó Chánh Thanh tra NHNN phụ trách giám sát tiêu hủy tiền"]),
23: ("Trong số ủy viên Hội đồng tiêu hủy, có bao nhiêu", [
 "3 (một thư ký Hội đồng, hai thư ký tại hai cụm)",
 "1 (thư ký chung của Hội đồng tiêu hủy)",
 "2 (một thư ký tại mỗi cụm tiêu hủy)",
 "4 (một thư ký tại mỗi tổ chuyên trách)"]),
26: ("Ai phê duyệt kế hoạch nhận tiền tiêu hủy", [
 "Phó Chủ tịch phụ trách cụm tiêu hủy đó",
 "Chủ tịch Hội đồng tiêu hủy tiền",
 "Thống đốc NHNN theo đề nghị của Cục",
 "Thủ kho tiền tiêu hủy của cụm đó"]),
28: ("“Tổ 1” trong các tổ chuyên trách", [
 "Tổ giao nhận và bảo quản tiền tiêu hủy",
 "Tổ kiểm đếm và phân loại tiền tiêu hủy",
 "Tổ cắt hủy tiền và thu hồi phế liệu",
 "Tổ tổng hợp, hành chính và kế toán"]),
29: ("Tổ nào có nhiệm vụ nhập kho tiền đủ tiêu chuẩn", [
 "Tổ 1 – Tổ giao nhận và bảo quản",
 "Tổ 2 – Tổ kiểm đếm tiền tiêu hủy",
 "Tổ 3 – Tổ cắt hủy tiền",
 "Tổ 4 – Tổ tổng hợp, kế toán"]),
30: ("Tổ 2 kiểm đếm tờ (miếng) đối với những bó", [
 "Bó (túi) thừa, thiếu thếp, niêm phong hoặc đóng gói không đúng quy cách",
 "Mọi bó (túi) nhận từ Kho tiền Trung ương trong ngày làm việc đó",
 "Chỉ bó (túi) có mệnh giá từ 100.000 đồng trở lên và tiền polymer",
 "Bó (túi) do Hội đồng giám sát chỉ định ngẫu nhiên khi giao nhận"]),
32: ("Tổ trưởng và Tổ phó của mỗi tổ", [
 "Phó Chủ tịch phụ trách cụm tiêu hủy",
 "Chủ tịch Hội đồng tiêu hủy tiền",
 "Vụ trưởng Vụ Tổ chức cán bộ",
 "Thống đốc NHNN theo đề nghị của Cục"]),
33: ("Khi phát hiện hành vi tham ô", [
 "Phối hợp công chức giám sát lập biên bản, báo cáo Hội đồng tiêu hủy và Hội đồng giám sát",
 "Báo ngay cho cơ quan công an, đồng thời tạm dừng toàn bộ hoạt động tiêu hủy của cụm",
 "Tự lập biên bản, gửi Vụ Tổ chức cán bộ xử lý kỷ luật theo phân cấp quản lý",
 "Báo cáo trực tiếp Thống đốc NHNN và Chánh Thanh tra NHNN trong ngày"]),
35: ("Tham gia quản lý kho tiền tiêu hủy tại mỗi cụm", [
 "Ủy viên Hội đồng tiêu hủy, nhân viên kế toán kho tiền tiêu hủy và thủ kho",
 "Chủ tịch Hội đồng tiêu hủy, Tổ trưởng Tổ 1 và thủ kho tiền tiêu hủy",
 "Phó Chủ tịch phụ trách cụm, công chức giám sát và thủ kho tiền tiêu hủy",
 "Tổ trưởng Tổ 1, Tổ trưởng Tổ 2 và Tổ trưởng Tổ 3 của cụm tiêu hủy"]),
38: ("Thành viên nào có nhiệm vụ kiểm tra, đối chiếu", [
 "Nhân viên thực hiện nhiệm vụ kế toán kho tiền tiêu hủy",
 "Ủy viên Hội đồng tiêu hủy tham gia quản lý kho tiền",
 "Thủ kho tiền tiêu hủy, người giữ chìa khóa cánh trong",
 "Tổ trưởng Tổ 4 phụ trách hành chính, kế toán, thống kê"]),
41: ("Đối với Cụm tiêu hủy phía Nam, đơn vị nào lập phiếu", [
 "Phòng Kế toán - Tài vụ thuộc Chi cục Phát hành và Kho quỹ",
 "Vụ Tài chính - Kế toán theo lệnh điều chuyển của Cục",
 "Cục Phát hành và Kho quỹ, kèm lệnh điều chuyển",
 "NHNN chi nhánh Khu vực tại TP. Hồ Chí Minh"]),
43: ("Khi thủ kho tiền tiêu hủy nhận tiền", [
 "Công chức kiểm soát nội bộ Cục Phát hành và Kho quỹ, Chi cục Phát hành và Kho quỹ",
 "Thanh tra viên NHNN và Tổ trưởng Tổ giám sát giao nhận của Hội đồng giám sát",
 "Đại diện Vụ Tài chính - Kế toán và Phòng Kế toán - Tài vụ của Chi cục",
 "Chủ tịch Hội đồng tiêu hủy hoặc Phó Chủ tịch phụ trách cụm tiêu hủy"]),
45: ("Số tiền đưa vào kiểm đếm tờ", [
 "Lấy ngẫu nhiên theo tỷ lệ kiểm đếm từng loại tiền do Chủ tịch Hội đồng tiêu hủy duyệt",
 "Chọn các bao (thùng) có niêm phong lâu nhất hoặc có dấu hiệu đóng gói không đúng quy cách",
 "Kiểm đếm toàn bộ 100% số tiền nhận về, sau đó mới chuyển sang Tổ 3 cắt hủy",
 "Do Hội đồng giám sát chỉ định từng bao (thùng) dựa trên kết quả kiểm kê tháng trước"]),
48: ("Kiểm ngân kiểm đếm thấy bó (túi) tiền đủ số lượng", [
 "Hủy ngay giấy niêm phong và đóng bó (túi), niêm phong mới",
 "Giữ nguyên niêm phong cũ và chuyển ngay sang Tổ 3 cắt hủy",
 "Gửi lại kho tiền tiêu hủy để chờ kiểm kê cuối tháng",
 "Lập biên bản gửi tổ chức tín dụng đã niêm phong bó tiền"]),
50: ("Tiền giấy biến dạng không thể đóng bó", [
 "Đóng 01 túi vải đủ 1.000 tờ, buộc chặt miệng túi, dán niêm phong sát nút buộc",
 "Đóng túi nilon 500 tờ, hàn kín miệng túi và dán niêm phong lên mặt túi",
 "Gói giấy kraft theo từng thếp 100 tờ, xếp 10 thếp vào một hộp có niêm phong",
 "Để rời trong thùng tôn có khóa, niêm phong nắp thùng có chữ ký kiểm ngân"]),
56: ("Số tiền tạm ứng (để bù vào bó thiếu tờ)", [
 "Tiêu hủy vào ngày cuối cùng khi tiêu hủy loại tiền cùng mệnh giá",
 "Nhập Quỹ Dự trữ phát hành tại Kho tiền Trung ương vào cuối năm",
 "Hoàn trả Kho tiền Trung ương ngay trong ngày làm việc tạm ứng",
 "Chuyển cho Tổ 4 hạch toán vào thu nhập khác của Cục cuối đợt"]),
57: ("Trong giờ nghỉ trưa, cửa phòng kiểm đếm", [
 "Tổ trưởng Tổ 2 và công chức giám sát của Hội đồng giám sát",
 "Thủ kho tiền tiêu hủy và nhân viên kế toán kho tiền tiêu hủy",
 "Phó Chủ tịch phụ trách cụm và Tổ trưởng Tổ 2 của cụm đó",
 "Kiểm ngân ra sau cùng và Tổ trưởng Tổ giám sát kiểm đếm"]),
58: ("Cuối ngày làm việc, biên bản thừa, thiếu", [
 "Theo từng NHNN chi nhánh Khu vực, Sở Giao dịch, tổ chức tín dụng, Kho bạc Nhà nước",
 "Theo từng kiểm ngân và từng ca làm việc, có xác nhận của Tổ trưởng Tổ 2",
 "Theo từng mệnh giá tiền và từng loại chất liệu (cotton, polymer, kim loại)",
 "Theo từng bao (thùng) nhận từ Kho tiền Trung ương trong ngày làm việc"]),
59: ("Cuối mỗi ngày, ai lập Biên bản xác nhận kết quả tiêu hủy", [
 "Tổ trưởng Tổ 3, có xác nhận của Tổ trưởng Tổ giám sát cắt hủy",
 "Thủ kho tiền tiêu hủy, có xác nhận của kế toán kho tiền",
 "Phó Chủ tịch phụ trách cụm, có xác nhận của Hội đồng giám sát",
 "Tổ trưởng Tổ 4, có xác nhận của Tổ trưởng Tổ 3 và Tổ 2"]),
62: ("Người không có nhiệm vụ tiêu hủy tiền muốn vào", [
 "Được Phó Chủ tịch phụ trách cụm tiêu hủy cho phép bằng văn bản",
 "Được Tổ trưởng của khu vực đó đồng ý và ghi vào sổ theo dõi",
 "Xuất trình thẻ ngành NHNN và đăng ký với công chức giám sát",
 "Có công chức giám sát đi cùng trong suốt thời gian ở bên trong"]),
65: ("Phát hiện bó (túi) thừa hoặc thiếu thếp", [
 "Lập biên bản tại chỗ dưới sự giám sát của công chức giám sát, giao Tổ 2 kiểm đếm tờ (miếng)",
 "Lập biên bản, niêm phong nguyên trạng và trả lại Kho tiền Trung ương trong ngày",
 "Ghi chú vào sổ giao nhận và chuyển thẳng sang Tổ 3 cắt hủy theo số ghi trên niêm phong",
 "Niêm phong lại, báo cáo Thống đốc và chờ ý kiến chỉ đạo trước khi kiểm đếm"]),
66: ("Ai quyết định thời điểm tiêu hủy trong năm", [
 "Phó Chủ tịch phụ trách cụm tiêu hủy",
 "Chủ tịch Hội đồng tiêu hủy tiền",
 "Thống đốc NHNN theo đề nghị của Cục",
 "Chủ tịch Hội đồng giám sát tiêu hủy"]),
67: ("Tiền đủ tiêu chuẩn lưu thông phát hiện qua kiểm đếm", [
 "Nhập Quỹ dự trữ phát hành tại Kho tiền Trung ương vào cuối đợt tiêu hủy",
 "Tiêu hủy cùng đợt với tiền không đủ tiêu chuẩn để bảo đảm khớp số liệu",
 "Trả lại tổ chức tín dụng đã nộp, kèm biên bản và niêm phong bó tiền",
 "Nhập Quỹ nghiệp vụ phát hành của NHNN chi nhánh Khu vực ngay trong ngày"]),
68: ("Tiền tiêu hủy bảo quản trong kho được kiểm kê", [
 "Mỗi tháng 01 lần, cuối ngày làm việc cuối cùng của tháng",
 "Mỗi quý 01 lần, vào ngày làm việc đầu tiên của quý sau",
 "Mỗi tuần 01 lần, vào cuối ngày làm việc thứ Sáu",
 "Mỗi đợt tiêu hủy 01 lần, vào ngày kết thúc đợt"]),
69: ("Khi Phó Chủ tịch phụ trách cụm vắng mặt, việc kiểm kê", [
 "Một ủy viên Hội đồng tiêu hủy không phải là ủy viên quản lý kho tiền",
 "Ủy viên Hội đồng tiêu hủy đang tham gia quản lý kho tiền tiêu hủy",
 "Thủ kho tiền tiêu hủy, có sự chứng kiến của kế toán kho tiền",
 "Trưởng phòng Tiêu hủy tiền, có sự giám sát của Hội đồng giám sát"]),
72: ("Tổ trưởng Tổ 2, Tổ 3 tổng hợp báo cáo", [
 "Hằng tháng, 6 tháng, đợt tiêu hủy và hằng năm",
 "Hằng ngày, hằng tuần, hằng tháng và hằng năm",
 "Hằng quý, 6 tháng, 9 tháng và hằng năm",
 "Hằng tuần, đợt tiêu hủy và khi có yêu cầu"]),
73: ("Hằng tháng, các cụm tiêu hủy tổng hợp số liệu", [
 "Báo cáo Chủ tịch Hội đồng tiêu hủy và gửi Hội đồng giám sát",
 "Báo cáo Thống đốc NHNN và gửi Cục Phát hành và Kho quỹ",
 "Gửi Vụ Tài chính - Kế toán và Hội đồng giám sát",
 "Báo cáo Chủ tịch Hội đồng giám sát và gửi Thanh tra NHNN"]),
76: ("Báo cáo sơ kết, tổng kết năm", [
 "Hội đồng tiêu hủy chủ trì, phối hợp với Hội đồng giám sát",
 "Hội đồng giám sát chủ trì, phối hợp với Hội đồng tiêu hủy",
 "Vụ Tài chính - Kế toán chủ trì, phối hợp với Cục",
 "Thanh tra NHNN chủ trì, phối hợp với Hội đồng tiêu hủy"]),
77: ("Cá nhân tham gia tiêu hủy tiền tham ô", [
 "Bồi thường 100% giá trị tài sản thiếu và buộc thôi việc hoặc bị truy cứu hình sự",
 "Bồi thường 50% giá trị tài sản thiếu và bị kỷ luật khiển trách hoặc cảnh cáo",
 "Bồi thường 100% giá trị tài sản thiếu và bị hạ một bậc lương trong 12 tháng",
 "Bị truy cứu trách nhiệm hình sự, không phải bồi thường nếu đã chấp hành án"]),
78: ("Ngoài tiền lương, phụ cấp, người tham gia", [
 "Chế độ bồi dưỡng về tiêu hủy tiền và chế độ khác theo hướng dẫn của NHNN",
 "Phụ cấp độc hại bằng 30% lương cơ bản trong thời gian tham gia tiêu hủy",
 "Tiền thưởng tính theo tỷ lệ trên tổng giá trị tiền đã tiêu hủy trong đợt",
 "Không có chế độ riêng ngoài tiền lương, phụ cấp lương, tiền công"]),
82: ("Trách nhiệm của Vụ Tài chính - Kế toán", [
 "Tổ chức công tác kế toán và hướng dẫn hạch toán kế toán tiêu hủy tiền",
 "Chủ trì giám sát tiêu hủy tiền theo quy định của Thống đốc NHNN",
 "Tuyển dụng lao động hợp đồng và trưng tập công chức tham gia tiêu hủy",
 "Trình Thống đốc phương án bán phế liệu và định mức cắt hủy tiền"]),
84: ("Vì sao phân tích phản biện cho rằng quyền lực", [
 "Cục trưởng vừa trình kế hoạch, làm Chủ tịch Hội đồng, ban hành nội quy, tự quyết tỷ lệ kiểm đếm",
 "Thống đốc trực tiếp điều hành mọi tổ chuyên trách mà không qua Hội đồng tiêu hủy",
 "Hội đồng giám sát kiêm luôn việc cắt hủy tiền và lập biên bản kết quả tiêu hủy",
 "Thủ kho giữ toàn bộ chìa khóa kho tiền, kể cả chìa khóa lớp cánh ngoài"]),
85: ("Hướng hoàn thiện nào được đề xuất để cân bằng", [
 "Hội đồng giám sát có ý kiến trước khi quyết, hoặc báo cáo Thống đốc tỷ lệ kèm căn cứ",
 "Bỏ hẳn việc kiểm đếm trước khi tiêu hủy để giảm chi phí và thời gian xử lý",
 "Giao thủ kho tiền tiêu hủy quyết định tỷ lệ vì là người trực tiếp quản lý tiền",
 "Kiểm đếm 100% mọi bó tiền, không phụ thuộc kết quả thừa thiếu các năm trước"]),
86: ("Rủi ro nào phát sinh khi Thông tư không quy định tỷ lệ", [
 "Tỷ lệ có thể bị đặt rất thấp, giảm khả năng phát hiện sai sót, mà tiền đã hủy không thể kiểm lại",
 "Hội đồng tiêu hủy buộc phải kiểm đếm lại toàn bộ số tiền đã cắt hủy trong năm trước",
 "Hội đồng tiêu hủy không thể được thành lập vì thiếu căn cứ xác định nhân sự",
 "Tiền giả phát hiện qua kiểm đếm được đưa trở lại lưu thông qua Quỹ dự trữ phát hành"]),
87: ("Vấn đề nào được chỉ ra đối với quỹ tạm ứng", [
 "Không có hạn mức tạm ứng tối đa; số dư chỉ hủy cuối đợt nên tồn ngoài quy trình chính lâu",
 "Quỹ tạm ứng được lấy từ ngân sách nhà nước nên phải quyết toán riêng với Bộ Tài chính",
 "Quỹ tạm ứng không được kiểm kê và không có sự giám sát của Hội đồng giám sát",
 "Quỹ tạm ứng do tổ chức tín dụng nộp nên phải hoàn trả sau mỗi đợt tiêu hủy"]),
88: ("Khoảng trống nào được chỉ ra về phế liệu", [
 "Chưa có tiêu chí kích thước mảnh cắt, cách kiểm tra, và yêu cầu môi trường với polymer, kim loại",
 "Thông tư cấm bán phế liệu dưới mọi hình thức nên phát sinh chi phí lưu kho lớn",
 "Phế liệu phải được lưu kho vĩnh viễn tại Kho tiền Trung ương để phục vụ thanh tra",
 "Phế liệu được trả lại tổ chức tín dụng đã nộp tiền để tự xử lý theo quy định"]),
89: ("Theo phân tích, công cụ nào chưa được Thông tư đề cập", [
 "Camera giám sát của đơn vị, máy phân loại tự động, sổ kế toán điện tử",
 "Niêm phong có chữ ký của tổ trưởng và công chức giám sát",
 "Biên bản giao nhận và sổ theo dõi giao nhận nội bộ giữa các tổ",
 "Thẻ nhân viên và trang phục do hai Hội đồng trang cấp"]),
90: ("Vấn đề nào được nêu về thời gian lưu kho", [
 "Không có thời hạn tối đa từ khi nhận đến khi hủy; tiền giả, lẫn loại do Phó Chủ tịch chọn thời điểm",
 "Tiền phải được cắt hủy ngay trong ngày nhận nên không đủ thời gian kiểm đếm theo tỷ lệ",
 "Thời hạn lưu kho tối đa là 15 ngày làm việc, quá ngắn so với công suất máy cắt hủy",
 "Tiền chỉ được cắt hủy vào tháng 12 hằng năm nên tồn kho rất lớn trong các tháng khác"]),
91: ("Biểu hiện nào thể hiện nguyên tắc kiểm soát chéo", [
 "Bốn tổ độc lập; kho ba thành viên mỗi người một ổ khóa; cửa phòng niêm phong có hai chữ ký",
 "Một cá nhân chịu trách nhiệm toàn bộ luồng tiền từ khi nhận đến khi cắt hủy để dễ quy trách nhiệm",
 "Hội đồng tiêu hủy tự giám sát chính mình, không cần sự tham gia của Hội đồng giám sát",
 "Chỉ thủ kho được ra vào khu vực cắt hủy và giữ toàn bộ chìa khóa phòng"]),
92: ("Vì sao cơ chế kiểm đếm theo tỷ lệ được đánh giá", [
 "Tiết kiệm nguồn lực, tập trung vào rủi ro, dựa trên dữ liệu thừa thiếu và mẫu ngẫu nhiên",
 "Vì cho phép bỏ qua hoàn toàn việc kiểm đếm đối với các loại tiền có mệnh giá nhỏ",
 "Vì tỷ lệ được Thống đốc cố định cho mọi năm nên dễ lập kế hoạch nhân sự",
 "Vì tổ chức tín dụng đã kiểm đếm trước khi nộp nên không cần kiểm lại"]),
94: ("Việc nhiều nội dung kỹ thuật được giao", [
 "Hợp lý về bảo mật, nhưng Thông tư khó được đánh giá độc lập, phụ thuộc văn bản hướng dẫn",
 "Khiến Thông tư không có hiệu lực cho đến khi văn bản hướng dẫn được đăng Công báo",
 "Buộc phải công bố quy trình máy hủy và trang thiết bị an ninh lên Công báo",
 "Làm Hội đồng giám sát mất thẩm quyền giám sát đối với quy trình cắt hủy"]),
95: ("Bất tiện nào được chỉ ra ở cách văn bản hợp nhất", [
 "Chỉ ghi “(được bãi bỏ)” mà không nêu nội dung cũ, phải tra văn bản gốc",
 "Điểm đ bị lặp lại hai lần ở Điều 16 và Điều 17 của văn bản hợp nhất",
 "Điểm đ mâu thuẫn với phạm vi điều chỉnh tại Điều 1 của Thông tư",
 "Điểm đ chưa có hiệu lực vì Thông tư 42/2026 chưa được đăng Công báo"]),
}}

for doc, patches in P.items():
    p = ROOT / "data" / f"{doc}.json"
    D = json.loads(p.read_text("utf-8"))
    for i, (prefix, opts) in patches.items():
        q = D["qs"][i]
        assert q["q"].startswith(prefix), (doc, i, q["q"][:60])
        assert len(opts) == 4 and len(set(opts)) == 4, (doc, i)
        q["o"] = opts
    p.write_text(json.dumps(D, ensure_ascii=False, indent=1), "utf-8")
    print(doc, len(patches), "câu đã sửa")
