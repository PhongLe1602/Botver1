import requests

from lxml import html
login_url = 'https://qldt.ptit.edu.vn/default.aspx?page=dangnhap'

def show(payload):
    with requests.Session() as s:
        ans = ""
        schedule = list()
        response = s.post(login_url, data=payload)
        r = s.get("https://qldt.ptit.edu.vn/Default.aspx?page=xemlichthi")
        tree = html.fromstring(r.content.decode(r.encoding))
        l = tree.xpath('.//span/text()')
        d = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        index = 0
        ans = "STT | Mã MH |  Tên MH | Ghép thi | Tổ thi | Số lượng | Ngày thi | Giờ BD | Số phút | Phòng | Ghi chú |"
        for i in range(29, len(l)- 6):
            if l[i] == d[index]:
                ans += '\n----------------------------------------------------------------------------------------------' + '\n'
                index += 1
            ans += l[i] + " | "
        if index > 0: return ans
        return "Hiện chưa có lịch thi!"