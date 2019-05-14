# Funkcije, ki geenrirajo izpis za igralca
import model

def izpis_igre(igra):
    tekst = (
        '========================================\n\n'
        '    {trenutno_stanje}\n\n'
        'Nesupesni poskusi: {poskusi} \n\n'
        '========================================\n\n'
    ).format(trenutno_stanje=igra.pravilni_del_gesla(), poskusi=igra.nepravilni_ugibi())

    return tekst

def izpis_zmage(igra):
    return 'Uspesno ste uganili geslo {}!'.format(igra.geslo)

def izpis_poraza(igra):
    return 'Porabili ste prevec poskusov. Pravilno geslo je {}'.format(igra.geslo)

def zahtevaj_vnos():
    vnos = input('Poskusi uganit crko: ')
    return vnos

def preveri_vnos(vnos):
    '''Funkcija vrne True, ce je vnos primeren, sicer igralca opozori in vrne False'''
    if len(vnos) != 1:
        print('Neveljaven vnos! Vnesi zgolj eno crko!')
        return False
    else:
        return True

# Izvajanje vmesnika

def zazeni_vmesnik():
    igra = model.nova_igra()

    while True:
        # izpisemo stanje
        print(izpis_igre(igra))
        #igralec ugiba
        poskus = zahtevaj_vnos() # se ni napisano
        if not preveri_vnos(poskus):
            continue # preskoci preostanek zanke

        rezultat = igra.ugibaj(poskus)
        #preverimo, ce je igre konec
        if igra.poraz(): # if rezultat == model.PORAZ():
            print(izpis_poraza(igra))
            return
        elif igra.zmaga():
            print(izpis_zmage(igra))
            return
    return

# Zares pozeni igro


# Zares zazeni vmesnik
zazeni_vmesnik()
