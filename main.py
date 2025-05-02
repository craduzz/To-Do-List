from interface import Interface


def main():
    menu = Interface()
    selection = menu.welcome_screen()

    while True:
        if selection == '1':
            menu.add_task()
        elif selection == '2':
            menu.modify_task('UPDATE')
        elif selection == '3':
            menu.modify_task('DELETE')
        elif selection == '4':
            menu.modify_task('VIEW')
        elif selection == '5':
            exit()
        selection = menu.welcome_screen()





if __name__ == "__main__":
    main()