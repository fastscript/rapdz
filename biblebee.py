class Book():
    pass


def justlookatme():
    with open("bibl.txt", "r") as file:
        print(file.read())
    return None


def addbook():
    d = {}
    with open("bibl.txt", "a") as file:
        print("Введите автора книги: ")
        d["author"] = input()
        print("Введите название книги: ")
        d["name"] = input()
        print("Введите год издания книги: ")
        d["year"] = input()
        file.write(d["author"] + ", " + d["name"] + ", " + d["year"] + ";" + "\n")
    return


def clearlibrary():
    file = open("bibl.txt", "w")
    file.close()
    return


def delbookbynumber():
    print("Введите порядковый номер книги для удаления: ")
    n = int(input())
    with open("bibl.txt", "r") as file:
        lines = file.readlines()
        del lines[n - 1]
    with open("bibl.txt", "w") as file:
        for line in lines:
            file.write(line)
    return


if __name__ == "__main__":
    addbook()
    addbook()
    addbook()
    justlookatme()
    delbookbynumber()
    justlookatme()