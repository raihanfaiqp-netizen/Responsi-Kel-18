class World:
    def __init__(self, size = 6):
        self.size = size
        
    def display(self, x, y): #ini method non-return type
        for row in range(self.size):
            for col in range(self.size):
                if row == y and col == x:
                    print("X", end=" ")
                else:
                    print(".", end=" ")
            print()
        print()

world = World()

def moveChar(x, y, move): #ini function return type
    if move == "w" and y > 0:
        y -= 1
    elif move == "s" and y < world.size - 1:
        y += 1
    elif move == "a" and x > 0:
        x -= 1
    elif move == "d" and x < world.size - 1:
        x += 1
    return x, y

def main(): #ini function non-return type
    x, y = 2, 2

    while True:
        world.display(x, y)
        print("PUNYA KELOMPOK 18")
        print("Gunakan W/A/S/D untuk bergerak, Q untuk keluar.")
        move = input("Masukkan perintah: ").lower()
        if move in ['w', 'a', 's', 'd']:
            x, y = moveChar(x, y, move)
        elif move == 'q':
            print("Program selesai")
            break
        else:
            print("Perintah tidak valid. Gunakan W/A/S/D untuk bergerak, Q untuk keluar.")

main()