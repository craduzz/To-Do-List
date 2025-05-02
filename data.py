import json


class Data:

    GREEN = '\033[92m'

    def add_note(self, title, description, expiration):
        with open("Data/data.json", "r") as f:
            notes = json.load(f)
        notes[title] = {
            "Description": description,
            "Status": "Created",
            "Expiration": expiration
        }
        json_note = json.dumps(notes)
        with open("Data/data.json", "w") as f:
            f.write(json_note)

        print(f"{self.GREEN}Note added successfully!")
        input("Press a key to continue....")

# #Testing
# d = {
#     "title3": {
#         "Description": "something",
#         "Status": "Created",
#         "Expiration": "20/12/2025"
#   }
# }
#
# with open("Data/data.json", "r") as f:
#     notes = json.load(f)
#
# print(notes)
# #notes.update(d)
# if "title3" in notes:
#     notes.pop("title3")
# else:
#     print("title3 not on notes")
#
# json_note = json.dumps(notes)
# with open("Data/data.json", "w") as f:
#     f.write(json_note)
#
