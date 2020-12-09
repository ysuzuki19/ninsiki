from datetime import datetime
import pytz

def now():
  time_zone = pytz.timezone('Japan')
  date = datetime.now(time_zone)
  return date.strftime('%Y_%H_%M_%S')
