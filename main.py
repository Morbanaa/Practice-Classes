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

        match(choice):
            case "1":
                player.move_forward()
            case "2":
                player.move_backward()
            case "3":
                player.move_left()
            case "4":
                player.move_right()
            case "5":
                player.attacking()
            case "6":
                player.heal()
            case _:
                continue


if __name__ == "__main__":
    main()