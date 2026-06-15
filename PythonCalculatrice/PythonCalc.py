print("""
╔══════════════════════════════════════════════════════╗
║                                                      ║
║  ██╗   ██╗██╗  ████████╗██████╗  █████╗             ║
║  ██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗            ║
║  ██║   ██║██║     ██║   ██████╔╝███████║            ║
║  ██║   ██║██║     ██║   ██╔══██╗██╔══██║            ║
║  ╚██████╔╝███████╗██║   ██║  ██║██║  ██║            ║
║   ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝            ║
║                                                      ║
║   ██████╗ █████╗ ██╗      ██████╗    ██╗            ║
║  ██╔════╝██╔══██╗██║     ██╔════╝   ██╔╝            ║
║  ██║     ███████║██║     ██║        ██║             ║
║  ██║     ██╔══██║██║     ██║       ██╔╝             ║
║  ╚██████╗██║  ██║███████╗╚██████╗ ██╔╝             ║
║   ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝              ║
║                                                      ║
║   ┌────────────────────────────────────────────┐    ║
║   │  [1] + Additionner   [2] - Soustraire      │    ║
║   │  [3] * Multiplier    [4] / Diviser         │    ║
║   └────────────────────────────────────────────┘    ║
║                                                      ║
║     [ v1.0 ]  ·  Made with Python  ·  by Nadir Mahi ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
""")
nombre1 = input("entrez le premier nombre ici : ")


nombre2 = input("entrez le 2eme nombre ici : ")
operation = input("entrez une opération : ")

nombre1 = int(nombre1)
nombre2 = int(nombre2)
operation = int(operation)

if operation == 1:
    print(nombre1 + nombre2)
elif operation == 2:
    print(nombre1 - nombre2)
elif operation == 3:
    print(nombre1 * nombre2)
elif operation == 4:
    print(nombre1 / nombre2)



resultat = nombre1 + nombre2

print(nombre1, type(nombre1))
print("Voutre resultat est : ", resultat)
input("")
