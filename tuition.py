import requests
from lxml import html
login_url = 'https://qldt.ptit.edu.vn/default.aspx?page=dangnhap'
def show(payload):
    with requests.Session() as s:
        ans = ""
        response = s.post(login_url, data=payload)
        r = s.get("https://qldt.ptit.edu.vn/Default.aspx?page=xemhocphi")
        tree = html.fromstring(r.content.decode(r.encoding))
        l = tree.xpath('.//span/text()')
        d = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        index = 0
        cnt = 10
        ans = "STT | Mã MH |  Tên MH | Mã nhóm | Tổ thực hành | Số TC | TCHP | Học phí | Miễn giảm | Phải đóng |"
        i = 28
        while i < len(l)- 21:
            if l[i] == d[index] and (cnt == 9 or cnt == 10):
                cnt = 0
                ans += '\n----------------------------------------------------------------------------------------------' + '\n'
                index += 1
            ans += l[i] + " | "
            cnt += 1
            i += 1
        ans += '\n----------------------------------------------------------------------------------------------' + '\n'
        ans += l[i] + l[i+1] + "\n"
        i += 2
        ans += l[i] + l[i + 1] + "\n"
        i += 2
        ans += l[i] + l[i + 1] + " " + l[i+2] + "\n"
        i += 3
        ans += l[i] + l[i + 1] + l[i+2] + "\n"
        i += 3
        ans += l[i] + " " + l[i + 1] + " " + l[i + 2] + "\n"
        i += 3
        ans += l[i] + " " +  l[i + 1] + l[i + 2] + "\n"
        i += 3
        if index > 0: return ans
        return "Hiện chưa có học phí!"