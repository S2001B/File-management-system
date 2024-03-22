from system_manager import FileSystem

def boot_system() -> None:
    file = input("[ OPTIONAL IF YOU USE SORT ] Place your file here: ")

    print(f"Chose [< move >] to move your file or [< copy >] to create a copied verion")
    print("You can also chose [< sort >] to sort all of your files at the same time")
    user_function_choice = input("Your choice: ").lower()
    
    system = FileSystem(file)

    if user_function_choice == "sort":
        system.sort_files()
        return 1

    match user_function_choice:
        case "move":
            system.move()
        case "copy":
            system.copy()
    return 0 

def main() -> None:
    boot_system()

if __name__ == "__main__":
    main()