import re
from colorama import Fore

def get_name(obj):
    obj = input(f"Enter {obj} name: ")
    return obj

def get_color():
    foreground_colors = [
        color for color in dir(Fore) if isinstance(getattr(Fore, color), str)
    ]
    color = input(f"Enter color: ")
    if color not in foreground_colors:
        print("No such color. Color was set to white")
        color = Fore.WHITE
    return Fore.color

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
