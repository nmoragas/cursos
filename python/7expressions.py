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
    test_um_majucules()

def test_um():
    assert count("Hola bon dia um") == 1
    assert count("um") == 1
    assert count("AEio") == 0


def test_um_majucules():
    assert count("Hola bon dia Um") == 1
    
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
