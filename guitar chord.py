class Chord:
    chord_shapes = {
        'CMAJ': [-1, 3, 2, 0, 1, 0], 'DMAJ': [-1, -1, 0, 2, 3, 2], 'EMAJ': [0, 2, 2, 1, 0, 0],
        'FMAJ': [1, 3, 3, 2, 1, 1], 'GMAJ': [3, 2, 0, 0, 0, 3], 'AMAJ': [-1, 0, 2, 2, 2, 0], 'BMAJ': [-1, 2, 4, 4, 4, 2],
        'CMIN': [0, 0, 0, 5, 4, 3], 'DMIN': [-1, -1, 0, 2, 3, 1], 'EMIN': [0, 2, 2, 0, 0, 0], 'FMIN': [1, 3, 3, 1, 1, 1],
        'GMIN': [3, 5, 5, 3, 3, 3], 'AMIN': [-1, 0, 2, 2, 1, 0], 'BMIN': [-1, 1, 4, 4, 3, 2],
        'DSUS': [2, 2, 0, 0, 3, 3], 'ESUS': [0, 2, 2, 2, 0, 0], 'GSUS': [3, 2, 0, 0, 1, 3], 
        'ASUS': [0, 0, 2, 2, 3, 0], 'BSUS': [2, 2, 4, 4, 5, 2]
    }

    def __init__(self, root: str, chord_type: str):
        self.root = root.upper()
        self.chord_type = chord_type
        self.name = self.get_chord_name()
        self.shape = self.chord_shapes.get(self.name)

    def get_chord_name(self):
        if self.chord_type == 'M':
            return f"{self.root}MAJ"
        elif self.chord_type == 'm':
            return f"{self.root}MIN"
        elif self.chord_type == 'S':
            return f"{self.root}SUS"
        return None

    def display(self):
        if self.shape is None:
            print(f"Chord {self.name} not found.\n")
            return

        print(f"\nChord: {self.name}")
        print("   E   A   D   G   B   e")
        print("--------------------------------------------")
        for value in self.shape:
            print("{:>4}".format("x" if value < 0 else value), end="")
        print("\n")


class ChordDisplay:
    def get_chord_type(self):
        while True:
            chord_type = input("Enter M for Major, m for Minor, and S for Suspended: ").strip().upper()
            if chord_type in ['M', 'm', 'S']:
                return chord_type
            print("Invalid input. Please enter M, m, or S.")

    def get_chord_root(self):
        while True:
            root = input("Enter a chord (Ex. C, D, etc.): ").strip().upper()
            if root in ['C', 'D', 'E', 'F', 'G', 'A', 'B']:
                return root
            print("Invalid chord. Please enter a valid note (e.g., C, D, E, etc.).")

    def run(self):
        while True:
            chord_type = self.get_chord_type()
            chord_root = self.get_chord_root()
            chord = Chord(chord_root, chord_type)
            chord.display()
            
            choice = input("Do you want to enter another chord? (Y/N): ").strip().lower()
            if choice != 'y':
                print("Goodbye!")
                break


if __name__ == "__main__":
    ChordDisplay().run()