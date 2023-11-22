import importlib
import os

from UI.menu import Menu
from UI.menu_item import Item
import data.lab7.main as lab7
# import data.lab7.tests.main as lab7

def main():
    labs = [f for f in os.listdir("data") if os.path.isdir(os.path.join("data", f))]
    labs.sort()

    labs_menu = Menu("Labs Menu")
    
    for index, lab in enumerate(labs, start=1):
        module = importlib.import_module(f'data.{lab}.main')
        labs_menu.add_item(Item(str(index), f'Lab {index} ', module.__main__))

    labs_menu.add_item(Item(0, "Exit"))
    labs_menu.run()

# if __name__ == "__main__":
    # main()
lab7.__main__()








# pattern = re.compile(r'\b(?:genres|track|artist)\s*=\s*([^;]+)(?:;|$)')

# def parse_user_input(user_input):
#     result_dict = {'genres': [], 'track': [], 'artist': []}
    
#     pattern = re.compile(r'\b(genres|track|artist)\s*=\s*([^;,]+)(?:;|$)')
#     matches = pattern.findall(user_input)

#     for key, value in matches:
#         result_dict[key].extend(map(str.strip, value.split(',')))

#     return result_dict

# user_input1 = "genres=pop"
# user_input2 = "track=some-track"
# user_input3 = "artist=artist1, artist2"
# user_input4 = "genres=pop, rock; track=some-track; artist=artist1, artist2"
# user_input5 = "artist=artist1, artist2; track=some-track"
# user_input6 = "genres=pop; track=some-track1, some-track2"
# user_input7 = "genres=pop; artist2=some-track1, some-track2"

# import re

# pattern = re.compile(r'\b(genres|track|artist)\s*=\s*([^;]+)(?:;|$)')

# user_inputs = [
#     "genres=pop",
#     "track=some-track",
#     "artist=artist1, artist2",
#     "artist=artist1, artist2; track=some-track",
#     "genres=pop, rock; track=some-track; artist=artist1, artist2",
#     "genres=pop; track=some-track1, some-track2",
#     "genres=pop; artist2=some-track1, some-track2"
# ]

# results = []

# for user_input in user_inputs:
#     matches = pattern.finditer(user_input)
#     result = {'genres': [], 'track': [], 'artist': []}
    
#     for match in matches:
#         category, values = match.groups()
#         result[category].extend([value.strip() for value in values.split(',')])
    
#     results.append(result)
#     print(result)


# print(results)

