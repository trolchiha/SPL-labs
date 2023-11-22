import re
from colorama import Fore

def get_name(obj):
    obj = input(f"Enter {obj} name: ")
    return obj

def get_color():
    list_of_colors = ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
    print("Available colors: red, green, yellow, blue, magenta, cyan, white")
    input_color = input(f"Enter color: ")
    color_name = input_color.upper() 
    if color_name not in list_of_colors:
        print("Invalid color")
        return "WHITE"
    return color_name

def get_user_input_recommendations():
    user_input = str(input("Enter parameters for recomendations\ne.g. genre=pop, rock; track=blinding lights; artist=the weeknd, metallica\n"))
    pattern = re.compile(r'\b(genre|artist|track)\s*=\s*([^;]+)(?:;|$)')

    user_recommendations = {'genre': [], 'artist': [], 'track': []}

    matches = pattern.finditer(user_input)

    if not matches:
        print("No matches")
        return 

    for match in matches:
        category, values = match.groups()
        user_recommendations[category].extend([value.strip() for value in values.split(',')])

    return user_recommendations
