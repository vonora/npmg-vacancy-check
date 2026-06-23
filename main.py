import time

from npmg_vacancy_check import check
from constants import URL
from notifier import send_email

timestamp = time.strftime("%Y/%m/%d %H:%M:%S")

if __name__ == "__main__":
    print("Проверка на страницата за свободни места в НПМГ: " + timestamp)
    page_diff = check()

    if page_diff:
        print(timestamp + " Страницата е обновена")
        msg = "\n" + timestamp + "\n" + page_diff + "\n Провери на:" + URL
        print(msg)
        send_email("Свободни места в НПМГ", msg)
    else:
        msg =   "\n" + time.strftime("%Y/%m/%d %H:%M:%S") + f" Няма промяна на страницата за свободни места\n"
        print(msg)
    with open("output/npmg_log.log", "a", encoding="utf-8") as f:
        f.write(msg)