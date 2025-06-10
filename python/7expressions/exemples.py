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
