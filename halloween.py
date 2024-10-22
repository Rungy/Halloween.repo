# halloween.py

# Fråga användaren om deras favorit halloween karaktär
karaktar = input("Vilken är din favorit-Halloween-karaktär? (vampyr, zombie, spöke): ").lower()

# Använd en if-sats för att ge ett svar baserat på användarens val
if karaktar == "vampyr":
    print("Blod är livet!")
elif karaktar == "zombie":
    print("Hjärnor... hjärnor...")
elif karaktar == "spöke":
    print("Buuuu!")
elif karaktar == "varulv":
    print("Månen är på din sida!")
elif karaktar == "Mummy":
    print("Määäääh")
elif karaktar == "troll":
    print("Troll jävel.")
elif karaktar == "trollkarl":
    print("Wow Magi!")
else:
    print("Det låter som en spännande karaktär!")

#Fråga användaren om deras favorit godis
godis = input("Vad är din favorit godis?").lower()

#ännu en if-sats för att ge ett svar baserat på användarens val
if godis == "twix":
    print("Såja så ska de låta")
elif godis == "snicker":
    print("Bra men it bäst.")
else:
    x = 0
    while x < 5:
        x = x + 1
        print("Bläh!")

