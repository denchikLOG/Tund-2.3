print("Tere! Olen sinu uus sõber - Deniss!")
nimi=input("Palun sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
kmi_küsimus=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah=> ")
if kmi_küsimus=="1":
    pikkus=int(input("Palun sisesta oma pikkus sentimeetrites: "))
    mass=float(input("Palun sisesta oma kehakaal kilogrammides: "))
    pikkus_metes=pikkus/100
    kmi=mass/(pikkus_metes**2)
    print(f"{nimi}! Sinu keha indeks on:{kmi:.1f}")
    if kmi<16:
        hinnang="Tervisele ohtlik alakaal"
    elif 16<=kmi<19:
        hinnang="Alakaal"
    elif 20<=kmi<25:
        hinnang="Normaalkaal"
    elif 26<=kmi< 30:
        hinnang="Ülekaal"
    elif 31<=kmi<35:
        hinnang="Rasvumine"
    elif 36<=kmi<40:
        hinnang="Tugev rasvumine"
    else:
        hinnang="Tervisele ohtlik rasvumine"
    print(f"Hinnang: {hinnang}")
else:
    print("Kahju! See on väga kasulik info!")
    print()
print(f"Kohtumiseni,{nimi}! Igavesti Sinu, Python!")