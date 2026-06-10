from colorama import init, Fore, Style
init()

def display():
<<<<<<< HEAD
    message = f"{Fore.GREEN}Ceci est une {Fore.CYAN}modification{Style.RESET_ALL}"
=======
    message = f"{Fore.GREEN}Bonjour {Fore.CYAN}tout le monde !{Style.RESET_ALL}"
>>>>>>> b0e1e42 (Modification du message par Dev2)
    print(message)

if __name__ == "__main__":
    display()