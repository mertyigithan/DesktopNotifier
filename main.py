# Kütüphaneleri yükle;
import time
from plyer import notification # https://pypi.org/project/plyer/

# Bildirimi ayarla;
uygulama = input("Bildirim göndermek istediğiniz uygulamanın adını giriniz: ")
baslik = input("Konu başlığını giriniz: ")
mesaj = input("Mesajınızı yazınız: ")
# bildirim göndermek istediğiniz uygulamanın ikonunu ".ico" formatında bu klasöre indirmeniz gerekiyor
notification.notify(title=baslik, message=mesaj, app_name=uygulama, app_icon="v.ico", timeout=6)

# Bildirimi şu kadar zaman sonra tekrarla;
time.sleep(30) # saniye