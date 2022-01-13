##################################################################
#1.создать папку ./аlphabet/ или проверить, что папка существует
#2. в папку ./аlphabet/ поместить файлы вида a.txt, b.txt, ....z.txt в которых будет записана строка алфавита,
# но с заменой буквы из названия файла на прописную. например: для b.txt строка будет abcde...
#3. сделать щелчек Таноса- удалить случайным образом половину файлов в этой папке
import os
from string import ascii_lowercase as alphabet
from random import shuffle

def create_folder(folder_name="alphabet"):
    os.makedirs(folder_name, exist_ok=True)

def create_file(symbol, folder_name):
    filename = f"{symbol}.txt"
    with open(f"{folder_name}/{filename}", "w") as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))
#создаем файл

def create_alphabet_files(folder_name):
    for symbol in alphabet:
        create_file(symbol, folder_name)

def do_tanos_click(dir_name):
    #for filename in set(os.listdir(dir_name)): множество можно чтобы не было порядка, 2 вар:
    files = os.listdir(dir_name)
    shuffle(files)
    for filename in files[:len(files) // 2]: #берем половину срез#
        os.remove(os.path.join(dir_name, filename)) #путь к файлу#



dir_name = "alphabet"
create_folder(dir_name)
create_alphabet_files(dir_name)
do_tanos_click(dir_name)