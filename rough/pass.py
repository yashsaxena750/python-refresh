import sys

class passd:
    def __init__(self,pwd):
        # Variables to track password complexity
        uc = lc = dc = sc = 0
        self.pwd = pwd

        # Special characters list
        sclist = ['!', '@', '#', '$', '%', '^', '&', '*']

        # Check password length
        if not (8 <= len(self.pwd) <= 20):
            print("Weak Password")
            sys.exit(-1)

        # Check password character types
        for p in self.pwd:
            if p.isupper():
                uc += 1
            elif p.islower():
                lc += 1
            elif p.isdigit():
                dc += 1
            elif p in sclist:
                sc += 1
            elif p.isspace():
                print("Can't contain spaces")
                sys.exit(-1)

        # Check if all complexity requirements are met
        if uc >= 1 and lc >= 1 and dc >= 1 and sc >= 1:
            print("Good Password")
        else:
            print("Weak Password")

if __name__ == "__main__":

    pwd = input("Enter a password: ")  # Taking user input
    p = passd(pwd)
