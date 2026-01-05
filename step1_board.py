rows = 10
cols = 10

board = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(".")
    
    board.append(row)
    
for item in board:
    print(" ".join(item))
    
while True:
    x = int(input("Введіть координату х, від 0 до 9: "))
    y = int(input("Введіть координату у, від 0 до 9: "))
    
    if (x > 9 or x < 0) or (y > 9 or y < 0):
        print("Невірні координати")
        continue
    
    if board[x][y] == "X":
        print("По цій клітинці був виконаний постріл")
        continue
    
    board[x][y] = "X"
        
    for item in board:
        print(" ".join(item))
        
    result = input("Якщо хочеш зупинитись напиши q або якщо продовжити натисни Enter: ")
        
    if result.lower() == "q":
        break