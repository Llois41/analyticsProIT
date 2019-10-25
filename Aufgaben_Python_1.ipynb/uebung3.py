color = input("Bitte geben Sie eine Farbe ein: ...")
color.lower()
if color=="schwarz" or color=="grau":
    print("Die Farbe ist etwas langweilig")
elif color[0]=="b" or color[0]=="g":
    print("Das ist eine schöne Farbe :)")