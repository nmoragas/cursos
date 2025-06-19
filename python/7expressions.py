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


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.match(pattern, ip)
    if match:
        for part in match.groups():
            if not 0 <= int(part) <= 255:
                return False
        return True
    return False




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
