
import generator

def obtine_lungime():
    '''Folosind metoda input obtinem lungimea minima a cuvantului.
    Aceasta metoda interogheaza  concurentul cu privire la lungimea minima redusa. Se verifica
    daca lungimea introdusa este intr-un anumit range.
    args:
        -
    :returns
        Valoarea numerica ce reprezinta lungimea minima.
    '''

    lungime= input('Care sa fie lungimea minima a cuvintelor pentru ghicit:')
    try:
        lungime_minima = int(lungime)
        if isinstance(lungime_minima, int):
            while lungime_minima<=2 or lungime_minima>=10:
                lungime_minima = int(input('Introduceti alta lungime minima:'))

            #print('Lungimea cuvantului ce urmeaza sa fie ghicit este in intervalul corect.')
            return lungime_minima
    except:
        print('Nu ai introdus un numar.')


def obtine_numar_incercari():
    '''Folosind metoda input obtinem numarul maxim de incercari pe care si-l doreste concurentul.
    Aceasta metoda interogheaza concurentul cu privire la numarul maxim de incercari. Se verifica
    daca numarul introdus este intr-un anumit range.
    Returns:
        Valoare numerica ce reprezinta numarul maxim de incercari.
    '''
    numar=input('Introdu numarul de incercari dorit:')
    try:
        numar_incercari = int(numar)
        while numar_incercari <= 1 or numar_incercari > 10:
            numar_incercari=int(input('Introdu un alt numar de incercari:'))
        return numar_incercari
    except:
        print('Nu ai introdus un numar.')



def afiseaza_cuvant(cuvant, numar_incercari):
    '''Metoda ce afiseaza cuvantul.
    Se doreste ca literele care nu au fost ghicite sa se afiseze ascuns folosind "*".
    Restul literelor se vor afisa clar.
    Args:
        cuvant (str) : cuvant ales random
        numar_incercari : numar ales
    Returns:
        Cuvantul (str) cu forma lui finala.
        Lista partiala si finala cu elementele cuvantului la fiecare etapa din joc.
    '''

    lista_cuvant = []
    #numar_incercari=obtine_numar_incercari()
    lista_cuvant=list(cuvant)
    # print(lista_cuvant)
    lista_ascunsa=[]
    for index in range(len(cuvant)):
        lista_ascunsa.append('*')
    print(f'Cuvant ascuns: {lista_ascunsa}')
    print(('-')*40)
    lista_incercari=[]
    lista_retineri=list()
    cuvant_ascuns=''
    while numar_incercari > 0:
        alege_litera = input('Alege o litera pentru cuvant:')
        while (alege_litera in lista_retineri) or (alege_litera in lista_incercari):
             print(f'Litera {alege_litera} este deja folosita.')
             alege_litera=input('Introdu o alta litera:')
             print(('-')*40)

        while (alege_litera not in lista_cuvant):
            numar_incercari -=1
            print(('-') * 40)
            lista_incercari.append(alege_litera)
            print(('-')*40)
            print(f'Litera {alege_litera} nu este in cuvantul de ghicit.')
            print(f'Litere deja utilizate care nu au fost bune: {lista_incercari}')
            print(f'Cuvantul de ghicit: {lista_ascunsa}')
            print(f'Ti-au ramas {numar_incercari} incercari.')
            print(('-')*40)
            break

        else:
            count=lista_cuvant.count(alege_litera)
            while count > 0:
                 index_cuvant=lista_cuvant.index(alege_litera)
                 lista_ascunsa.pop(index_cuvant)
                 lista_ascunsa.insert(index_cuvant,alege_litera)
                 lista_cuvant.pop(index_cuvant)
                 lista_cuvant.insert(index_cuvant, '*')
                 count -=1
            print(f'Litera {alege_litera} este in cuvant.')
            print(f'Cuvant de ghicit: {lista_ascunsa}')
            cuvant_ascuns = ''
            for parcurgere in lista_ascunsa:
                cuvant_ascuns += parcurgere
            #print(f'Cuvantul este: {cuvant_ascuns}')
            lista_retineri.append(alege_litera)
            #print(f'Litere ce apartin cuvantului: {lista_retineri}')
            print(('-')*40)
            if lista_ascunsa == list(cuvant) :
                print(f'Cuvantul este: {cuvant_ascuns}')
                print('Felicitari!! Ai ghicit cuvantul.')
                break
    if numar_incercari == 0:
        print('Ai pierdut. Ai ramas fara incercari.')
        print(f'Cuvantul era: {cuvant}')
        print(('-')*40)



if __name__=='__main__':
    #print(obtine_lungime())
    #print(obtine_numar_incercari())
    cuvant = generator.alege_cuvant_random(5)
    print(cuvant)
    afiseaza_cuvant(cuvant, 5)