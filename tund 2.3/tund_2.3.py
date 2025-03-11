print("Tere! Olen sinu uus sõber - KMI!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
kmi_soov=input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
try:
    kmi_soov=int(kmi_soov)
    if kmi_soov==1:
        pikkus=int(input("Sisesta oma pikkus sentimeetrites: "))
        mass=float(input("Sisesta oma kehakaal kilogrammides: "))
        kmi=mass/((pikkus/100)**2)
        print(f"{nimi}! Sinu keha indeks on: {kmi:.1f})
        if kmi<16:
            print("Tervisele ohtlik alakaal")
        elif 16<=kmi<19:
            print("Alakaal")
        elif 19<=kmi<25:
            print("Normaalkaal")
        elif 25<=kmi<30:
            print("Ülekaal")
        elif 30<=kmi<35:
            print("Rasvumine")
        elif 35<=kmi<40:
            print("Tugev rasvumine")
        else:
            print("Tervisele ohtlik rasvumine")
    elif kmi_soov==0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Palun sisesta kehtiv valik (0 või 1).")
except:
    print("Vigane sisend! Palun sisesta kehtivad numbrid.")
print(f"Kohtumiseni, {nimi}! Igavesti Sinu, KMI!")
