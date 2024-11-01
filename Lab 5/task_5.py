from datetime import date

d1 = date.today()
ds = str(d1)
year, month, day = ds.split('-')
formatted_date = f"{day}/{month}/{year}"

print("Date in Day/Month/Year format:", formatted_date)