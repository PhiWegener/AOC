mapStruktur = []
with open("input/input.txt", 'r') as file:
        zeilen = file.read().splitlines()
        print(zeilen)
    
    # mapStruktur = [list(zeile) for zeile in zeilen]