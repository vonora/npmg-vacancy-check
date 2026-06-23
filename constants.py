import time

URL = "https://npmg.org/%d0%bf%d1%80%d0%b8%d0%b5%d0%bc-%d0%b2-%d1%81%d1%82%d0%b0%d1%80%d1%88%d0%b8-%d0%ba%d0%bb%d0%b0%d1%81%d0%be%d0%b2%d0%b5/"
# ====== НАСТРОЙКИ ======
EMAIL_SENDER = "martin.aronov@gmail.com"
EMAIL_PASSWORD = "bcvh nkmb yker bmno"   # НЕ нормалната парола!

EMAIL_RECEIVERS = [
    "dora.laskova@gmail.com"
]
#     "aronov@gmail.com",
#     "christian.aronov@gmail.com"

DATA_FILE = "output/last_page.txt"
DATA_FILE_MODIFIED = "output/last_page_modified_" + time.strftime("%Y%m%d") + ".txt"

