from interface import Interface


def main():
    menu = Interface()
    selection = menu.welcome_screen()

    while selection != '4':
        if selection == '1':
            menu.add_task()
        elif selection == '2':
            menu.view_all_tasks()
        elif selection == '3':
            menu.delete_task()
        elif selection == '4':
            exit()
        selection = menu.welcome_screen()





if __name__ == "__main__":
    main()