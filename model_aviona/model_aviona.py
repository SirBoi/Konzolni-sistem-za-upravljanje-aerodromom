id = 0


"""
Funkcija kreira novi rečnik za model aviona i dodaje ga u rečnik svih modela aviona.
Kao rezultat vraća rečnik svih modela aviona sa novim modelom.
"""
def kreiranje_modela_aviona(
    svi_modeli_aviona: dict,
    naziv: str ="",
    broj_redova: str = "",
    pozicije_sedista: list = []
) -> dict:
    
    global id

    # Prazan unos
    for key in [naziv, broj_redova, pozicije_sedista]:
        if key == None or key == "":
            raise Exception(f"Provera za nedostajucu vrednost: {key}")

    # Provjera validnosti unesenih vrijednosti
    if not (type(naziv) == str and len(naziv) == 3):
        raise Exception("Vrednosti od aerodroma nisu dobre")

    if not (type(broj_redova) == int and broj_redova >= 0 and broj_redova <= 20):
        raise Exception("Vrednosti od aerodroma nisu dobre")

    if not (type(pozicije_sedista) == list and len(pozicije_sedista) >= 1 and len(pozicije_sedista) <= 8):
        raise Exception("Vrednosti od aerodroma nisu dobre")

    # Sve provjere su prosle, aerodrom se kreira
    svi_modeli_aviona[id] = {
        "naziv": naziv,
        "broj_redova": broj_redova,
        "pozicije_sedista": pozicije_sedista,
        "id": id,
    }

    id += 1

    return svi_modeli_aviona


"""
Funkcija čuva sve modele aviona u fajl na zadatoj putanji sa zadatim operatorom.
"""
def sacuvaj_modele_aviona(putanja: str, separator: str, svi_aerodromi: dict):
    
    with open(putanja, "w") as f:
        for aerodrom in svi_aerodromi:
            list_ = []

            for key in svi_aerodromi[aerodrom]:
                if (type(svi_aerodromi[aerodrom][key]) == list):
                    str_ = ""
                    for element in svi_aerodromi[aerodrom][key]:
                        str_ += str(element)
                    
                    list_.append(str_)

                else:
                    list_.append(str(svi_aerodromi[aerodrom][key]))

            line = separator.join(list_)

            f.writelines(line + '\n')


"""
Funkcija učitava sve modele aviona iz fajla na zadatoj putanji sa zadatim operatorom.
"""
def ucitaj_modele_aviona(putanja: str, separator: str) -> dict:
    
    dictionary_ = {}

    with open(putanja, "r") as f:
        for line in f.readlines():
            line = line[:-1]

            list_ = line.split(separator)

            dictionary_[int(list_[3])] = {
                "naziv": str(list_[0]),
                "broj_redova": int(list_[1]),
                "pozicije_sedista": [str(sjediste) for sjediste in list_[2]],
                "id": int(list_[3])
            }
    
    return dictionary_
