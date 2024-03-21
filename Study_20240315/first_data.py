import datetime
from datetime import datetime as dt

first_Date = dt.strptime('2024-03-15','%Y-%m-%d')
print(first_Date, type(first_Date), type('2024-03-15'))

print(first_Date + datetime.timedelta(days=100))