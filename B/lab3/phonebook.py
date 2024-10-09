#!/usr/bin/env python

from genericpath import isfile
from pydoc import ispath
import sys
import os
from turtle import Turtle

PHONEBOOK_ENTRIES = "python_phonebook_entries"


def main():
    if len(sys.argv) < 2:
        exit(1)

    elif sys.argv[1] == "new":
        if len(sys.argv) !=4 :
            raise ValueError("Arguments Error!")
        else:
            name_ = sys.argv[2]
            number_ = sys.argv[3]
            with open(PHONEBOOK_ENTRIES,'a') as f:
                f.writelines(f"{name_},{number_}\n")

    elif sys.argv[1] == "list":
        if not os.path.isfile(PHONEBOOK_ENTRIES) or os.path.getsize(
                PHONEBOOK_ENTRIES) == 0:
            print("phonebook is empty")
        else:
            # YOUR CODE HERE #
            with open(PHONEBOOK_ENTRIES,'r') as f:
                for line in f:
                    print(f"{line}",end="")
    
    elif sys.argv[1] == "lookup":
        # YOUR CODE HERE #
        name_ = sys.argv[2]
        with open(PHONEBOOK_ENTRIES,'r') as f:
            for line in f:
                name,number = line.split(",")
                if name == name_:
                    print(f"{name_}'s num is {number}")
                    return
                print("NO SUCH NUMBER")
            
    elif sys.argv[1] == "remove":
        name_ = " ".join(sys.argv[2:])
        if not os.path.isfile(PHONEBOOK_ENTRIES):
            print("PHONEBOOK_ENTRIES IS EMPTY")
            return
        with open(PHONEBOOK_ENTRIES, 'r+') as f:
            lines = f.readlines()
            for line in lines:
                name, number = line.strip().split(",")
                if name == name_:
                    found = True
                    number = ""
                    print(f"Removed entry for {name_}")
            if found != True:
                print(f"NO FOUND {name_}")


    elif sys.argv[1] == "clear":
        # YOUR CODE HERE #
        if os.path.isfile(PHONEBOOK_ENTRIES):
            os.remove(PHONEBOOK_ENTRIES)
            print("Clear Contents")
        else:
            print("PHONEBOOK_ENTRIES IS EMTPY")

    else:
        name = " ".join(sys.argv[1:])
        with open(PHONEBOOK_ENTRIES, 'r') as f:
            lookup = "".join(filter(lambda line: name in line, f.readlines() ) )
            if lookup:
                print(lookup.strip())
            else:
                print(f"NO NUM FIND {name}")


if __name__ == "__main__":
    main()