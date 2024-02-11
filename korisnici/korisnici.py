import common.konstante
from common import konstante

"""
Funkcija koja kreira novi rečnik koji predstavlja korisnika sa prosleđenim vrednostima. Kao rezultat vraća kolekciju
svih korisnika proširenu novim korisnikom. Može se ponašati kao dodavanje ili ažuriranje, u zavisnosti od vrednosti
parametra azuriraj:
- azuriraj == False: kreira se novi korisnik. staro_korisnicko_ime ne mora biti prosleđeno.
Vraća grešku ako korisničko ime već postoji.
- azuriraj == True: ažurira se postojeći korisnik. Staro korisnicko ime mora biti prosleđeno. 
Vraća grešku ako korisničko ime ne postoji.

Ova funkcija proverava i validnost podataka o korisniku, koji su tipa string.

CHECKPOINT 1: Vraća string sa greškom ako podaci nisu validni.
    Hint: Postoji string funkcija koja proverava da li je string broj bez bacanja grešaka. Probajte da je pronađete.
ODBRANA: Baca grešku sa porukom ako podaci nisu validni.
"""
def kreiraj_korisnika(svi_korisnici: dict, azuriraj: bool, uloga: str, staro_korisnicko_ime: str, 
                      korisnicko_ime: str, lozinka: str, ime: str, prezime: str, email: str = "",
                      pasos: str = "", drzavljanstvo: str = "",
                      telefon: str = "", pol: str = "") -> dict:
   
   # Prazan unos
    for key in [ime, prezime, korisnicko_ime, lozinka, email, pasos, drzavljanstvo, telefon, pol, uloga]:
        if key == None:
            raise Exception(f"Provera za nedostajucu vrednost: {key}")

    # Email
    at_pos = email.find('@')

    if at_pos == -1:
        raise Exception("Email provera bez @")
    if email[at_pos:].count('.') > 1:
        raise Exception("Email provera sa @ ali sa više poddomena")
    if email[at_pos:].count('.') < 1:
        raise Exception("Email provera sa @ ali bez poddomena")

    # Pasos
    if pasos != "0":
        if not pasos.isdigit():
            raise Exception("Pasoš nebrojevni string")
        if len(pasos) < 9:
            raise Exception("Pasoš manje od 9 cifara")
        if len(pasos) > 9:
            raise Exception("Pasoš više od 9 cifara")

    # Telefon
    if not telefon.isdigit():
        raise Exception("Broj telefona nebrojevni string")

    # Uloga
    if uloga not in [konstante.ULOGA_ADMIN, konstante.ULOGA_KORISNIK, konstante.ULOGA_PRODAVAC]:
        raise Exception("Uloga nije validna")

    # Azuriranje postojecih korisnika
    if azuriraj == True:
        if staro_korisnicko_ime not in svi_korisnici:
            raise Exception("Nepostojece korisnicko ime")
        if korisnicko_ime in svi_korisnici and korisnicko_ime != staro_korisnicko_ime:
            raise Exception("Korisničko ime je već zauzeto: očekuje se greška")
        if staro_korisnicko_ime in svi_korisnici:
            svi_korisnici[staro_korisnicko_ime] = {
            "ime": ime,
            "prezime": prezime,
            "korisnicko_ime": korisnicko_ime,
            "lozinka": lozinka,
            "email": email,
            "pasos": pasos,
            "drzavljanstvo": drzavljanstvo,
            "telefon": telefon,
            "pol": pol,
            "uloga": uloga,
        }

    # Unos novih korisnika
    if azuriraj == False and korisnicko_ime in svi_korisnici:
        raise Exception("Postojece korisnicko ime")
    else:
        svi_korisnici[korisnicko_ime] = {
            "ime": ime,
            "prezime": prezime,
            "korisnicko_ime": korisnicko_ime,
            "lozinka": lozinka,
            "email": email,
            "pasos": pasos,
            "drzavljanstvo": drzavljanstvo,
            "telefon": telefon,
            "pol": pol,
            "uloga": uloga,
        }

    return svi_korisnici


"""
Funkcija koja čuva podatke o svim korisnicima u fajl na zadatoj putanji sa zadatim separatorom.
"""
def sacuvaj_korisnike(putanja: str, separator: str, svi_korisnici: dict):
    
    with open(putanja, "w") as f:
        for korisnik in svi_korisnici:
            list = []

            for key in svi_korisnici[korisnik]:
                list.append(svi_korisnici[korisnik][key])

            line = separator.join(list)

            f.writelines(line + '\n')


"""
Funkcija koja učitava sve korisnika iz fajla na putanji sa zadatim separatorom. Kao rezultat vraća učitane korisnike.
"""
def ucitaj_korisnike_iz_fajla(putanja: str, separator: str) -> dict:
    import fajlovi
    dictionary = {}

    with open(putanja, "r") as f:
        for line in f.readlines():
            line = line[:-1]

            list = line.split(separator)
            
            dictionary[list[2]] = {
                "ime": list[0],
                "prezime": list[1],
                "korisnicko_ime": list[2],
                "lozinka": list[3],
                "email": list[4],
                "pasos": list[5],
                "drzavljanstvo": list[6],
                "telefon": list[7],
                "pol": list[8],
                "uloga": list[9],
            }
    
    return dictionary


"""
Funkcija koja vraća korisnika sa zadatim korisničkim imenom i šifrom.
CHECKPOINT 1: Vraća string sa greškom ako korisnik nije pronađen.
ODBRANA: Baca grešku sa porukom ako korisnik nije pronađen.
"""
def login(svi_korisnici, korisnicko_ime, lozinka) -> dict:
    
    try:
        if svi_korisnici[korisnicko_ime]["lozinka"] == lozinka:
            return svi_korisnici[korisnicko_ime]
        else:
            raise Exception("Login pogrešna lozinka")

    except:
        raise Exception("Login nepostojeći")
        

"""
Funkcija koja vrsi log out
*
"""
def logout(korisnicko_ime: str):
    
    print("Good bye!")
    
    return

