from other import Player

def main():
    name = ""
    while name == "":
        name = input("Player, please enter your name: ")

    player = Player(name)

    while True:
        print("Will You:")
        print("(1) Move Forward")
        print("(2) Move Backwar")
        print("(3) Move Left")
        print("(4) Move Right")
        print("(5) Attack")
        print("(6) Heal")
        choice = input("Choose: ")




if __name__ == "__main__":
    main()