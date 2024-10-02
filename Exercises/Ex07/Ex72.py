from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import math


def main():
    fmt = "%Y-%m-%d"
    borrowDateStr = input("借書日期 (年-月-日): ")
    borrowDays = int(input("可借幾日: "))
    # 將datetime轉為date
    borrowDate = datetime.strptime(borrowDateStr, fmt).date()
    returnDate = borrowDate + timedelta(days=borrowDays)
    returnDateStr = date.strftime(returnDate, fmt)
    print(f"{returnDateStr} 前歸還")
    todayStr = date.strftime(date.today(), fmt)
    print(f"今天是 {todayStr}")
    # 計算今天與還書日差幾天，可使用timedelta或relativedelta
    delta = date.today() - returnDate
    # delta = relativedelta(dt1=date.today(), dt2=returnDate)
    # 可印出詳細差值除錯用
    # print(f"delta: {delta}")
    if delta.days < 0:
        print(f"您必須在 {abs(delta.days)} 天內歸還")
    elif delta.days == 0:
        print("您必須在今天內歸還")
    else:
        print(f"逾期天數: {math.fabs(delta.days)}")



main()