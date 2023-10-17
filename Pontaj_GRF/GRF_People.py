GRF_people = f'''
Adelina Vasile
Adrian Preoteasa
Adriana Dinu
Adriana Nedelcu
Adriana Pintilescu
Alexandra Pitulice
Alexandra Tataru
Alexandru Jac
Andreea Cristea
Andreea Motoc
Beatrice Mituleci
Bianca Boliacu
Bianca Florea
Bianca Pirvoiu
Bianca Placintaru
Bianca Ranete
Bianca Stefan
Bogdan Tomoiaga
Brindusa Bira
Catalin Olaru
Corina Coman
Corina Latosu
Cosmin Radulescu
Cristian Iosif
Cristina Iancu
Dan Dracea
Daniel Oprea
Daniel Secatureanu
Daniela Panfil
Dragos Botcau
Elena Stefan
Emil Calenciuc
Eva Bunici
Gabriela Catan
Geanina Iamandi
Georgiana Calin
Ilinca Teodorescu
Ioana Cucu
Ioana Petcu
Ioana Samoilescu
Ioana Traistaru
Irina Botezatu
Irina Ghidarcea
Irina Stanescu
Iulia Boieriu
Iulia Botar
Iulia Serafim
Iulia Stoicanea
Laura Nedelschi
Loredana Dicu
Loredana Ianus
Madalina Ghebaru
Madalina Radu
Mariana Oprea
Marinel Neagu
Mihaela Nastase
Mihaela Nicolae
Mihai Adler
Mirela Stoian
Monica Voinic
Nicoleta Iancu
Nina Cepraga
Olga Hosu
Paul Kasprovschi
Petronela Murarasu
Raluca Rotundu
Ramin Vahidi
Rebeca Maresescu
Roxana Diaconescu
Silvia Stoica
Simina Sirbu
Sorina Mihail
Tudor Salcudeanu
Victor Voicu
Viviana Dimcev
Anda Popescu

'''.strip()
GRF_list = []
list_people = GRF_people.splitlines()

for i in list_people:
    i = i.split(' ')
    i[0], i[1] = i[0].capitalize(), i[1].capitalize()

    GRF_list.append(f'{i[0]} {i[1]}')


GRF_dictionary = {}
for key, value in enumerate(GRF_list, start=1):
    GRF_dictionary[value] = key
