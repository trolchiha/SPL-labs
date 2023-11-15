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
