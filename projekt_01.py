TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']
SPACE = '=' * 80
count_cap = []
count_cap_all = []
count_low = []
count_numb = []
text_bez_znaku = []

name = input('Enter your username: ')
password = input('Enter your password: ')
registered = {"bob": "123",
              "ann": "pass123",
              "mike": "password123",
              "liz": "pass123"}
if registered.get(name) == password:
    print(f'NICE TO SEE YOU AGAIN {name}.YOU CAN USE TEXT ANALYZER.'
          .center(len(SPACE)), SPACE, sep="\n")
else:
    print('SORRY YOU ARE NOT IN THE REGISTERED PEOPLE. GOODBYE!'
          .center(len(SPACE)), SPACE, sep="\n")
    quit()
print(f'WE HAVE {len(TEXTS)} TEXTS TO BE ANALYZED.'
      .center(len(SPACE)), SPACE, sep="\n")
choice = input(f'ENTER A NUMBER BTW. 1 AND {len(TEXTS)} TO SELECT:')
print(SPACE)
if choice.isdigit() and int(choice) < len(TEXTS) + 1:
    text = TEXTS[int(choice) - 1]
    bez_mezer = text.split()
    for slova in bez_mezer:
        bez_znaku = slova.strip(".,;:")
        text_bez_znaku.append(bez_znaku)  # celkový počet slov v textu
        bez_cisel = slova.strip('0123456789.,;: ')
        if slova[0].isupper():
            slova = slova.strip(',')
            count_cap.append(slova)  # celkový slov, které začínají velk
        elif slova.isupper():
            slova = slova.strip(',')
            count_cap_all.append(slova)  # celkový počet slov co jsou jenom velká
        elif slova.islower():
            count_low.append(slova)   # celkový počet slov co jsou jenom malá
        elif slova.isalpha() is False:
            count_numb.append(slova)  # všechna čísla co se nachází v textu
else:
    if not choice.isdigit():
        print('SORRY YOU WROTE SOMETHING DIFFERENT THAN A NUMBER. GOODBYE.'
              .center(len(SPACE)), SPACE, sep="\n")
        quit()
    else:
        print('SORRY THIS TEXT IS NOT IN OUR OFFER. GOODBYE.'
              .center(len(SPACE)), SPACE, sep="\n")
        quit()
for k in range(0, len(count_numb)):
    count_numb[k] = int(count_numb[k])
celkove = sum(count_numb)  # součet čísel v textu
cetnost = {}
for slov in text_bez_znaku:
    if len(slov) in cetnost.keys():
        cetnost[len(slov)] = cetnost[len(slov)] + 1
    else:
        cetnost[len(slov)] = 1  # kolikrát tam slova mám
print(f'''THERE ARE {len(text_bez_znaku)} WORDS IN THE SELECTED TEXT.
THERE ARE {len(count_cap)} TITLECASE WORDS.
THERE ARE {len(count_cap_all)} UPPERCASE WORDS.
THERE ARE {len(count_low)} LOWERCASE WORDS.
THERE ARE {len(count_numb)} NUMERIC STRING.
THE SUM OF ALL THE NUMBERS {celkove} 
{SPACE}''')
print(f'''LEN|  OCCURENCES  |NR.
{SPACE}''')
for key in sorted(cetnost.keys()):
    print(key, '|', '*' * cetnost[key], '|', cetnost[key])
