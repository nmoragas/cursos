# EX·ERCICI 1

import re
import sys
 
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^[F0-9]{3}.[F0-9].[F0-9].[F0-9]"
    match = re.search(pattern, ip)
    

    if match:
        primer, segon, tercer , quart= ip.split(".")
        n_primer = int(primer)

        if n_primer > 255:
            return "False"
        else:
            return "True"
    else:
        return "False" 
   



if __name__ == "__main__":
    main()

#####################################################################################################################################################################



# EXRECICI 2

'''
inputs: 
http://youtube.com/embed/xvFZjo5PgG0
https://youtube.com/embed/xvFZjo5PgG0
https://www.youtube.com/embed/xvFZjo5PgG0


"harvard\.edu", utilitzeu r"harvard\.edu". -> per evitar problemes amb \

# exemple input: <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#exeple resultat: https://youtu.be/xvFZjo5PgG0
'''

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    

    
    pattern = r'src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    match = re.search(pattern, s)
    

    if match:
        video_id = match.group(2)  # segon grup del match segons ()
        return f"https://youtu.be/{video_id}"
    else:
        return "False"


if __name__ == "__main__":
    main()




####################3

# EXERCICI 3:
import re
import sys


dictionary = {
    "12 AM": "00",
    "1 AM": "01",
    "2 AM": "02",
    "3 AM": "03",
    "4 AM": "04",
    "5 AM": "05",
    "6 AM": "06",
    "7 AM": "07",
    "8 AM": "08",
    "9 AM": "09",
    "10 AM": "10",
    "11 AM": "11",
    "12 PM": "12",
    "1 PM": "13",
    "2 PM": "14",
    "3 PM": "15",
    "4 PM": "16",
    "5 PM": "17",
    "6 PM": "18",
    "7 PM": "19",
    "8 PM": "20",
    "9 PM": "21",
    "10 PM": "22",
    "11 PM": "23"
}


def main():
    print(convert(input("Hours: ")))

def convert(s):
   # pattern = r'(\d{1,2})(:\d{2})?\s(AM|PM)\s+to\s+(\d{1,2})(:\d{2})?\s(AM|PM)'
    pattern = r'^(\d{1,2})(:\d{2})?\s(AM|PM) to (\d{1,2})(:\d{2})?\s(AM|PM)$'
    match = re.search(pattern, s)

    if not match:
        raise ValueError("Format incorrecte")

    # Hora inicial
    h1 = match.group(1)
    m1 = match.group(2)[1:] if match.group(2) else "00"
    p1 = match.group(3)

    # Validació minuts inicial
    if not m1.isdigit() or int(m1) > 59:
        raise ValueError("Format incorrecte")

    h1_24 = dictionary.get(f"{h1} {p1}")
    if h1_24 is None:
        raise ValueError("Format incorrecte")

    # Hora final
    h2 = match.group(4)
    m2 = match.group(5)[1:] if match.group(5) else "00"
    p2 = match.group(6)

    # Validació minuts finals
    if not m2.isdigit() or int(m2) > 59:
        raise ValueError("Format incorrecte")

    h2_24 = dictionary.get(f"{h2} {p2}")
    if h2_24 is None:
        raise ValueError("Format incorrecte")

    return f"{h1_24}:{m1} to {h2_24}:{m2}"



if __name__ == "__main__":
    main()




# test
from working import convert
import pytest

def main():
    test_convert()
    test_error_to()
    test_error()

def test_convert():
    assert convert("6 AM to 8 PM") == "06:00 to 20:00"


def test_error_to():
    with pytest.raises(ValueError):
        convert("9:00 AM 5:00")

def test_error():
    with pytest.raises(ValueError):
        convert("9:67 AM to 5:00 PM")


if __name__ == "__main__":
    main()



###################

# exercici 4:
import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    entrada = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(entrada)



if __name__ == "__main__":
    main()


##### py_test:
from um import count

def main():
    test_um()


def test_um():
    assert count("hello um") == 1
    assert count("hello my name is") == 0
    assert count("um") == 1
    assert count("Um") == 1
    assert count("yummy") == 0



if __name__ == "__main__":
    main()


    
##########################################

#EXERCICI 6

# python3 -m pip install --user validators

import validators


def main():
    print(validation(input("What's your email address?: ")))


def validation(s):
    return validators.email(s) is True


if __name__ == "__main__":
    main()
