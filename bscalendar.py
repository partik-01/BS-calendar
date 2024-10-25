import calendar
from datetime import *
from year_monthmap import bs_year as year ,events 
from tithi import calculate_tithi

months = ["Baishakh","Jestha","Ashadh","Shrawan","Bhadra","Ashwin","Kartik","Mangsir","Poush","Magh","Falgun","Chaitra"]
days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

starting_adyear=1943
starting_admonth=4
starting_adday=14

#starting bs mapping for AD
bs_year=2000
bs_month=1
bs_day=1

def ad_to_bs(ad_year,ad_month,ad_day):
    #starting bs mapping for AD
    bs_year=2000
    bs_month=1
    bs_day=1

    #calculating day difference
    diff_days=(date(ad_year,ad_month,ad_day)-date(starting_adyear,starting_admonth,starting_adday)).days    

    while diff_days>0:
        month_days=(year.get(str(bs_year))[bs_month-1])
        if diff_days >= month_days:
            bs_month +=1
            bs_day=1
            diff_days-=month_days
            if bs_month > 12:
                bs_year +=1
                bs_month=1
        else:
            bs_day +=diff_days
            diff_days=0
    return bs_year,bs_month,bs_day
        
def get_event(bs_month,bs_day):
    return events.get((bs_month,bs_day),"NO IMPORTANT EVENTS.")

#tithi calculation

#displaying output
if __name__=="__main__":
    print("enter the english date : ")
    ad_year=int(input("enter year : "))
    ad_month=int(input("enter month : "))
    ad_day=int(input("enter date : "))

    #tithi calculation
    tithi= calculate_tithi(ad_year,ad_month,ad_day)
    #adtobs
    bs_year,bs_month,bs_day=ad_to_bs(ad_year,ad_month,ad_day)
    print("-*"*40)
    print("-"*40)
    print(f"the BS date is : \n {bs_year} / {bs_month} / {bs_day}")
    print("-"*40)
    print(f"{bs_year} {months[bs_month-1]} {bs_day} , {days[calendar.weekday(ad_year,ad_month,ad_day)]}")
    print("-"*40)
    print("Special event : ",get_event(bs_month,bs_day))
    print("-"*40)
    print("Tithi : ",tithi)
    print("-"*40)
    print("current Time : ",datetime.now())
    print("-"*40)