def leapYear(year):
    if year%4==0 & year%100!=0:
        return f"{year} is a  leap year"
    elif year%100==0 and year%400==0:
        return f"{year} is leap year"
    else:
        return f"its not leap year {year}"
print(leapYear(2100))