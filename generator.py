
import random

def alege_cuvant_random(lungime_minima):
    ''' Alege random un cuvant din fisierul dat.
    Se parcurge linie cu linie fisierul si se adauga toate cuvintele care indeplinesc criteriul intr-o
    structura de date (lista). Se alege random din acea structura un cuvant.

    Args:
         lungime_minima(int):lungimea minima a cuvantului
    Returns:
        Intoarce cuvantul ales aleator cu lungimea mai mare decat lungime_minima.
    '''
    lista_de_ales = []
    lista_cuvinte = []
    lista_splituire = []
    file_name = r'C:\\Users\\alin9\\PycharmProjects\\PythonAlin\\Proiect\\cuvinte.txt'
    try:
        with open(file_name, mode='rt', encoding='utf-8') as fisier:
            continut = fisier.readlines()
            for i in continut:
                x=i.lower()
                a = x.rstrip()
                b = a.split(' ')
                lista_splituire.append(b)
            for m in lista_splituire:
                lista_cuvinte += m
            # print(lista_cuvinte) # doar daca vrem sa vedem toata lista cu cuvinte
            for i in lista_cuvinte:
                if len(i) >= lungime_minima:
                    lista_de_ales.append(i)
            #print(lista_de_ales)
            #print('Cuvantul care trebuie ghicit a fost selectat.')
            cuvant_de_ghicit=random.choice(lista_de_ales)
            print(f'Cuvant selectat. Are lungimea de {len(cuvant_de_ghicit)} caractere.')
            return cuvant_de_ghicit
    except IOError:
        print('Fisierul din care doresti sa aleaga cuvinte nu exista.')


if __name__=='__main__':
    print(f'Am ales cuvantul: {alege_cuvant_random(5)}')

