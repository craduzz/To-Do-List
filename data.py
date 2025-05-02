import json


class Data:

    GREEN = '\033[92m'

    #add tasks in the json
    def add_task_json(self, title, description, expiration):
        with open("Data/data.json", "r") as f:
            notes = json.load(f)
        notes[title] = {
            "Description": description,
            "Status": "CREATED",
            "Expiration": expiration
        }
        json_task = json.dumps(notes)
        with open("Data/data.json", "w") as f:
            f.write(json_task)

        print(f"{self.GREEN}Note added successfully!")
        input("Press a key to continue....")

    #get tasks from the json
    def get_task_json(self):
        with open("Data/data.json", "r") as f:
            notes = json.load(f)
        return notes

    #delete the selected task from the json and update it
    def delete_task_json(self, title,tasks):

        tasks.pop(title)
        json_task = json.dumps(tasks)
        with open("Data/data.json", "w") as f:
            f.write(json_task)

        print(f"{self.GREEN}Note deleted successfully!")
        input("Press a key to continue....")


    def update_task_title_json(self, tasks:dict):
        json_task = json.dumps(tasks)
        with open("Data/data.json", "w") as f:
            f.write(json_task)

    def update_task_json(self, title, tasks, new_text, label):
        tasks[title][label] = new_text
        json_task = json.dumps(tasks)
        with open("Data/data.json", "w") as f:
            f.write(json_task)
