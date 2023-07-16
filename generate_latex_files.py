import random
import os

def load_descriptions():
    """
    Load guest descriptions from a text file.
    """
    guest_descriptions = []
    try:
        with open('guest_descriptions.txt', 'r') as file:
            for line in file:
                guest_descriptions.append(line)
    except FileNotFoundError:
        print("Error: File 'guest_descriptions.txt' not found.")

    return guest_descriptions


def grid_per_guest():
    """
    Generates one grid per guest and saves them as LaTeX files.
    Args:
        grid_size (int): Optional input for the size of the grid (s x s). Default value is 5.
    Returns:
        str: The LaTeX code representing the grid.
    """
    qs = random.sample(guest_descriptions, 25)
    ret = ''
    i = 1
    for q in qs:
        if i % 5 == 0:
            ret += "{} \\\\\hline ".format(q)
        else:
            ret += "{} &".format(q)
        i += 1
    return ret

n_cards = int(input('How many BINGO cards would you like to generate?'))

guest_descriptions = load_descriptions()
assert len(guest_descriptions) >= 25, "Not enough guest-descriptions." \
                                     "add more desciriptions to file 'guest_descriptions'"

print(guest_descriptions)
print(len(guest_descriptions))
current_path = os.getcwd()

success = True
for g in range(n_cards):
    try:
        with open("card_{}.tex".format(g), 'w') as fd:
            fd.write(grid_per_guest())
    except IOError:
        success = False
        print("Error occurred while creating/saving file 'card_{}'.".format(g))

if success:
    print("{} files have been created and saved in '{}'".format(n_cards, current_path))


    for i in range(n_cards):

        with open("latex_tables.tex", 'w') as file:
            for i in range(n_cards):
                    file.write("\\vspace{3cm}\n")
                    file.write("\\begin{table}[htbp]\n")
                    file.write("\\centering\n")
                    file.write("\\begin{tabular}{|p{3cm}|p{3cm}|p{3cm}|p{3cm}|p{3cm}|}\n")
                    file.write("\\hline\n")
                    file.write("\\input{{card_{}.tex}}\n".format(i))
                    file.write("\\end{tabular}\n")
                    file.write("\\end{table}\n")
                    file.write("\n")