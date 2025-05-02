import os
from data import Data

class Interface:
    #Text colours
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'
    #console clear command
    cls = os.system("clear||cls")




    def __init__(self):
        pass


    #To-do list main menu
    def welcome_screen(self):
        print(f"{self.YELLOW}To-do List by Carlos Ruiz")
        print(f"{self.BLUE}{"-"*40}")
        print(f"{self.WHITE}Choose an option:")
        print(f"{self.GREEN}1.{self.WHITE} Add a new task")
        print(f"{self.GREEN}2.{self.WHITE} View all tasks")
        print(f"{self.GREEN}3.{self.WHITE} Delete a task")
        print(f"{self.GREEN}4.{self.RED} Exit")
        print(f"{self.BLUE}Enter your choice: ")
        selection = input()

        if selection not in ['1', '2', '3', '4']:
            print(f"{self.RED}Invalid option. Please try again.")
            selection = self.welcome_screen()
        return selection

    #add task interface
    def add_task(self):
        data = Data()

        self.cls
        print(f"{self.BLUE}Title: ")
        title = input()
        self.cls
        print(f"{self.BLUE}Description: ")
        description = input()
        self.cls
        #todo validate date input and convert it to datetime
        print(f"{self.BLUE}Expiration date (Format: DD/MM/YYYY):")
        expiration_date = input()
        data.add_note(title, description, expiration_date)




    def view_all_tasks(self):
        pass

    def delete_task(self):
        pass