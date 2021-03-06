


#  proxyCleave, Proxy Bioinformatics © 2018
#  Written By Andrew Lamothe

from tkinter import *

from tkinter import filedialog

enzymes = {'EcoRI': 'GAATTC', 'EcoRII': 'CCWGG', 'BamHI': 'GGATTC', 'HIND': 'AAGCTT', 'Nspl': 'RCATG'}

degenerate_nucleotides = {'R': ['G', 'A'], 'Y': ['T', 'C'], 'M': ['A', 'C'], 'K': ['G', 'T'], 'S': ['G', 'C'],
                          'W': ['A', 'T'], 'H': ['A', 'C', 'T'], 'B': ['G', 'T', 'C'], 'V': ['G', 'C', 'A'],
                          'D': ['G', 'A', 'T'], 'N': ['G', 'A', 'T', 'C']}

root = Tk()

root.title("proxyCleave V1.3, Proxy Bioinformatics © 2018")
root.configure(background='black')
root.geometry("1500x1000")

ProxyDongle = PhotoImage(file='PC.png')
ProxyDongle = ProxyDongle.subsample(2, 2)
Label(root, image=ProxyDongle, bg="black").grid(column=0, row=0)

#  ----------------------------------CLEAVE---------------------------------------------------------------

cleave = ' '
cleave_get = ' '
cleave_list = []


def set_cleave():

    global cleave, cleave_get, cleave_list, degenerate

    cleave_get = cleave_entry.get()
    cleave = cleave_get

    if cleave not in enzymes.keys():
        cleave = cleave.upper()

    print(cleave, type(cleave))

    for specificity in enzymes.keys():

        if specificity == cleave:

            cleave = use_of_name()

            print('cleave=result_of_name', cleave, type(cleave))

    for element in cleave:

        if element == '/':

            cleave = slash_handler()
            print('cleave = slash_handler()', cleave, type(cleave))

    for degenerate in degenerate_nucleotides.keys():

        if degenerate in cleave:

            cleave = deg_processed_list
            print('cleave = degenerate_handler()', cleave, type(cleave))


def slash_handler():

    global cleave

    for element in cleave:

        if element == '/':

            cleave = slash_finder()

            original_slash_list = cleave

            print('original_slash_list', original_slash_list, type(original_slash_list))

            for thing in cleave:

                print('thing', thing, type(thing))

                for bit in thing:

                    if bit in degenerate_nucleotides.keys():

                        cleave = thing

                        print('cleave = thing', cleave, type(cleave))

                        index_of_thing = original_slash_list.index(thing)

                        print('index of thing', index_of_thing, type(index_of_thing))

                        print(original_slash_list[index_of_thing], type(original_slash_list[index_of_thing]))

                        degenerate_slash_list = degenerates_input()

                        del original_slash_list[index_of_thing]

                        print('cleave', cleave, type(cleave))

                        original_slash_list = original_slash_list + degenerate_slash_list

                        print('cleave', cleave, type(cleave))

                return original_slash_list


#  ----------------------------------check for degenerates in cleave------------------------------------------------


def degenerates_input():

    for key in degenerate_nucleotides.keys():

        if key in str(cleave):  # searching for degenerates in original input

            degenerate_value_list = degenerate_nucleotides[key]

            degenerate_nucleotide_position = cleave.find(key)

            if len(degenerate_value_list) >= 1:

                first_degenerate = degenerate_value_list[0]

                first_degenerate_iterant = cleave.replace(cleave[degenerate_nucleotide_position], first_degenerate)

                if len(degenerate_value_list) >= 2:

                    second_degenerate = degenerate_value_list[1]

                    second_degenerate_iterant = cleave.replace(cleave[degenerate_nucleotide_position],
                                                               second_degenerate)

                    degenerate_list = [first_degenerate_iterant, second_degenerate_iterant]

                    print(second_degenerate, second_degenerate_iterant, degenerate_list)

                    if len(degenerate_value_list) >= 3:

                        third_degenerate = degenerate_value_list[2]

                        third_degenerate_iterant = cleave.replace(cleave[degenerate_nucleotide_position],
                                                                  third_degenerate)

                        degenerate_list = [first_degenerate_iterant, second_degenerate_iterant,
                                           third_degenerate_iterant]

                        print(third_degenerate, third_degenerate_iterant, degenerate_list)

                        if len(degenerate_value_list) >= 4:

                            fourth_degenerate = degenerate_value_list[3]

                            fourth_degenerate_iterant = cleave.replace(cleave[degenerate_nucleotide_position],
                                                                       fourth_degenerate)

                            degenerate_list = [first_degenerate_iterant, second_degenerate_iterant,
                                               third_degenerate_iterant, fourth_degenerate_iterant]

                        return degenerate_list

        break


deg_processed_list = []


def degenerate_handler():

    global cleave, degenerate

    global deg_processed_list

    for degenerate in degenerate_nucleotides.keys():

        if degenerate in cleave:

            print('if degenerate in cleave', cleave, type(cleave))

            deg_processed_cleave_1 = degenerates_input()

            print('deg_processed_cleave_1', deg_processed_cleave_1, type(deg_processed_cleave_1))

            deg_processed_list = deg_processed_list + deg_processed_cleave_1

            print('deg_processed_list', deg_processed_list, type(deg_processed_list))

            for component in deg_processed_list:

                if degenerate in component:

                    cleave = component

                    deg_processed_cleave_2 = degenerates_input()

                    deg_processed_list = deg_processed_list + deg_processed_cleave_2

                    print(deg_processed_list)

                continue

            continue


cleave_entry = StringVar()
cleave1 = Entry(root, textvariable=cleave_entry, width=20).grid(column=1, row=0)

cleave_button = Button(root, width=20, text="recognition specificity", command=set_cleave)
cleave_button.grid(column=1, row=1)

temp_cleave_reassigned = str(cleave)

temp_cleave_reassigned_maketrans = str.maketrans("<>'[],123456789=?.;_", 20 * " ")

cleave = temp_cleave_reassigned.translate(temp_cleave_reassigned_maketrans)

cleave = cleave.strip()

cleave = str(cleave)

#  ----------------------------------ORF---------------------------------------------------------------

ORF_entry = IntVar()

ORF_get = 0
ORF = 0


def set_orf():

    global ORF_get, ORF
    ORF_get = ORF_entry.get()
    ORF = ORF_get


ORF1 = Entry(root, textvariable=ORF_entry, width=20).grid(column=2, row=0)

ORF_button = Button(root, width=20, text="enter ORF", command=set_orf)
ORF_button.grid(column=2, row=1)

#  ------------------------------------------find slash in cleave----------------------------------------------------
#  It may be more robust to .split('/') and then append to either side of the split than to make separate
#  cases for each possible position within a string


def slash_finder():

    for component in cleave:

        if component == '/':

            slash_index = cleave.find(component)

            print('index of slash', slash_index, 'type of', type(slash_index))

            slash_split = cleave.split('/')

            print('slash_split', type(slash_split), slash_split)

            cleave_len = len(cleave)

            print('cleave_len', cleave_len, type(cleave_len))

            first_slash_split = slash_split[0]

            second_slash_split = slash_split[1]

            print(slash_split[0], slash_split[1])

            print('first_slash_split', first_slash_split, type(first_slash_split),
                  'second_slash_split', second_slash_split, type(second_slash_split))

            end_of_first = len(first_slash_split)-1

            print(end_of_first)

            first_slash_split_last_removed = first_slash_split.replace(first_slash_split[end_of_first], '', 1)

            print('second_slash_split', second_slash_split, type(second_slash_split), second_slash_split[0])

            second_slash_split_first_removed = second_slash_split.replace(second_slash_split[0], '', 1)

            final_iterant_1 = first_slash_split_last_removed + second_slash_split

            print('final_iterant_1', final_iterant_1, type(final_iterant_1))

            final_iterant_2 = first_slash_split + second_slash_split_first_removed

            print('final_iterant_2', final_iterant_2, type(final_iterant_2))

            split_list = [final_iterant_1, final_iterant_2]

            print('split_list', split_list, type(split_list))

            return split_list

#  ----------------------------------------check for use of brand spec------------------------------------------------


def use_of_name():

    print('OK')

    if cleave in enzymes.keys():

        cleave_reassigned = enzymes[cleave]

        cleave_reassigned = cleave_reassigned.strip()

        print('the if statement for checking user input against '
              'established brand dictionary keys has returned positive', cleave_reassigned, type(cleave_reassigned))

        return cleave_reassigned


result_of_name = use_of_name()

#  -------------------------------------------main--------------------------------------------------------------------


def main():

    root.fileName = filedialog.askopenfilename(filetypes=(("fasta files", ".txt"), ("All files", "*.*")))

    file = root.fileName

    with open(file, 'r') as sequence:

        search = sequence.read()

        search = search.upper()

        temp_search_reassigned = str(search)

        temp_search_reassigned_maketrans = str.maketrans("<>'[],123456789=?.;_", 20 * " ")

        search = temp_search_reassigned.translate(temp_search_reassigned_maketrans)

        search = str(search.strip(' '))

        search = search.replace(' ', '')

        sequence.close()

        parse_orf = [search[i:i + ORF] for i in range(0, len(search), ORF)]

        character_count = 0

        white_space = 0

        line_count = 0

        total_lines = 0

        for line in parse_orf:

            total_lines = total_lines + 1

            for character in line:

                if character != ' ':

                    character_count = character_count + 1

        print('total chars:', character_count, type(character_count))
        print('total white space:', white_space, type(white_space), 'total lines in file:', total_lines)

    if type(cleave) is list:

        print('list cleave', cleave, type(cleave))

        for i in cleave:

            palindrome = i[::-1]

            print('cleave:', i, type(i), 'palindrome: ', palindrome, type(palindrome))

            print('i', i, type(i))

            for nucleotidesOnly in parse_orf:

                recognition = int(nucleotidesOnly.find(i))

                palindrome_recognition = int(nucleotidesOnly.find(i))

                if recognition > 0:

                    graphic_line_recognition = 'Yes'

                else:

                    graphic_line_recognition = 'No'

                if palindrome_recognition > 0:

                    graphic_line__palindrome_recognition = 'Yes'

                else:

                    graphic_line__palindrome_recognition = 'No'

                line_count = line_count + 1

                output_textbox.insert(INSERT, "line:{} nucleotides:{} recognition:{} at:{} palindrome:{} at:{}"
                                      .format(line_count, nucleotidesOnly, graphic_line_recognition, recognition,
                                              graphic_line__palindrome_recognition, palindrome_recognition,))

    elif type(cleave) is str:

        palindrome = cleave[::-1]

        print('cleave:', cleave, type(cleave), 'palindrome: ', palindrome, type(palindrome))

        for nucleotidesOnly in parse_orf:

            recognition = int(nucleotidesOnly.find(cleave))

            palindrome_recognition = int(nucleotidesOnly.find(palindrome))

            if recognition > 0:

                graphic_line_recognition = 'Yes'

            else:

                graphic_line_recognition = 'No'

            if palindrome_recognition > 0:

                graphic_line__palindrome_recognition = 'Yes'

            else:

                graphic_line__palindrome_recognition = 'No'

            line_count = line_count + 1

            output_textbox.insert(INSERT, "line:{} nucleotides:{} recognition:{} at:{} palindrome:{} at:{}"
                                          .format(line_count, nucleotidesOnly, graphic_line_recognition, recognition,
                                                  graphic_line__palindrome_recognition, palindrome_recognition,
                                                  ))


#  ----------------------------------button for main-------------------------------------------------------------------

file_button = Button(root, width=20, text="file upload")
file_button.grid(column=3, row=0)
file_button.config(command=main)

#  -----------------------Text Box && SCROLL BAR-----------------------------------------------------------------

output_textbox = Text(root, state='normal', width=200, height=50, wrap=WORD)
output_textbox.grid(columnspan=6, rowspan=1)

scroll = Scrollbar(root, command=output_textbox.yview)
output_textbox.configure(yscrollcommand=scroll.set)
scroll.grid(column=4, row=1)

# --------------------------plasmid vectors-----------------------------------------------------------------------------

#  -------------------------Highlight recognition-----------------------------------------------------------------------

output_textbox.tag_config(cleave, background='red')
#  -------------------------Text Box Delete-----------------------------------------------------------------------------


def obliterate():

    output_textbox.delete(1.0, END)
    print('delete!')


delete_text_button = Button(root, width=20, text="Delete Output", command=obliterate)
delete_text_button.grid(column=3, row=1)

#  ------------------------------main loop----------------------------------------------------------------------------
root.mainloop()
