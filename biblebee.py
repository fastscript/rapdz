def justlookatme(f):
    return print(f.read())


if __name__ == "__main__":
    file = open("bibl.txt")
    justlookatme(file)
    file.close()

#pip install Flask, Django and PYqt5 C:\Users\userauto\AppData\Local\Programs\Python\Python37