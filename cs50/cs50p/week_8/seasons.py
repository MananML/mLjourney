from datetime import date
import inflect
import sys

class Time:

    @classmethod 
    def age(cls, date_of_birth):
        try:
            d = map(int, date_of_birth.split("-"))
            year, month, day = d

            duration = date.today() - date(year, month, day)
            return duration.days * 24 * 60
        
        except ValueError:
            sys.exit("Invalid input")

def main():

    user_input= input("Date of Birth: ")
    print(get_age(user_input))


def get_age(date_of_birth):
    p = inflect.engine()
    word = p.number_to_words(Time.age(date_of_birth), andword="").capitalize()

    return f"{word} minutes"


if __name__ == "__main__":
    main()



"""





datetime.date(year, month, day)¶
classmethod date.today()¶

time.time()


import datetime as dt
delta = dt.timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
delta

lass datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)¶

> p.number_to_words(12345, group=1)
'one, two, three, four, five'
>>> p.number_to_words(12345, group=2)
'twelve, thirty-four, five'
>>> p.number_to_words(12345, group=3)
'one twenty-three, forty-five'
>>> p.number_to_words(1234, andword="")
'one thousand, two hundred thirty-four'
>>> p.number_to_words(1234, andword=", plus")
'one thousand, two hundred, plus thirty-four'
>>> p.number_to_words(555_1202, group=1, zero="oh")
'five, five, five, one, two, oh, two'
>>> p.number_to_words(555_1202, group=1, one="unity")
'five, five, five, unity, two, zero, two'
>>> p.number_to_words(123.456, group=1, decimal="mark")
'one, two, three, mark, four, five, six'



"""