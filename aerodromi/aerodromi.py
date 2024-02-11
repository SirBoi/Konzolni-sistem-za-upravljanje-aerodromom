

"""
Funkcija kreira rečnik za novi aerodrom i dodaje ga u rečnik svih aerodroma.
Kao rezultat vraća rečnik svih aerodroma sa novim aerodromom.
"""
def kreiranje_aerodroma(
    svi_aerodromi: dict,
    skracenica: str ="",
    pun_naziv: str ="",
    grad: str ="",
    drzava: str =""
) -> dict:
    
    # Prazan unos
    for key in [skracenica, pun_naziv, grad, drzava]:
        if key == None or key == "":
            raise Exception(f"Provera za nedostajucu vrednost: {key}")

    # Provjera validnosti unesenih vrijednosti
    if not (type(skracenica) == str and len(skracenica) == 3):
        raise Exception("Vrednosti od aerodroma nisu dobre")

    for key in [pun_naziv, grad, drzava]:
        if not (type(key) == str and len(key) == 7):
            raise Exception("Vrednosti od aerodroma nisu dobre")

    # Sve provjere su prosle, aerodrom se kreira
    svi_aerodromi[skracenica] = {
        "skracenica": skracenica,
        "pun_naziv": pun_naziv,
        "grad": grad,
        "drzava": drzava
    }

    return svi_aerodromi


"""
Funkcija koja čuva aerodrome u fajl.
"""
def sacuvaj_aerodrome(putanja: str, separator: str, svi_aerodromi: dict):
    
    with open(putanja, "w") as f:
        for aerodrom in svi_aerodromi:
            list_ = []

            for key in svi_aerodromi[aerodrom]:
                list_.append(str(svi_aerodromi[aerodrom][key]))

            line = separator.join(list_)

            f.writelines(line + '\n')


"""
Funkcija koja učitava aerodrome iz fajla.
"""
def ucitaj_aerodrom(putanja: str, separator: str) -> dict:
    
    dictionary_ = {}

    with open(putanja, "r") as f:
        for line in f.readlines():
            line = line[:-1]

            list_ = line.split(separator)

            dictionary_[str(list_[0])] = {
                "skracenica": str(list_[0]),
                "pun_naziv": str(list_[1]),
                "grad": str(list_[2]),
                "drzava": str(list_[3])
            }
    
    return dictionary_