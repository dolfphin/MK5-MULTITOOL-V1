import pyfiglet

pytext = pyfiglet.figlet_format("M5K Multi-tool", font="larry3d", justify="left")
print(pytext)
disclaimer = 'I AM NOT RESPONSIBLE FOR THE USE OF ANY OF THESE PROGRAMS THAT ARE FOR MALICIOUS INTENT'
def menu():
    print("[1] Port Scanner")
    print("[2] Dos Attack")
    print("[3] Discord Server Nuker")
    print("DO NOT PUT A NUMBER THAT IS NOT ON THIS MENU")

menu()
option = int(input("Enter your choice:"))




while option != 0:
    if option == 1:
        exec(open('port.py').read())
    elif option == 2:
        exec(open('routerdos.py').read())
    elif option ==3:
        exec(open('nukebot.py').read())
    else:
        print("Invalid option")

print()
menu()
option = int(input("Enter your Choice:"))