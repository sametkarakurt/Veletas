tahta = []
aticilar = []
for i in range(10):
    tahta.append(["-"] * 10)

# Tahta koordinatlarini eklemek için
koordinatlar = ["   A B C D E F G H I J"]
for i in range(10):
    koordinatlar.append(str(i+1).rjust(2) + " " + " ".join(tahta[i]))

# Tahtayi yazdirmak için
for row in koordinatlar:
    print(row)

# Oyuncu 1'in atici koordinatlarini iste ve kontrol et
aticilar = []

player = 'Black'

def isAdjacent(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1

# Oyuncu 1'in siyah taş koordinatlarını iste ve kontrol et
siyah_tas = ()
for i in range(3):
    while True:
        x, y = input("Oyuncu 1, {}. atıcının koordinatlarını girin (örnek: A1): ".format(i+1)).upper()
        x = ord(x) - 65  # Harf koordinatını indekse dönüştür
        y = int(y) - 1  # Sayı koordinatını indekse dönüştür

        if tahta[y][x] != "-" or (x, y) in aticilar or any(isAdjacent((x, y), atici) for atici in aticilar):
            print("Geçersiz koordinat. Başka bir koordinat girin.")
        else:
            aticilar.append((x, y))
            tahta[y][x] = "O"
            # Tahta koordinatlarını güncelle
            koordinatlar[y + 1] = str(y + 1).rjust(2) + " " + " ".join(tahta[y])
            break

# Oyuncu 1'in siyah taş koordinatlarını iste ve kontrol et

while True:
    x, y = input("Oyuncu 1, siyah taşın koordinatlarını girin (örnek: A1): ").upper()
    x = ord(x) - 65  # Harf koordinatını indekse dönüştür
    y = int(y) - 1  # Sayı koordinatını indekse dönüştür

    if tahta[y][x] != "-" or (x, y) in aticilar:
        print("Geçersiz koordinat. Başka bir koordinat girin.")
    else:
        siyah_tas = (x, y)
        tahta[y][x] = "S"
        # Tahta koordinatlarını güncelle
        koordinatlar[y + 1] = str(y + 1).rjust(2) + " " + " ".join(tahta[y])
        break

# Oyuncu 2'nin atıcı koordinatlarını iste ve kontrol et
for i in range(4):
    while True:
        x, y = input("Oyuncu 2, {}. atıcının koordinatlarını girin (örnek: A1): ".format(i + 1)).upper()
        x = ord(x) - 65  # Harf koordinatını indekse dönüştür
        y = int(y) - 1  # Sayı koordinatını indekse dönüştür

        if tahta[y][x] != "-" or (x, y) in aticilar or any(isAdjacent((x, y), atici) for atici in aticilar):
            print("Geçersiz koordinat. Başka bir koordinat girin.")
        else:
            aticilar.append((x, y))
            tahta[y][x] = "O"
            # Tahta koordinatlarını güncelle
            koordinatlar[y + 1] = str(y + 1).rjust(2) + " " + " ".join(tahta[y])
            break
# Oyuncu 2'nin beyaz taş koordinatlarini iste ve kontrol et
while True:
    x, y = input("Oyuncu 2, beyaz taşin koordinatlarini girin (örnek: A1): ").upper()
    x = ord(x) - 65 # Harf koordinatini indekse dönüştür
    y = int(y) - 1  # Sayi koordinatini indekse dönüştür
    if tahta[y][x] != "-" or (x, y) in aticilar:
        print("Geçersiz koordinat. Başka bir koordinat girin.")
    else:
        tahta[y][x] = "W"
        # Tahta koordinatlarini güncelle
        koordinatlar[y+1] = str(y+1).rjust(2) + " " + " ".join(tahta[y])
        break


# Tahtayi yazdirmak için
def tahta_yazdir():
    for row in koordinatlar:
        print(row)

tahta_yazdir()
    
def checkAndConvertO(tahta):
    rows = len(tahta)
    cols = len(tahta[0])

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if tahta[i][j] == "O":
                neighbors = [tahta[i-1][j-1], tahta[i-1][j], tahta[i-1][j+1],
                             tahta[i][j-1], tahta[i][j+1],
                             tahta[i+1][j-1], tahta[i+1][j], tahta[i+1][j+1]]

                if all(n == "S" or n == "W" for n in neighbors):
                    s_count = neighbors.count("S")
                    w_count = neighbors.count("W")
            
                    if s_count > w_count:
                        tahta[i][j] = "S"
                    elif w_count > s_count:
                        tahta[i][j] = "W"

    # Köşeleri kontrol etmek için ekstra işlem
    if tahta[0][0] == "O":
        corner_neighbors = [tahta[0][1], tahta[1][0], tahta[1][1]]
        if all(n == "W" or n == "S" for n in corner_neighbors):
            w_count = corner_neighbors.count("W")
            s_count = corner_neighbors.count("S")
            if s_count > w_count:
                tahta[0][0] = "S"
            elif w_count > s_count:
                tahta[0][0] = "W"

    if tahta[0][cols - 1] == "O":
        corner_neighbors = [tahta[0][cols - 2], tahta[1][cols - 2], tahta[1][cols - 1]]
        if all(n == "W" or n == "S" for n in corner_neighbors):
            w_count = corner_neighbors.count("W")
            s_count = corner_neighbors.count("S")
            if s_count > w_count:
                tahta[0][cols - 1] = "S"
            elif w_count > s_count:
                tahta[0][cols - 1] = "W"

    # Diğer benzer durumların kontrolünü ekle
    for i in range(1, rows - 1):
        if tahta[i][0] == "O":
            corner_neighbors = [tahta[i-1][0], tahta[i-1][1], tahta[i][1], tahta[i+1][0], tahta[i+1][1]]
            if all(n == "W" or n == "S" for n in corner_neighbors):
                w_count = corner_neighbors.count("W")
                s_count = corner_neighbors.count("S")
                if s_count > w_count:
                    tahta[i][0] = "S"
                elif w_count > s_count:
                    tahta[i][0] = "W"
        
        if tahta[i][cols - 1] == "O":
            corner_neighbors = [tahta[i-1][cols - 2], tahta[i-1][cols - 1], tahta[i][cols - 2], tahta[i+1][cols - 2], tahta[i+1][cols - 1]]
            if all(n == "W" or n == "S" for n in corner_neighbors):
                w_count = corner_neighbors.count("W")
                s_count = corner_neighbors.count("S")
                if s_count > w_count:
                    tahta[i][cols - 1] = "S"
                elif w_count > s_count:
                    tahta[i][cols - 1] = "W"

    # Tahta koordinatlarını güncelle
    for i in range(rows):
        koordinatlar[i+1] = str(i+1).rjust(2) + " " + " ".join(tahta[i])

    tahta_yazdir()

def checkCanGo(aticiX,aticiY,newCoordinateX,newCoordinateY):
    if(tahta[aticiY][aticiX] == "-" or tahta[aticiY][aticiX] == "S" or tahta[aticiY][aticiX] == "W"):
        return False
    elif(aticiX > newCoordinateX and aticiY < newCoordinateY):
        x = 0
        for i in range(aticiX):
            if(tahta[aticiY-x][aticiX+x] == "O"):
                print("Konumda giderken engelle karşılaşıldı")
                return False
            x += 1
    elif aticiX == newCoordinateX and aticiY > newCoordinateY:
        y_direction = -1
        y = aticiY + y_direction
        while y != newCoordinateY:
            if tahta[y][aticiX] == "O":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            y += y_direction
    elif aticiX < newCoordinateX and aticiY > newCoordinateY:
        x_direction = 1
        y_direction = -1
        x = aticiX + x_direction
        y = aticiY + y_direction
        while x != newCoordinateX and y != newCoordinateY:
            if tahta[y][x] == "O":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            x += x_direction
            y += y_direction
    # Sağa doğru hareket
    elif aticiY == newCoordinateY and aticiX < newCoordinateX:
        x_direction = 1
        x = aticiX + x_direction
        while x != newCoordinateX:
            if tahta[aticiY][x] == "O":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            x += x_direction

    # Sola doğru hareket
    elif aticiY == newCoordinateY and aticiX > newCoordinateX:
        x_direction = -1
        x = aticiX + x_direction
        while x != newCoordinateX:
            if tahta[aticiY][x] == "O":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            x += x_direction
    elif aticiX == newCoordinateX and aticiY < newCoordinateY:
        y = aticiY + 1
        while y <= newCoordinateY:
            if tahta[y][aticiX] == "O" or tahta[y][aticiX] == "W" or tahta[y][aticiX] == "S":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            y += 1
    # Sol aşağı çapraz hareket
    elif aticiX > newCoordinateX and aticiY < newCoordinateY:
        x_direction = -1
        y_direction = 1
        x = aticiX + x_direction
        y = aticiY + y_direction
        while x >= newCoordinateX and y <= newCoordinateY:
            if tahta[y][x] == "O" or tahta[y][x] == "W" or tahta[y][x] == "S":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            x += x_direction
            y += y_direction

    # Sağ aşağı çapraz hareket
    elif aticiX < newCoordinateX and aticiY < newCoordinateY:
        x_direction = 1
        y_direction = 1
        x = aticiX + x_direction
        y = aticiY + y_direction
        while x <= newCoordinateX and y <= newCoordinateY:
            if tahta[y][x] == "O" or tahta[y][x] == "W" or tahta[y][x] == "S":
                print("Konumda giderken engelle karşılaşıldı")
                return False
            x += x_direction
            y += y_direction
    return True

def checkGameOver(tahta):
    s_count = 0
    w_count = 0

    for row in tahta:
        for cell in row:
            if cell == "S":
                s_count += 1
            elif cell == "W":
                w_count += 1

    if s_count == 0:
        print("W oyuncusu kazandı!")
    elif w_count == 0:
        print("S oyuncusu kazandı!")
    else:
        return False

    return True


def oyun_baslat():
    player = 'Black'
    while True:
        # Oyuncudan hareket ettireceği atıcı taşın koordinatlarını iste
        x, y = input("Hareket ettirmek istediğiniz atıcı taşın koordinatlarını girin (örnek: A1): ").upper()
        x = ord(x) - 65 # Harf koordinatini indekse dönüştür
        y = int(y) - 1  # Sayi koordinatini indekse dönüştür
        
        # Seçilen koordinatların geçerli olup olmadığını kontrol et
        if (x, y) not in aticilar:
            print("Geçersiz koordinat. Atıcı taş seçin.")
            continue
        
        aticiX, aticiY = input("{} oyuncusu, atıcıyı hareket ettirmek istediğiniz  koordinatları girin (örnek: A1): ").upper()
        aticiX = ord(aticiX) - 65 # Harf koordinatini indekse dönüştür
        aticiY = int(aticiY) - 1  # Sayi koordinatini indekse dönüştür

        if(checkCanGo(x,y,aticiX, aticiY)):
            tahta[y][x] = "-"
            koordinatlar[y+1] = str(y+1).rjust(2) + " " + " ".join(tahta[y])
            aticilar.remove((x, y))
            tahta[aticiY][aticiX] = "O"
            koordinatlar[aticiY+1] = str(aticiY+1).rjust(2) + " " + " ".join(tahta[aticiY])
            aticilar.append((aticiX, aticiY))
            for row in koordinatlar:
                print(row)
            newAticiX, newAticiY = input("Yeni aticinin koordinatlarini girin (örnek: A1): ".format(i+1)).upper()
            newAticiX = ord(newAticiX) - 65 # Harf koordinatini indekse dönüştür
            newAticiY = int(newAticiY) - 1  # Sayi koordinatini indekse dönüştür
            if checkCanGo(aticiX,aticiY,newAticiX,newAticiY):
                if(player == 'Black'):
                    tahta[newAticiY][newAticiX] = "S"
                    player = 'White'
                else:
                    tahta[newAticiY][newAticiX] = "W"
                    player = 'Black'
                # Tahta koordinatlarini güncelle
                koordinatlar[newAticiY+1] = str(newAticiY+1).rjust(2) + " " + " ".join(tahta[newAticiY])
                checkAndConvertO(tahta)
                if(checkGameOver(tahta)):
                    return False             
            else:
                print("Geçersiz koordinat. Başka bir koordinat girin.")


            for row in koordinatlar:
                print(row)
        else:
            print("Geçersiz koordinat. Başka bir koordinat girin.")
            continue
            



oyun_baslat()
    
