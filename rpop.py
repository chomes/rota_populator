#!/usr/bin/env python3
# author: chomes@github
# version: 3.1b minor fix to correct the times to start on night shift.
# Future version improvements: Classes and different rota patterns.  A re-write.
import configparser
from pathlib import Path
import csv
from datetime import datetime, timedelta


# help menu for 4 users
def help_menu_single():
    print('''
        Please add usernames to the list.. you can only add 4
        del - option to delete a user you added onto the list
        help - shows these options again''')


# help menu for 8 users
def help_menu_dual():
    print('''
            Please add usernames to the list.. you can only add 8
            If some shifts don't have users, just press enter to leave blank.
            del - option to delete a user you added onto the list
            help - shows these options again''')


# csv file was created to it's own function to allow it to be easily used for multiple functions and automation
def csv_creation(date, firstday, firstday_second, firstnight, firstnight_second,
                 thirdday, thirdday_second, fithday, fithday_second, dlsav):
    print("Config file saved, generating your csv file")
    # Checks if daylight savings is enabled or not
    if dlsav == "y":
        newdate = date.replace(hour=18, minute=50)
    else:
        newdate = date.replace(hour=19, minute=50)
    # creating csv file
    with open('shiftrota.csv', 'w') as csvfile:
        fieldnames = ['shift_date', 'shift_user']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        days = 0
        # While loop for populating 30 days worth of rota
        while days < 60:
            writer.writerow({'shift_date': newdate, 'shift_user': firstnight})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=12), 'shift_user': firstday})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=24), 'shift_user': firstnight_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=36), 'shift_user': thirdday})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=48), 'shift_user': firstday})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=60), 'shift_user': thirdday_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=72), 'shift_user': firstday_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=84), 'shift_user': fithday})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=96), 'shift_user': thirdday})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=108), 'shift_user': fithday_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=120), 'shift_user': thirdday_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=132), 'shift_user': firstnight})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=144), 'shift_user': fithday})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=156), 'shift_user': firstnight_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=168), 'shift_user': fithday_second})
            days += 1
            writer.writerow({'shift_date': newdate + timedelta(hours=180), 'shift_user': firstday})
            days += 1
            newdate = newdate + timedelta(hours=192)

        # informing user of completed csv
        print("Your csv file is now done, it should be in the same folder titled shiftrota")


# Function for manual rota populating, this is ran when no config is present.
def rotapopman():
    # While loop for setting the first date
    while True:
        poten_date = input("Please put in the date of the first person in the night shift yyyy/mm/dd: ")
        confirm_date = input("You have chosen the date of {} is this correct? (y/n) ".format(poten_date)).lower()
        if confirm_date == 'y':
            date = datetime.strptime(poten_date, '%Y/%m/%d')
            print("Ok, next we will get a list of names from you.")
            break
        else:
            continue
    # while loop for adding users
    # Depending on dual_shift answer, user will either input up to 4 or 8 users.
    usernames = []
    dual_shift = input("Do you have people working the same shift? (y/n): ").lower()
    if dual_shift == "n":
        help_menu_single()
        while len(usernames) < 4:
            add_user = input("> ").lower()
            if add_user == "help":
                help_menu_single()
                continue
            elif add_user == "del":
                del_user = input("Please state the user you want to delete: ").lower()
                usernames.remove(del_user)
                print("User {} has been deleted!".format(del_user))
                continue
            usernames.append(add_user)
            print("Username {} has been added to the list".format(add_user))
    else:
        help_menu_dual()
        while len(usernames) < 8:
            add_user = input("> ").lower()
            if add_user == "help":
                help_menu_dual()
                continue
            elif add_user == "del":
                del_user = input("Please state the user you want to delete: ").lower()
                usernames.remove(del_user)
                print("User {} has been deleted!".format(del_user))
                continue
            usernames.append(add_user)
            print("Username {} has been added to the list".format(add_user))

    print("Here are your list of users")
    for users in usernames:
        print(users)

    sanity_check = []

    # Loop for assigning shift positions
    while True:

        print("We now need to assign days and nights that they start working")
        print("Please state the first night shift and then the first day shift etc")
        print("If there's no user for the second day of that shift just press enter.")
        firstnight = input("List the user on the first night shift: ").lower()
        sanity_check.append(firstnight)
        firstnight_second = input("List the second user on the first night shift: ").lower()
        # If statement will populate second user if left blank.
        if firstnight_second == "" or dual_shift == "n":
            firstnight_second = firstnight
            sanity_check.append(firstnight_second)
        elif firstnight_second != "" or dual_shift != "n":
            sanity_check.append(firstnight_second)

        firstday = input("List the user on the first day shift: ").lower()
        sanity_check.append(firstday)
        firstday_second = input("List the second user on the first day shift: ").lower()
        # If statement will populate second user if left blank.
        if firstday_second == "" or dual_shift == "n":
            firstday_second = firstday
            sanity_check.append(firstnight_second)
        elif firstday_second != "" or dual_shift != "n":
            sanity_check.append(firstnight_second)

        thirdday = input("List the user on the third day shift: ").lower()
        sanity_check.append(thirdday)
        thirdday_second = input("List the second user on the third day shift: ").lower()
        # If statement will populate second user if left blank.
        if thirdday_second == "" or dual_shift == "n":
            thirdday_second = thirdday
        elif thirdday_second != "" or dual_shift != "n":
            sanity_check.append(thirdday_second)

        fithday = input("List the user on the 5th day shift: ").lower()
        sanity_check.append(fithday)
        fithday_second = input("List the second user on the 5th day shift: ").lower()
        # If statement will populate second user if left blank.
        if fithday_second == "" or dual_shift == "n":
            fithday_second = fithday
        elif fithday_second != "" or dual_shift != "n":
            sanity_check.append(fithday)

        # Check if all variables exist in list, if they don't it will start loop again.
        # Have made the code cleaner then before but will research a better way of doing this
        # perhaps with all/any function
        print("Checking users are in the list")
        confirmation = []
        for confirm in sanity_check:
            if confirm in usernames:
                confirmation.append(True)
            else:
                confirmation.append(False)

        if False in confirmation:
            print("Not all users are in the list, try again")
            continue
        else:
            print("Okay we now have everything we need, lets make the csv file")
            break

    # Daylight savings check
    print("One last thing, we need to check if it's daylight savings in america")
    dlsav = input("Please confirm if it's daylight savings or not (y/n): ").lower()
    print("Saving users to config file")
    config = configparser.ConfigParser()
    cfgfile = open('main.cfg', 'w')
    # Creating sections for config
    config.add_section('USERS')
    config.add_section('DATE')
    config.add_section('DAYLIGHT_SAVINGS')
    # Populating sections for config
    config.set('USERS', 'firstnight', firstnight)
    config.set('USERS', 'firstnight_second', firstnight_second)
    config.set('USERS', 'firstday', firstday)
    config.set('USERS', 'firstday_second', firstday_second)
    config.set('USERS', 'thirdday', thirdday)
    config.set('USERS', 'thirdday_second', thirdday_second)
    config.set('USERS', 'fithday', fithday)
    config.set('USERS', 'fithday_second', fithday_second)
    config.set('DATE', 'oncalldate', poten_date)
    config.set('DAYLIGHT_SAVINGS', 'america_daylight', dlsav)
    config.write(cfgfile)
    cfgfile.close()
    # Running csv function
    csv_creation(date, firstday, firstday_second, firstnight, firstnight_second,
                 thirdday, thirdday_second, fithday, fithday_second, dlsav)


# Function used for creating rota based on config
def rotapopauto():

    print("Loading the config and running the script")
    config = configparser.ConfigParser()
    config.read('main.cfg')
    # If statement to check if second user is blank, make second night variable = firstnight
    firstnight = config.get('USERS', 'firstnight')
    firstnight_second = config.get('USERS', 'firstnight_second')
    if firstnight_second == "":
        firstnight_second = firstnight
    firstday = config.get('USERS', 'firstday')
    firstday_second = config.get('USERS', 'firstday_second')
    if firstday_second == "":
        firstday_second = firstday
    thirdday = config.get('USERS', 'thirdday')
    thirdday_second = config.get('USERS', 'thirdday_second')
    if thirdday_second == "":
        thirdday_second = thirdday
    fithday = config.get('USERS', 'fithday')
    fithday_second = config.get('USERS', 'fithday_second')
    if fithday_second == "":
        fithday_second = fithday
    poten_date = config.get('DATE', 'oncalldate')
    date = datetime.strptime(poten_date, '%Y/%m/%d')
    dlsav = config.get('DAYLIGHT_SAVINGS', 'america_daylight')
    csv_creation(date, firstday, firstday_second, firstnight, firstnight_second,
                 thirdday, thirdday_second, fithday, fithday_second, dlsav)


# Checking config exists
cfgchk = Path('main.cfg')

if cfgchk.is_file():
    print("We have the config, lets go to the final steps")
    rotapopauto()
else:
    print("Config doesn't exist, doing manual work, we will also create a config at the end to automate this later")
    rotapopman()
