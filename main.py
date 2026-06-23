import time

from npmg_vacancy_check import check
from constants import URL
from notifier import send_email

timestamp = time.strftime("%Y/%m/%d %H:%M:%S")

if __name__ == "__main__":
    print("Проверка на страницата за свободни места в НПМГ: " + timestamp)

    msg_format = "\n--------------"  + timestamp + "--------------\n%s\n%s\n--------------------------------------------------------"
    page_diff = check()

    if page_diff:
        print(timestamp + " Страницата е обновена")
        msg = msg_format % (page_diff, "Провери на:" + URL)
        print(msg)
        send_email("Свободни места в НПМГ", msg)
    else:
        msg =   msg_format % ("Няма промяна на страницата за свободни места","")
        print(msg)
    with open("output/npmg_log.log", "a", encoding="utf-8") as f:
        f.write(msg)

