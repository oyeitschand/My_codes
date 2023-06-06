def ecryptmytext(character, plaintext, shift):
    n = len(plaintext)
    cipher = []
    for i in range(0, n):
        for j in character:
            if character[j] == plaintext[i]:
                numbergreater = j + shift
                if numbergreater > 26:
                    numbergreater = numbergreater - 26
                    cipher.append(character[numbergreater])
                    continue
                cipher.append(character[numbergreater])

    return cipher


def printcipher(cipher):
    print("Ciper: ", end="")
    for i in cipher:
        print(i, end="")
    print()


def main():
    text = input("Enter your text: ")
    shift = int(input("Which Shift you wanna use: "))
    characters = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z"
    }

    a = ecryptmytext(characters, text, shift)
    printcipher(a)


if __name__ == "__main__":

    main()
