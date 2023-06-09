import requests
from bs4 import BeautifulSoup
from lxml import html
login_url = 'https://qldt.ptit.edu.vn/default.aspx?page=dangnhap' #Link login the web
get_url = 'https://qldt.ptit.edu.vn/Default.aspx?page=xemdiemthi' #Link web which i want to get data
# payload = {
#     '__EVENTTARGET': '',
#     '__EVENTARGUMENT': '',
#     '__VIEWSTATE': '/wEPDwUKLTMxNjc3NTM3NQ9kFgJmD2QWBGYPZBYCAgEPFgIeB2NvbnRlbnRkZAIBD2QWCAIDD2QWAmYPZBYCAgEPZBYMZg8PFgYeCUZvcmVDb2xvcgp4HgRUZXh0BQxDaMOgbyBi4bqhbiAeBF8hU0ICBGRkAgEPDxYEHwEKeB8DAgRkZAICDw8WBB8BCngfAwIEZGQCAw8PFgYfAgUYVGhheSDEkeG7lWkgbeG6rXQga2jhuql1HwEKeB8DAgRkZAIEDw8WBB8BCngfAwIEZGQCBQ8PFgYfAgUNxJDEg25nIE5o4bqtcB8BCngfAwIEZGQCBQ9kFsIBAgEPDxYEHghDc3NDbGFzcwUIb3V0LW1lbnUfAwICZBYCZg8PFgIfAgULVFJBTkcgQ0jhu6ZkZAIDDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ8PFgIfAgUXREFOSCBN4bukQyBDSOG7qEMgTsSCTkdkZAIFDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ8PFgIfAgUbRE0gQ0jhu6hDIE7Egk5HIMSQw4FOSCBHScOBZGQCBw8PFgQfBAUIb3V0LW1lbnUfAwICZGQCCQ8PFgYfBAUIb3V0LW1lbnUfAwICHgdWaXNpYmxlaGQWAgIBDw8WAh8CBRXEkMSCTkcgS8OdIE3DlE4gSOG7jENkZAILDw8WBB8EBQhvdXQtbWVudR8DAgJkZAINDw8WBh8EBQhvdXQtbWVudR8DAgIfBWhkFgICAQ8PFgIfAgUHWEVNIFRLQmRkAg8PDxYEHwQFCG91dC1tZW51HwMCAmRkAhEPDxYGHwQFCG91dC1tZW51HwMCAh8FaGQWAmYPDxYCHwIFDlhFTSBM4buKQ0ggVEhJZGQCEw8PFgYfBAUIb3V0LW1lbnUfAwICHwVoZBYCAgEPDxYCHwIFFFhFTSBM4buKQ0ggVEhJIEzhuqBJZGQCFQ8PFgYfBAUIb3V0LW1lbnUfAwICHwVoZBYCAgEPDxYCHwIFEVhFTSBM4buKQ0ggVEhJIEdLZGQCFw8PFgYfBAUIb3V0LW1lbnUfAwICHwVoZGQCGQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCGw8PFgYfBAUIb3V0LW1lbnUfAwICHwVoZBYCAgEPDxYCHwIFDlhFTSBI4buMQyBQSMONZGQCHQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCHw8PFgYfBAUIb3V0LW1lbnUfAwICHwVoZBYCAgEPDxYCHwIFC1hFTSDEkEnhu4JNZGQCIQ8PFgYfBAUIb3V0LW1lbnUfAwICHwVoZGQCIw8PFgQfBAUIb3V0LW1lbnUfAwICZGQCJQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCJw8PFgQfBAUIb3V0LW1lbnUfAwICZGQCKQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCKw8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFCVhFTSBDVMSQVGRkAi0PDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBQtYRU0gTcOUTiBUUWRkAi8PDxYEHwQFCG91dC1tZW51HwMCAmRkAjEPDxYEHwQFCG91dC1tZW51HwMCAmRkAjMPDxYGHwQFCG91dC1tZW51HwMCAh8FaGQWAgIBDw8WAh8CBRJT4busQSBUVCBDw4EgTkjDgk5kZAI1Dw8WBh8EBQhvdXQtbWVudR8DAgIfBWdkFgICAQ8PFgIfAgUOR8OTUCDDnSBLSeG6vk5kZAI3Dw8WBh8EBQhvdXQtbWVudR8DAgIfBWhkFgJmDw8WAh8CBRBT4busQSBMw50gTOG7ikNIZGQCOQ8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFFVFV4bqiTiBMw50gU0lOSCBWScOKTmRkAjsPDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBSJL4bq+VCBRVeG6oiBTSU5IIFZJw4pOIMSQw4FOSCBHScOBZGQCPQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCPw8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPZBYCZg8PFgIfAgUZxJDDgU5IIEdJw4EgR0nhuqJORyBE4bqgWWRkAkEPDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBRTEkMSCTkcgS8OdIFRISSBM4bqgSWRkAkMPDxYEHwQFCG91dC1tZW51HwMCAmRkAkUPDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBRLEkEsgQ0hVWcOKTiBOR8OATkhkZAJHDw8WBB8EBQhvdXQtbWVudR8DAgJkZAJJDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ8PFgIfAgUWS1EgWMOJVCBU4buQVCBOR0hJ4buGUGRkAksPDxYEHwQFCG91dC1tZW51HwMCAmRkAk0PDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBRpDw4JVIEjhu45JIFRIxq/hu5xORyBH4bq2UGRkAk8PDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBRPEkEsgS0jDk0EgTFXhuqxOIFROZGQCUQ8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFDk5I4bqsUCDEkEnhu4JNZGQCUw8PFgQfBAUIb3V0LW1lbnUfAwICZGQCVQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCVw8PFgQfBAUIb3V0LW1lbnUfAwICZGQCWQ8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFHlhFTSDEkEnhu4JNIE3DlE4gR0nhuqJORyBE4bqgWWRkAlsPDxYEHwQFCG91dC1tZW51HwMCAmRkAl0PDxYEHwQFCG91dC1tZW51HwMCAmRkAl8PDxYEHwQFCG91dC1tZW51HwMCAmRkAmEPDxYEHwQFCG91dC1tZW51HwMCAmRkAmMPDxYEHwQFCG91dC1tZW51HwMCAmRkAmUPDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBSZUSOG7kE5HIEvDiiBHSeG6ok5HIFZJw4pOIERVWeG7hlQgS1FES2RkAmcPDxYEHwQFCG91dC1tZW51HwMCAmRkAmkPDxYEHwQFCG91dC1tZW51HwMCAmRkAmsPDxYEHwQFCG91dC1tZW51HwMCAmRkAm0PDxYEHwQFCG91dC1tZW51HwMCAmRkAm8PDxYGHwQFCG91dC1tZW51HwMCAh8FZ2QWAgIBDw8WAh8CBRRIxq/hu5pORyBE4bqqTiDEkEtNSGRkAnEPDxYEHwQFCG91dC1tZW51HwMCAmRkAnMPDxYEHwQFCG91dC1tZW51HwMCAmRkAnUPDxYEHwQFCG91dC1tZW51HwMCAmRkAncPDxYEHwQFCG91dC1tZW51HwMCAmRkAnkPDxYEHwQFCG91dC1tZW51HwMCAmRkAnsPDxYEHwQFCG91dC1tZW51HwMCAmRkAn0PDxYEHwQFCG91dC1tZW51HwMCAmRkAn8PDxYEHwQFCG91dC1tZW51HwMCAmRkAoEBDw8WBB8EBQhvdXQtbWVudR8DAgJkZAKDAQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQChQEPDxYEHwQFCG91dC1tZW51HwMCAmRkAocBDw8WBB8EBQhvdXQtbWVudR8DAgJkZAKJAQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCiwEPDxYEHwQFCG91dC1tZW51HwMCAmRkAo0BDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ8PFgIfAgUXSMOTQSDEkMagTiDEkEnhu4ZOIFThu6xkZAKPAQ8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFFk5HSOG7iCBE4bqgWSBE4bqgWSBCw5lkZAKRAQ8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFF8SQxIJORyBLw50gTkdI4buIIFBIw4lQZGQCkwEPDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBRLEkMSCTkcgS8OdIENPSSBUSElkZAKVAQ8PFgQfBAUIb3V0LW1lbnUfAwICZBYCAgEPDxYCHwIFElhFTSBM4buKQ0ggQ09JIFRISWRkApcBDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ8PFgIfAgUbS1EgTkdIScOKTiBD4buoVSBLSE9BIEjhu4xDZGQCmQEPDxYEHwQFCG91dC1tZW51HwMCAmRkApsBDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ9kFgJmDw8WAh8CBSTEkMSCTkcgS8OdIFhJTiBHSeG6pFkgQ0jhu6hORyBOSOG6rE5kZAKdAQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCnwEPDxYEHwQFCG91dC1tZW51HwMCAmRkAqEBDw8WBB8EBQhvdXQtbWVudR8DAgJkFgICAQ8PFgIfAgUVQ+G6qE0gTkFORyBTSU5IIFZJw4pOZGQCowEPDxYEHwQFCG91dC1tZW51HwMCAmRkAqUBDw8WBB8EBQhvdXQtbWVudR8DAgJkZAKnAQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCqQEPDxYEHwQFCG91dC1tZW51HwMCAmQWAgIBDw8WAh8CBSRCw4FPIEJJ4buCVSBQSOG7pEMgVuG7pCBMw4NOSCDEkOG6oE9kZAKrAQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCrQEPDxYEHwQFCG91dC1tZW51HwMCAmRkAq8BDw8WBB8EBQhvdXQtbWVudR8DAgJkZAKxAQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCswEPDxYEHwQFCG91dC1tZW51HwMCAmRkArUBDw8WBB8EBQhvdXQtbWVudR8DAgJkZAK3AQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCuQEPDxYEHwQFCG91dC1tZW51HwMCAmRkArsBDw8WBB8EBQhvdXQtbWVudR8DAgJkZAK9AQ8PFgQfBAUIb3V0LW1lbnUfAwICZGQCvwEPDxYEHwQFCG91dC1tZW51HwMCAmRkAsEBDw8WBB8EBQhvdXQtbWVudR8DAgJkZAIHD2QWAgIBD2QWAmYPZBYCAgMPZBYQAgEPDxYCHwIFE1F1w6puIG3huq10IGto4bqpdSFkZAIDDw8WAh8CBRJUw6puIMSQxINuZyBOaOG6rXBkZAIFDw9kFgIeCm9ua2V5cHJlc3MFQGJ1dHRvbl9jbGljayh0aGlzLCdjdGwwMF9Db250ZW50UGxhY2VIb2xkZXIxX2N0bDAwX2J0bkRhbmdOaGFwJylkAgcPDxYCHwIFDE3huq10IEto4bqpdWRkAgkPD2QWAh8GBUBidXR0b25fY2xpY2sodGhpcywnY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9jdGwwMF9idG5EYW5nTmhhcCcpZAILDw8WAh8CBQ3EkMSDbmcgTmjhuq1wZGQCDQ8PFgIfBWhkZAIPDw8WAh8FaGRkAgkPZBYCAgEPDxYCHwIFbUNvcHlyaWdodCDCqTIwMDkgSOG7jWMgVmnhu4duIEPDtG5nIE5naOG7hyBCxrB1IENow61uaCBWaeG7hW4gVGjDtG5nLUPGoSBT4bufIE1p4buBbiBC4bqvYy4gUXXhuqNuIGzDvSBi4bufaSBkZGS2JNDgBreCczRPCBl8M2SpYD/2aw==',
#     '__VIEWSTATEGENERATOR': 'CA0B0334',
#     'ctl00$ContentPlaceHolder1$ctl00$txtTaiKhoa': info.username(),
#     'ctl00$ContentPlaceHolder1$ctl00$txtMatKhau':info.password(),
#     'ctl00$ContentPlaceHolder1$ctl00$btnDangNhap': 'Đăng Nhập'
# }
def show(payload):
    with requests.Session() as s:
        # Login to training management website PTIT
        response = s.post(login_url, data=payload)
        ans = ""
        lst = list()
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        #Get data from exam makeup on training management website
        res = s.get(get_url)

        #Convert binary data to html with BeautifulSuop
        soup = BeautifulSoup(res.text, 'html.parser')

        # Get the html data in the scoreboard section
        id_data = soup.find(id = "ctl00_ContentPlaceHolder1_ctl00_div1", class_ = 'GridViewContainer')

        # Get html data from view-table class where there are subtags with test score data
        table_data = id_data.find('table',class_ = "view-table")

        #Get data from rows containing titles, subjects and test scores
        tr_data = table_data.find_all('tr')
        #Get and print test score data
        cnt = 0
        ok = 0
        for i in range(len(tr_data) - 8):
            #Extract data from the td subcard of the tr card, which contains the score columns, subject names,...
            td_data = tr_data[i].find_all('td')
            if cnt == 0:
                ans += td_data[0].text + " | "
                ans += td_data[1].text + " | "
                ans += td_data[2].text + " | "
                ans += td_data[len(td_data)-5].text + " | "
                for j in range(len(td_data) - 3, len(td_data)):
                    ans += td_data[j].text + " | "
                ans += '\n----------------------------------------------------------------------------------------------' + '\n'
                cnt += 1
                continue
            if cnt == 1:
                ans += td_data[0].text + '\n'
                cnt += 1
                lst.append(ans)
                ans = ""
                continue

            if len(td_data) > 2:
                ans += td_data[0].text + " | "
                ans += td_data[1].text + " | "
                ans += td_data[2].text + " | "
                ans += td_data[len(td_data)-5].text + " | "

                # print(td_data[1].text, end='\t')
                # print(td_data[2].text, end='\t')
                # print(td_data[len(td_data) - 5].text, end='\t')
                for j in range(len(td_data) - 3, len(td_data)):
                    # Print the score data of each column
                    # print(td_data[j].text, end = '\t')
                    ans += td_data[j].text + " | "
            else:
                ok += 1
                if ok == 1 and cnt == 2 and '-' in td_data[0].text:
                    ans += '\n----------------------------------------------------------------------------------------------' + '\n'
                    lst.append(ans)
                    ans = ""
                    ok  = 0
                    cnt += 1
                    ans += td_data[0].text
                    continue
                if ok == 5:
                    ans += '\n----------------------------------------------------------------------------------------------' + '\n'
                    lst.append(ans)
                    ans = ""
                    ok = 0
                for j in range(len(td_data)):
                    # Print the score data of each column
                    ans += td_data[j].text
            ans += '\n'
        lst.append(ans)
        return lst
# if _name_ == '_main_':
#     show()