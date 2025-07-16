# EXERCIC 1:

# inpute: date of birth in YYYY-MM-DD format  - oput: minutes
    # user was born at midnight (i.e., 00:00:00) - current time midnight
# datetime.date.today to get today’s date

# Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.




from datetime import date, datetime
import sys
import inflect

# data (any, mes, dia).

'''
class date:
    def __init__(self, any, mes, dia):
        self.any = any
        self.mes = mes
        self.dia = dia
'''



def main():
    
    neixement = data_input()
    minuts = contar_minuts(neixement)
    
    lletres = conversio_min_lletres(minuts)
    print(lletres)




def data_input():
    d_input = input("Date of Birth:")
    
    try:
        d_in_format = datetime.strptime(d_input, "%Y-%m-%d").date()
        return(d_in_format)

    except ValueError:
        sys.exit("Invalid date")


def contar_minuts(neixement):
    today_date = date.today()
    # contar minuts

    days_count = today_date - neixement
    # Total minuts (correcte)
    minutes = days_count.total_seconds() / 60
    return(minutes)


def conversio_min_lletres(minuts):
    p = inflect.engine()
    return p.number_to_words(minuts, andword="").capitalize()




if __name__ == "__main__":
    main()



