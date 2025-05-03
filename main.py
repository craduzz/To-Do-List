from interface import Interface

# main method
def main():
    menu = Interface()

    #Displays the main menu
    selection = menu.welcome_screen()

    #Main program loop
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




# main function
if __name__ == "__main__":
    main()