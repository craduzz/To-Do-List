from data import Data

class Interface:
    #Text colours
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    BLUE = '\033[94m'

    def __init__(self):
        pass

    #To-do list main menu
    def welcome_screen(self):
        self.divisor()
        print(f"{self.YELLOW}To-do List by Carlos Ruiz")
        self.divisor()
        print(f"{self.WHITE}Choose an option:")
        print(f"{self.GREEN}1.{self.WHITE} Add a new task")
        print(f"{self.GREEN}2.{self.WHITE} Update tasks")
        print(f"{self.GREEN}3.{self.WHITE} Delete a task")
        print(f"{self.GREEN}4.{self.WHITE} View tasks")
        print(f"{self.GREEN}5.{self.RED} Exit")
        print(f"{self.BLUE}Enter your choice: ")
        selection = input()

        if selection not in ['1', '2', '3', '4', '5']:
            print(f"{self.RED}Invalid option. Please try again.")
            selection = self.welcome_screen()
        return selection

    #add task interface
    def add_task(self):
        data = Data()

        self.divisor()
        print(f"{self.BLUE}Title: {self.WHITE}")
        title = input()
        print(f"{self.BLUE}Description: {self.WHITE}")
        description = input()
        #todo validate date input and convert it to datetime
        print(f"{self.BLUE}Expiration date (Format: DD/MM/YYYY):{self.WHITE}")
        expiration_date = input()
        data.add_task_json(title, description, expiration_date)
        self.divisor()

    #Simple method to display on the screen all notes
    def view_all_tasks(self):
        tasks = Data().get_task_json()
        i = 1
        self.divisor()
        for task in tasks:
            print(f"{self.GREEN}{i}.- {self.WHITE}{task}")
            i += 1
        self.divisor()
        return tasks

    #delete & update functionality
    def modify_task(self,action:str):
        data = Data()

        self.divisor()
        print(f"{self.BLUE}Select task to {action}:")
        tasks = self.view_all_tasks()
        print(f"{self.GREEN}Press enter to return to main menu.")
        self.divisor()
        selection = input()

        try:
            selection = int(selection)
        except:
            return
        titles = list(tasks.keys())
        selection = selection - 1

        if selection not in range(0,len(titles)+1):
            print(f"{self.RED}Invalid option. Please try again.")
        else:
            if action == 'DELETE':
                data.delete_task_json(titles[selection],tasks)
            elif action == 'UPDATE':
                self.visualize_tasks(titles[selection],tasks,action)
            elif action == 'VIEW':
                self.visualize_tasks(titles[selection],tasks,action)
            else:
                print(f"{self.RED}ERROR.")
                return

    #displays the details of the selected tasks and the selections of the selected action
    def visualize_tasks(self,title:str,tasks:dict,action:str):
        data = Data()

        print(f"{self.BLUE}1.- Title: {self.WHITE}{title}")
        print(f"{self.BLUE}2.- Description: {self.WHITE}{tasks[title]['Description']}")
        print(f"{self.BLUE}3.- Expiration date: {self.WHITE}{tasks[title]['Expiration']}")

        #sets the visuals of the status code
        status = tasks[title]['Status']
        color = self.WHITE
        if status == 'CREATED':
            color = self.PURPLE
        elif status == 'IN_PROGRESS':
            color = self.YELLOW
        elif status == 'COMPLETED':
            color = self.GREEN
        elif status == 'EXPIRED':
            color = self.RED

        print(f"{self.BLUE}4.- Status: {color}{tasks[title]['Status']}")
        if action == 'UPDATE':
            print(f"{self.BLUE}5.- Return to main menu")
        if action == 'VIEW':
            print(f"{self.GREEN} Press enter to return")
            self.divisor()
            input()
            self.modify_task(action)
            return
        self.divisor()
        print(f"{self.WHITE}Enter your choice: ")
        selection = input()

        if selection not in ['1', '2', '3', '4','5']:
            print(f"{self.RED}Invalid option. Please try again.")
            self.visualize_tasks(title,tasks,action)
        else:
            if selection == '1':
                new_title = self.edit_title()
                if title != new_title:
                    tasks[new_title] = tasks[title]
                    del tasks[title]
                    data.update_task_title_json(tasks)
                else:
                    print(f"{self.YELLOW}Title is already the same. No changes were made. \n")
                self.divisor()

            elif selection == '2':
                new_description = self.edit_description()
                data.update_task_json(title,tasks,new_description,"Description")
            elif selection == '3':
                new_expiration = self.edit_expiration()
                data.update_task_json(title,tasks,new_expiration,"Expiration")
            elif selection == '4':
                new_status = self.edit_status()
                data.update_task_json(title,tasks,new_status,"Status")
            elif selection == '5':
                return
            else:
                print(f"{self.RED}ERROR.")
            print(f"{self.GREEN}The task has been updated! \n")
            self.divisor()
        self.visualize_tasks(title,tasks,action)

    #Creates a new key with the same values of the object to modify and deletes the previous one, if the key is the same do nothing
    def edit_title(self):
        print(f"{self.BLUE}Enter new title: ")
        new_title = input()
        return new_title

    #Modifies the description field
    def edit_description(self):
        print(f"{self.BLUE}Enter new description: ")
        new_description = input()
        return new_description

    #Modifies the expiration date field
    def edit_expiration(self):
        print(f"{self.BLUE}Enter new expiration date (Format: DD/MM/YYYY):")
        new_expiration = input()
        return new_expiration

    #Modifies the status with a selection of available statuses for the task
    def edit_status(self):
        label = ''
        print(f"{self.BLUE}Select new status: ")
        print(f"{self.WHITE}1.- {self.PURPLE}Created")
        print(f"{self.WHITE}2.- {self.YELLOW}In progress")
        print(f"{self.WHITE}3.- {self.GREEN}Completed")
        print(f"{self.WHITE}4.- {self.RED}Expired")
        new_status = input()
        if new_status not in ['1','2','3','4']:
            print(f"{self.RED}Invalid option. Please try again.")
            self.edit_status()
        else:
            if new_status == '1':
                label = 'CREATED'
            elif new_status == '2':
                label = 'IN_PROGRESS'
            elif new_status == '3':
                label = 'COMPLETED'
            elif new_status == '4':
                label = 'EXPIRED'

        return label

    #Simple method for visual console lines to declutter the code
    def divisor(self):
        print(f"{self.BLUE}{"-"*40}")