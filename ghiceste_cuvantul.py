import time

import utilitare
import generator

def joaca():
    '''Este prezentatorul aplicatiei.
    Trebuie sa ne asiguram ca avem in primul rand numarul de incercari si lungimea minima
    obtinute de la concurent. Dupa acest pas, afisam starea curenta (cuvant, numar incercari)
    si cerem cuvinte. Aceasta bucla se opreste atunci cand intreg cuvantul a fost ghicit
    sau cand a fost atins numarul maxim de incercari.
    Returns:
        True/False echivalent cu faptul ca acel concurent mai vrea sau nu sa joace o tura.
    '''
    solicitare=input('Vrei sa incepem jocul? Da/Nu - ')
    raspuns=solicitare.capitalize()
    print(('-')*40)
    while raspuns == 'Da':
        start_time=time.time()
        lungime_minima_cuvant=utilitare.obtine_lungime()
        cuvant = generator.alege_cuvant_random(lungime_minima_cuvant)
        print(('-')*40)
        numar_incercari = utilitare.obtine_numar_incercari()
        print(('-') * 40)
        utilitare.afiseaza_cuvant(cuvant, numar_incercari)
        print(('-') * 40)
        end_time=time.time()
        durata_joc=round(end_time - start_time)
        print('Jocul tau a durat: {0} de secunde.'.format(durata_joc,'.1f'))
        alt_raspuns=input('Mai vrei sa joci?  Da/Nu - ')
        raspuns=alt_raspuns.capitalize()
        print(('-')*40)
    else:
        print('Ok. Jocul s-a sfarsit.')

if __name__=='__main__':
    joaca()





