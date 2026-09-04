class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    HEADER = "\033[38;5;118m"
    PREFIX = "\033[38;5;244m"
    WARNING = "\033[93m"
    ERROR = "\033[91m"
    FOLDER = "\033[33m"
    YN = "\033[36m"

class Term:
    CLEAR = "\033[2J\033[H"
    CLEAR_BELOW = "\033[J"

    @staticmethod
    def UP(n: int) -> str:
        return f"\033[{n}A"

config = {}


def print_header():
    print(Term.CLEAR, end="")
    print(("=" * 23) + f"\n==== {Color.HEADER}Healthe Hypr{Color.RESET} ====\n" + ("=" * 23))


def clear_viewport():
    print_header()


def add_yn(prompt: str) -> bool:
    ch = input(f"{Color.BOLD}{prompt}?{Color.RESET} {Color.YN}(y/N):{Color.RESET} ").strip().lower()
    return ch == 'y'


def add_prompt(title: str, options: list[tuple[str, str]], config_key: str, default_idx: int = 1):
    error_msg = ""
    while True:
        clear_viewport()
        print(f"\n{Color.BOLD}{title}:{Color.RESET}\n")
        
        for i, opt in enumerate(options, 1):
            name, desc = opt
            marker = f" {Color.HEADER}(default){Color.RESET}" if i == default_idx else ""
            
            print(f" {Color.YN}{i}){Color.RESET} {Color.BOLD}{name}{Color.RESET}{marker}")
            print(f"    {Color.PREFIX}{desc}{Color.RESET}\n")
            
        if error_msg:
            print(f"{Color.ERROR}{error_msg}{Color.RESET}\n")
            
        choice = input(f"{Color.YN}>>{Color.RESET} ").strip()
        
        if choice == "":
            config[config_key] = options[default_idx - 1][0]
            break
            
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(options):
                config[config_key] = options[idx - 1][0]
                break
                
        error_msg = f"Invalid choice '{choice}'. Please enter a number from 1 to {len(options)}."


def step_welcome():
    clear_viewport()
    print(f"\n{Color.PREFIX}This installer will guide you through the config\n"
          f"and let you select your best Healthy flavour.{Color.RESET}\n")
    print(f"{Color.WARNING}Warning:{Color.RESET} your {Color.FOLDER}~/.config/hypr{Color.RESET} folder will be completely overwritten.\n")
    
    if not add_yn("Proceed installation"):
        clear_viewport()
        print(f"\n{Color.ERROR}{Color.BOLD}Installation interrupted.{Color.RESET}\n")
        exit(1)


def step_select_flavour():
    flavours = [
        ("Everything", "Install all that template contains"),
        ("Guided", "Select which components to install manually"),
        ("Config only", "Install just config layout")
    ]
    add_prompt("Select your flavour", flavours, "flavour", default_idx=1)


def step_autoinstall():
    clear_viewport()
    print(f"\n{Color.BOLD}Installing...{Color.RESET}")


def step_confonly():
    clear_viewport()
    print(f"\n{Color.BOLD}Copying configs...{Color.RESET}")


def main():
    step_welcome()
    step_select_flavour()

    flavour = config.get('flavour')
    if flavour == 'Everything':
        step_autoinstall()
    elif flavour == 'Guided':
        pass
    elif flavour == 'Config only':
        step_confonly()

main()