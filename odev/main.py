import plyer
from plyer import notification

def notify():
        notification.notify(
                title="UYARI MESAJI",
                message="BILGISAYARIMIZ HATA VERİYOR\nSORUNU DUZELTIN\tHata kodu: ABC123",
                toast = False,
                app_name="",
                app_icon ="",
                ticker ="",
                timeout=5)
notify()



