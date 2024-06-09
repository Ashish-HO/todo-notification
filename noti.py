import win10toast
import time
import schedule

noti = win10toast.ToastNotifier()
print(type(noti))


def eat():
    noti.show_toast("bhat khane bela bhayo!!")


def study():
    noti.show_toast("oi padne bela bhayo.")


def water():
    noti.show_toast("pani khau babu.")


def sleep():
    noti.show_toast("sutni bela bhayo.")


def work():
    noti.show_toast("kam garni bela bhayo.")


# Routine you want to set
schedule.every().hour.do(water)
schedule.every().day.at("22:00").do(sleep)
schedule.every().day.at("08:30").do(eat)
schedule.every().day.at("11:00").do(study)
schedule.every().day.at("16:00").do(work)


while True:
    try:
        schedule.run_pending()
        time.sleep(4)
    except:
        pass
