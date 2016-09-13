import re
import sys
from person import Person

names_files = open("names.txt", encoding="utf-8")
data = names_files.read()
names_files.close()


class AddressBook:
    
    def search_entries(self):
        line = re.compile(r'''
        ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # Last and first names
        (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
        (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone number
        (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
        (?P<twitter>@[\w\d]*)?$ # Twitter handle
        ''', re.X|re.M)
        
        search_person = input("Enter the first or last name: ").title()
        person = Person()
        if any(search_person in names for names in line.findall(data)):
            for match in line.finditer(data):
                if search_person in match.groupdict()['name'].title().replace(',',''):
                    person.name = match.groupdict()['name']
                    person.email = match.groupdict()['email']
                    person.phone = match.groupdict()['phone']
                    person.job = match.groupdict()['job']
                    person.twitter = match.groupdict()['twitter']
                    print(person)
        else:
            next_step = input("{} was not found. Enter [y]es to try again or [q]uit to exit: ".format(search_person))
            if next_step.lower() == 'q':
                print("Thanks for using the Address Book Finder!")
                sys.exit()
            else:
                self.search_entries()
                
                
    def __init__(self):
        start_input = input("Welcome! Enter [s]earch to look up an address book entry or [q]uit to exit: ").lower()
        if start_input == 'q':
            print("Thanks for using the Address Book Finder!")
            sys.exit()
        else:
            repeat = True
            while repeat != 'q':
                self.search_entries()
                print('\n' + '=' * 20)
                repeat = input("Would you like to [s]earch or [q]uit? ").lower()
            print("Thanks for using the Address Book Finder!")
            sys.exit()

            
            
AddressBook()