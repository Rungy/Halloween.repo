# halloween.py

# Fråga användaren om deras favorit halloween karaktär
karaktar = input("Vilken är din favorit-Halloween-karaktär? (vampyr, zombie, spöke, troll, trollkarl, varulv, mummy.):").lower()

# Använd en if-sats för att ge ett svar baserat på användarens val
if karaktar == "vampyr":
    print("Blod är livet!")
elif karaktar == "zombie":
    print("Hjärnor... hjärnor...")
elif karaktar == "spöke":
    print("Buuuu!")
elif karaktar == "varulv":
    print("Månen är på din sida!")
elif karaktar == "mummy":
    print("Määäääh")
elif karaktar == "troll":
    print("Troll jävel.")
elif karaktar == "trollkarl":
    print("Wow Magi!")
else:
    print("Det låter som en spännande karaktär!")

#Fråga användaren om deras favorit godis
godis = input("Vad är din favorit godis?: ").lower()

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

#En variabel för att fråga om användare är lätt skrämd
radsla = input("Är du lätt skrämd?: ").lower()

#En while loop som tvingar användaren att svara ja eller nej
while radsla not in ("ja", "nej"):
   radsla = input("Svara ja eller nej!: ").lower()


#En lista för att printa ut spooky message
message = ["Va","redo","för","att","bli","skrämd!"]
for ord in message:
    print(ord)
