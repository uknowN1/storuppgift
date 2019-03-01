import os
meny = 0

print("*** Välkommen till HA-programet ***")
print("Gör ett val i menyn:")
print("1. läs in fil")
print("2. hantera fil")
print("3. spara fil")
print("4. avsluta")

while meny != 4:
    try: 
        meny = int(input("meny val: "))
    except:
        print("du gjorde inte ett korekt val")
    
    if meny == 1:
        print("hej")
    elif meny == 2:
        print("hej")
    elif meny == 3:
        print("hej")
    else: 
        print(" ")