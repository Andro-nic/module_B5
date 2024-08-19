
def greeting():
    print("-----------------------")
    print(f"ПРИВЕТСТВУЕМ ВАС В ИГРЕ\n"
          f" КРЕСТИКИ НОЛИКИ")
    print("_______________________")
    print(f"игроки ходят по очереди,\n"
          f"вводя координаты клетки x y,\n"
          f"где: x - номер строки\n"
          f"     y - номер столбца")
    print("-----------------------")


greeting()

board = [[" "] * 3 for i in range(3)]  # Инициализация игрового поля


# создаем игровое поле
def play_board():
    print(f'    0   1   2')
    print(f'  _____________')
    for i, rows in enumerate(board):
        row = " | ".join(rows)
        print(f'{i} | {row} |\n  -------------')


play_board()


# ввод ходов пользователем
def ask_to_input():

    while True:
        turn = (input("Введите координаты(x y) для хода: ")).split()
        # проверка колличества введенных координат
        if len(turn) != 2:
            print("Введите две координаты!!!")
            continue
        x, y = turn
        # проверка цифрового ввода
        if not (x.isdigit()) or not (y.isdigit()):
            print("Введите числовые значения координат!!!")
            continue

        x, y = int(x), int(y)
        # проверяем диапазон координат
        if x < 0 or x > 2 or y < 0 or y > 2:
            print("Введенные координаты выходят за диапазон 0-2")
            continue

        # проверяем свободна ли данная клетка
        if board[x][y] != " ":
            print("Эта клетка занята другим игроком")
            continue

        return x, y


# ask_to_input()
# определение и проверка выиграшных комбинаций
def check_win():
    win_comb = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    for comb in win_comb:
        a = comb[0]
        b = comb[1]
        c = comb[2]

        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == "X":
            print("Победил первый игрок (X)")
            return True
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == "0":
            print("Победил второй игрок (0)")
            return True


check_win()

count = 0  # счетчик ходов

while True:
    count += 1
    if count % 2 > 0:
        print(F'Ходит первый игрок "X"')
        x, y = ask_to_input()
        board[x][y] = "X"

    else:
        print(F'Ходит второй игрок "0"')
        x, y = ask_to_input()
        board[x][y] = "0"
    play_board()
    if check_win():
        print("Игра окончена")
        break
    if count == 9:
        print("Ничья")
        break
