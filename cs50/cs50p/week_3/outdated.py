
DATES =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def standard(date):
    while True:
        try:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)
            if month <= 12 and day <= 31:
                return f"{year}-{month:02}-{day:02}"
            else:
                break

        except ValueError:
            try:
                month_date, year = date.split(",")
                month, day = month_date.split(" ")

                day, year = int(day), int(year)
            
                if month.title() in DATES:
                    month_index = DATES.index(month.title()) + 1
                    if day <= 31:
                        return f"{year}-{month_index:02}-{day:02}"
                    else:
                        break
                else:
                    break    
            except ValueError:
                break
            
def main():
    while True:
        date = input("Date: ")
        stan_dard = standard(date)
        if stan_dard != None: 
            print(stan_dard)
            break
    

main()