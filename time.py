from datetime import datetime
import pytz

tz_PST = pytz.timezone('US/Pacific') 
datetime_PST = datetime.now(tz_PST)
print("PST:", datetime_PST.strftime("%H:%M:%S"))

tz_IST = pytz.timezone('Asia/Kolkata')
datetime_IST = datetime.now(tz_IST)
print("IST:", datetime_IST.strftime("%H:%M:%S"))

print('This is a small change to time.py')
print('Another print statement')
