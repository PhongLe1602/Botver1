import telebot
import testschedule
import schedule
import tuition
import anouce
import scheduleweek
import testscore

API_KEY = "5771573743:AAFtQxZ7GorK9vcNHrlEOIZxlTaSdUc64vo"
bot = telebot.TeleBot(API_KEY)
payload = schedule.payload
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! Welcome to our Bot!!')
    bot.send_message(message.chat.id, 'Nhập /help để xem hướng dẫn sử dụng!')
# instruction syntax /help
@bot.message_handler(commands = ['help'])
def help(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add( telebot.types.InlineKeyboardButton('Message the developer', url = 'telegram.me/CHP_chat_bot'))
    bot.reply_to(message, "Đây là bot chat telegram lấy dữ liệu từ trang QLDT của PTIT.\n" +
                 "Sau đây là 1 số cú pháp có thể sử dụng trên con bot này:\n" +
                 "/start : bắt đầu con bot\n" +
                 "/help : hiển thị hướng dẫn sử dụng\n" +
                 "/login : để bắt đầu đăng nhập QLDT bằng MSV và password. " +
                 "Sau khi nội dung yêu cầu nhập username và password nếu:\n" +
                 "      + thông báo Đăng nhập thành công là đã login thành công! Sẽ có các options: Điểm thi, Thông báo, Thời khóa biểu, Học phí và Lịch thi để lựa chọn.\n" +
                 "      + thông báo nhập sai username hoặc password thì nhập lại!\n" +
                 "/TKBT* : Thời khóa biểu theo tuần trong học kỳ. Dấu '*' là số từ 1 - 16.\n" +
                 "/exit : Đăng xuất tài khoản QLDT\n",
                 reply_markup=keyboard
                 )

def request(message):
    return True

#logout QLDT
@bot.message_handler(commands = ['exit'])
def exit(message):
    pay = schedule.payload
    pay['ctl00$ContentPlaceHolder1$ctl00$txtTaiKhoa'] = "B20DCCN338"
    pay['ctl00$ContentPlaceHolder1$ctl00$txtMatKhau'] = 'B23235345'
    schedule.show(pay)
    bot.send_message(message.chat.id, "Đăng xuất thành công!!")

#login QLDT
@bot.message_handler(commands = ['login'])
def loginQLDT(message):
    bot.send_message(message.chat.id, "Nhập MSV và Password (ngăn cách bởi 1 dấu space): ")
    @bot.message_handler(func=request)
    def send_mes(message):

        s = message.text.split()

        payload = schedule.payload
        try:
            payload['ctl00$ContentPlaceHolder1$ctl00$txtTaiKhoa'] = s[0]
            payload['ctl00$ContentPlaceHolder1$ctl00$txtMatKhau'] = s[1]
            # schedule.show(payload)
            if schedule.show(payload) != "-1":
                # Tạo một thông báo đăng nhập thành công và 3 options lựa chọn
                keyboard = telebot.types.InlineKeyboardMarkup()
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Thông báo', callback_data='TB'),
                    telebot.types.InlineKeyboardButton('Lịch thi', callback_data='LT')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Thời khóa biểu', callback_data='TKB'),
                    telebot.types.InlineKeyboardButton('Điểm thi', callback_data='DT')
                )
                keyboard.row(
                    telebot.types.InlineKeyboardButton('Học phí', callback_data='HP')
                )
                bot.send_message(message.chat.id, "Đăng nhập thành công!!!\n" +
                                 "Vui lòng chọn các lựa chọn sau:", reply_markup = keyboard)

                @bot.callback_query_handler(func=lambda call: True)
                def iq_callback(query):
                    data = query.data
                    if data.startswith('TKB'):
                        bot.send_message(message.chat.id, schedule.show(payload), reply_markup = keyboard)
                    elif data.startswith('LT'):
                        bot.send_message(message.chat.id, testschedule.show(payload), reply_markup = keyboard)
                    elif data.startswith('HP'):
                        bot.send_message(message.chat.id, tuition.show(payload), reply_markup = keyboard)
                    elif data.startswith('TB'):
                        bot.send_message(message.chat.id, anouce.showw(payload), reply_markup=keyboard)
                    elif data.startswith('DT'):
                        lst = testscore.show(payload)
                        for i in range(len(lst)-1):
                            bot.send_message(message.chat.id, lst[i])
                        bot.send_message(message.chat.id, lst[len(lst)-1], reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id, "Sai MSV hoặc password. Vui lòng nhập lại!!")
        except:
            bot.send_message(message.chat.id, "Sai cú pháp. Vui lòng nhập lại!!")

# scheduleweek
@bot.message_handler(commands = ['TKBT1', 'TKBT2', 'TKBT3', 'TKBT4', 'TKBT4', 'TKBT5', 'TKBT6', 'TKBT7', 'TKBT8',
                                 'TKBT9', 'TKBT10', 'TKBT11', 'TKBT12', 'TKBT13', 'TKBT14', 'TKBT15', 'TKBT16'])
def send(message):
    s = message.text[1:]
    try:
        str = scheduleweek.show(payload, s)
        if str == '-1':
            bot.send_message(message.chat.id, "Vui lòng đăng nhập!")
        else:
            bot.send_message(message.chat.id, str)
    except:
        bot.send_message(message.chat.id, "Lịch học bị lỗi!")

bot.polling()