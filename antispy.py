import os
import sys
from pystyle import Colors
import time

blue = Colors.blue
cyan = Colors.cyan
red = Colors.red
green = Colors.green

os.system("title AntiSpy")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def spyfile():
    spylist = []
    with open("spylist.txt", "r") as file:
        for line in file:
            spylist.append(line.strip())
    return spylist

opts = f"""
{cyan}1. Add List {red}(WARNING THE CONTENT OF THE FILE hosts WILL BE OVERWRITTEN!!!)
{cyan}2. Remove List {red}(WARNING THE CONTENT OF THE FILE WILL BE DELETED)
{cyan}3. See File Content
"""
print(opts)

def addlist():
    try:
        print(f"{cyan}Adding List...")
        hosts = open("C:\\Windows\\System32\\Drivers\\etc\\hosts", "w")
        hosts.write("# List and tool made by Senity more info https://dsc.gg/senity | https://github.com/HWYkagiru\n")
        spylist = spyfile()
        for ip in spylist:
            hosts.write(f"{ip}\n")
        print(f"{green}Succes")
    except PermissionError:
        print(f"{red}Run As Admin!")
        
def remlist():
    try:
        print(f"{cyan}Removing List")
        hosts = open("C:\\Windows\\System32\\Drivers\\etc\\hosts", "w")
        hosts.write("# List and tool made by Senity more info https://dsc.gg/senity | https://github.com/HWYkagiru\n")
        print(f"{green}Done!")
    except PermissionError:
        print(f"{red}Run As Admin!")

def seehosts():
    try:
        with open("C:\\Windows\\System32\\Drivers\\etc\\hosts", "r") as hosts:
            hcont = hosts.read()

        with open("hostsc.txt", "w") as hostsc_file:
            hostsc_file.write(hcont)

        print("File Saved: ", os.path.abspath("hostsc.txt"))
    except PermissionError:
        print(f"{red}Run As Admin")


if __name__ == "__main__":
    while True:
        try:
            ch = input(f"{cyan}Enter a number: ")
            if ch == "1":
                addlist()
                input("Enter to exit...")
                break
            elif ch == "2":
                remlist()
                input("Enter to exit...")
                break
            elif ch == "3":
                seehosts()
                input("Enter to exit...")
                break
            else:
                print(f"{red}Invalid  Input!")
                time.sleep(0.4)
                clear()
        except KeyboardInterrupt:
            print(f"{red}\nexit...")
            time.sleep(0.4)
            break
