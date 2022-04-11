# Palauta nämä tehtävät 15.4 mennessä ....

print("Hello world!")

# Tiedon SYÖTTÖ ohjelmalle JA TULOSTUS näytölle (tekstikonsoliin)

text = input("Syötä nimesi?")

print("Hei", text)

float1 = float(input("Syötä liukuluku 1: "))
float2 = float(input("Syötä liukuluku 2: "))

print("Summa:", float1 + float2)
print("Erotus:", float1 - float2)
print("Tulo:", float1 * float2)

# ARITMETIIKKA

# Korkolaskuri

loan = float(input("Lainan määrä? (euroa) "))
interest = float(input("Koron määrä? (rosenttia) "))
loanperiod = float(input("Laina-aika? (vuosia) "))

interest_amount = loan * (interest/100) * loanperiod

print("Laina kasvaa korkoa yhteensä: ", interest_amount, " euroa")

# Maksimisykelaskuri

age = int(input("Ikä vuosina? "))

maxbeat = 220 - age

print("Maksimisykkeesi: ", maxbeat)

zone1 = str(maxbeat * 0.5) + " - " + str(maxbeat * 0.6)
zone2 = str(maxbeat * 0.6) + " - " + str(maxbeat * 0.7)
zone3 = str(maxbeat * 0.7) + " - " + str(maxbeat * 0.8)
zone4 = str(maxbeat * 0.8) + " - " + str(maxbeat * 0.9)
zone5 = str(maxbeat * 0.9) + " - " + str(maxbeat * 1.0)

print("Sykealueet: ")
print("Sykealue 1: ", zone1)
print("Sykealue 2: ", zone2)
print("Sykealue 3: ", zone3)
print("Sykealue 4: ", zone4)
print("Sykealue 5: ", zone5)

# EHTOLAUSEET (IF/ELSE)

# Painoindeksilaskuri

weight = float(input("Kehosi paino? (kilogrammoina) "))
height = float(input("Kehosi pituus? (senttimetreinä) "))

bmi = weight / ((height / 100) ** 2)

print("Painoindeksi: ", bmi)

# Kielitervehdys

hello_language = int(input("Millä kielellä haluat tervehdyksen? (1=suomi,2=ruotsi,3=englanti) "))

if(hello_language == 1):
    print("Moro nääs.")
elif(hello_language == 2):
    print("Hejjj.")
elif(hello_language == 3):
    print("Hello.")

# Kirjelaskuri

letter_weight = float(input("Paljonko kirjeesi painaa (grammoissa): "))
letter_price = 1.95

if(20 <= letter_weight < 100):
    letter_price = 1.95
elif(100 <= letter_weight < 500):
    letter_price = 3.90
elif(500 <= letter_weight < 2000):
    letter_price = 7.80
elif(2000 <= letter_weight):
    letter_price = "Virhe! Kirje voi painaa max 2000.0 grammaa."

print("Kirjeen lähetys maksaa (euroa): ", letter_price)

# Käypähoito Varfariini

inr_value = float(input("INR-arvo? "))

if(inr_value < 1.5):
    print("Lisää viikkoannosta 15 %, toista INR-määritys 1–2 viikon päästä.")
elif(1.5 <= inr_value < 2):
    print("Lisää viikkoannosta 10 %, jos INR alenee toistuvissa mittauksissa tai kaksi peräkkäistä arvoa 1,5–1,9. INR-määritys 1–2 viikon päästä.")
elif(2 <= inr_value < 3):
    print("Ei muutosta.")
elif(3 <= inr_value < 4):
    print("Älä keskeytä varfariinia, pienennä viikkoannosta 10 %, jos INR noususuunnassa tai kaksi peräkkäistä arvoa 3–3,9.")
elif(4 <= inr_value < 5):
    print("Yhden päivän varfariinin käytön tauko. Pienennä viikkoannosta 10 %, määritä INR 1–2 viikon päästä.")
elif(5 <= inr_value < 9):
    print("Keskeytä varfariinin annostelu. Anna suun kautta K-vitamiinia, jos potilaan vuotoriski on suuri. Jos INR on vuorokauden kuluttua edelleen korkea, anna lisää 1–2 mg K-vitamiinia. Aloita varfariinin annostelua 15 % pienemmällä annoksella, kun INR on hoitoalueella. Määritä INR viikottain, kunnes antikoagulaatiotaso on vakaa.")
elif(9 <= inr_value):
    print("Keskeytä varfariinin käyttö ja anna suun kautta 5–10 mg K-vitamiinia. Seuraa potilaan vointia tarkasti ja anna tarvittaessa lisää K-vitamiinia.")
else:
    print("Virheellinen arvo.")