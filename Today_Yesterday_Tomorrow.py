from datetime import datetime,timedelta
def TodayTomorrowYesterday(today):
    yesterday=today-timedelta(1)
    print("Yesterday:{0} {1}".format(yesterday.strftime("%d-%m-%Y"),yesterday.strftime("%A")))
    present_day=today
    print("Present day:{0} {1}".format(present_day.strftime("%d-%m-%Y"),present_day.strftime("%A")))
    tomorrow=today+timedelta(1)
    print("Tomorrow:{0} {1}".format(tomorrow.strftime("%d-%m-%Y"),tomorrow.strftime("%A")))
today=datetime.now()
TodayTomorrowYesterday(today)
