"""
chạy file https://github.com/ohidurbappy/ScriptKiddy/blob/main/python/AlarmClock.py cả trên jupyter notebook và pycharm
đối với jupyter notebook: lần lượt copy các dòng lệnh rồi dán vào các ô code
đối với pycharm: tạo mới 1 file .py, copy cả tất cả code rồi dán vào rồi chạy debug
    chú ý: đặt break point ở dòng 27, khi nào code chạy đến break point thì chụp ảnh màn hình để nộp bài tập

Enter the number of minutes you would like to sleep for:  # gõ số phút muốn ngủ vào, xong ấn Enter (tức là số phút mà sau đó sẽ báo thức); ví dụ gõ 5
Enter the number of hours you would like to sleep for:  # gõ số giờ muốn ngủ vào, xong ấn Enter (tức là số giờ mà sau đó sẽ báo thức); ví dụ gõ 1
nó sẽ hỏi lại 1 lần nữa Would you like to set this alarm? [Y/N]>?  # gõ Y để xác nhận
như phía trên thì đặt breakpoint ở dòng số 27, chạy debug rồi để máy tính chạy trong 1 tiếng 5 phút rồi quay lại chụp màn hình là được (nên có cách khác, con số 1 tiếng 5 phút phía trên rất dở) (ngoài ra, nếu đặt breakpoint ở dòng số 23 rồi Step Over (F8) dần dần để xem nó chạy thì rất hoan nghênh)
"""
import time, winsound, sys  # , datetime
from datetime import datetime, timedelta

frequency = 2500
duration = 2000

currentTime = time.strftime("%H:%M:%S")

print("")
print("Currently it is:", currentTime)
minutesOfSleep = int(input("Enter the number of minutes you would like to sleep for:"))
hoursOfSleep = int(input("Enter the number of hours you would like to sleep for:"))
print("")

Alarm = (datetime.now() + timedelta(hours=hoursOfSleep) + timedelta(minutes=minutesOfSleep)).strftime('%H:%M:%S')
print("You will be woken up at:", Alarm)
yesOrNo = str(input("Would you like to set this alarm? [Y/N]")).lower()
print("")

while yesOrNo == "y" or yesOrNo == "yes":

    while currentTime != Alarm:
        print("Currently:", time.strftime("%H:%M:%S"))
        currentTime = time.strftime("%H:%M:%S")
        time.sleep(1)
        if currentTime == Alarm:
            print("Wake up!")
            for i in range(30):
                winsound.Beep(frequency, duration)
            sys.exit(0)

