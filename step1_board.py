rows = 10
cols = 10

board = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(".")
    
    board.append(row)
    
board[0][0], board[0][1], board[0][2] = "O", "O", "O"

for item in board:
    copy = item[:]
    for i in range(len(copy)):
        if copy[i] == "O":
            copy[i] = "."
    print(" ".join(copy))
    
    
while True:
    x = int(input("Введіть координату х, від 0 до 9: "))
    y = int(input("Введіть координату у, від 0 до 9: "))
    
    if (x > 9 or x < 0) or (y > 9 or y < 0):
        print("Невірні координати")
        continue
    
    elif board[x][y] == "X":
        print("По цій клітинці був виконаний постріл")
        continue
    
    elif board[x][y] == "O":
        print("Влучив!")
        board[x][y] = "X"
    
    elif board[x][y] == ".":
        print("Промах!")
        board[x][y] = "*"
                
    for item in board:
        copy = item[:]
        for i in range(len(copy)):
            if copy[i] == "O":
                copy[i] = "."
        print(" ".join(copy))
        
    result = input("Якщо хочеш зупинитись напиши q або якщо продовжити натисни Enter: ")
        
    if result.lower() == "q":
        break