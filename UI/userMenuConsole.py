import UI.menuTemplates as m

def menu_console():
    m.printMenuTitle("MAIN MENU\n            NOTES JOURNAL")
    print("1. - Journal \n2. - Note by ID \n3. - Choose note by date"
          "\n4. - Note edit \n5. - Add note \n6.- Delete note \n7. - Exit")
    m.printMenuLine()
    print("\n Enter the menu item ")