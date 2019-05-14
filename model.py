import random 

# Definiramo konstante
STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'

ZMAGA = 'W'
PORAZ = 'X'

# Definiramo logicni model igre

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper() #string
        self.crke = crke #list
        return

    def napacne_crke(self):
        napacne = []
        for crka in self.crke:
            if crka not in self.geslo:
                napacne += [crka]
        return napacne

    def pravilne_crke(self):
        prave = []
        for crka in self.crke:
            if crka in self.geslo:
                prave += [crka]
        return prave

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
            return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK
            
    
    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.crke:
                niz += ' ' + crka
            else:
                niz += ' _'
        return niz.strip()

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA  
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA      

# Izluscimo vse slovenske besede
bazen_besed = []

with open("besede.txt", 'r', encoding='utf-8') as datoteka:
    for vrstica in datoteka.readlines():
        beseda = vrstica.strip()
        bazen_besed.append(beseda)

# Funkcije za generiranje iger

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo, [])