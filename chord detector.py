# Define the chords
chords = {
    "C MAJOR": (-1, 3, 2, 0, 1, 0),
    "D MAJOR": (-1, -1, 0, 2, 3, 2),
    "E MAJOR": (0, 2, 2, 1, 0, 0),
    "F MAJOR": (1, 3, 3, 2, 1, 1),
    "G MAJOR": (3, 2, 0, 0, 0, 3),
    "A MAJOR": (-1, 0, 2, 2, 2, 0),
    "B MAJOR": (-1, 2, 4, 4, 4, 2),
    "C MINOR": (0, 0, 0, 5, 4, 3),
    "D MINOR": (-1, -1, 0, 2, 3, 1),
    "E MINOR": (0, 2, 2, 0, 0, 0),
    "F MINOR": (1, 3, 3, 1, 1, 1),
    "G MINOR": (3, 5, 5, 3, 3, 3),
    "A MINOR": (-1, 0, 2, 2, 1, 0),
    "B MINOR": (-1, 1, 4, 4, 3, 2),
    "D SUS": (2, 2, 0, 0, 3, 3),
    "E SUS": (0, 2, 2, 2, 0, 0),
    "G SUS": (3, 2, 0, 0, 1, 3),
    "A SUS": (0, 0, 2, 2, 3, 0),
    "B SUS": (2, 2, 4, 4, 5, 2),
}

def get_user_input():
    while True:
        print('Enter the fret numbers for the strings you played (use 0 for open strings and -1 for muted strings: ')
        print()
        user_chord = []
        
        for string in ["E", "A", "D", "G", "B", "e"]:
            try:
                note_input = int(input(f"Enter the fret number you played on the {string} string: "))
                print()
                user_chord.append(note_input)
            except ValueError:
                print("Invalid input. Please enter an integer value for the fret number.")
                return
            
        # Check if the entered chord matches any known chords
        for name, chord in chords.items():
            if tuple(user_chord) == chord:
                print(f'The chord you played is {name}.')
                return
        
        print("No matching chord found.")
        return

def main():
    get_user_input()
    while True:
        run_again = input("Do you wish to check another chord? (Y/N): ")
        if run_again.lower() == 'y':
            get_user_input()
        elif run_again.lower() == 'n':
            print('Goodbye')
            return
        else:
            print('Invalid input. Please enter Y or N.')


main()
