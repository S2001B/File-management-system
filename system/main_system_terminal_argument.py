import sys
from system_manager import FileSystem

def boot_system() -> None:
    if len(sys.argv) < 2:
        print("Use two arguments to boot the system: Mandatory[< system name >]  Optional[< file name >]")
        return
    
    print("Chose [< move >] to move your file or [< copy >] to create a copied verion")
    user_function_choice = input("Your choice: ").lower()

    system = validate_system_argv_input()

    if user_function_choice == "sort":
        system.sort_files()
        return 1

    match user_function_choice:
        case "move":
            system.move()
        case "copy":
            system.copy()
    return 0 
            
def validate_system_argv_input():
    try:
        if sys.argv[1]:
            return FileSystem(sys.argv[1])
    except IndexError: 
            return FileSystem(None)

def main() -> None:
    boot_system()

if __name__ == "__main__":
    main()