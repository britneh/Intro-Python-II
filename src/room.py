# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = [item]

    def print_items(self):
        if not self.item:
            print("None")
        for i, item in enumerate(self.item):
            print(f'# {i+1}: {item}')


    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}'