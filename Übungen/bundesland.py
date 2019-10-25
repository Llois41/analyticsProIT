bundesland_input = input("Bundesland eingeben...: ")
bundeslaender = {"Berlin": "Berlin", "Brandenburg": "Potsdam", "Bayern": "München", "Baden Württemberg": "Stuttgart"}

for bundesland in bundeslaender:    
    if bundesland_input == bundesland:
        print("Die Hauptstadt ist: " + bundeslaender[bundesland])

