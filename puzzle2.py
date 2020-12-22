board_ = [
    ['C', 'A', 'T', 'F', 'Z', 'K', 'L'],
    ['B', 'G', 'E', 'S', 'E', 'A', 'U'],
    ['I', 'T', 'A', 'E', 'P', 'F', 'M'],
    ['S', 'E', 'A', 'T', 'N', 'Q', 'H'],
    ['T', 'F', 'Z', 'E', 'L', 'E', 'J'],
    ['A', 'I', 'W', 'O', 'D', 'J', 'A']
]
# ['C', 'A', 'T', 'F', 'Z', 'K', 'L', 'B', 'G', 'E', 'S', 'E', 'A', 'U', 'I', 'T', 'A', 'E', 'P', 'F', 'M'


def function(board, word):
    index_of_elem = i = 0

    while i < len(board):
        try:
            index_of_elem = board[i].index(word[0], index_of_elem) # иищем первую букву в строке и получаем индекс
        except ValueError:
            i += 1
            index_of_elem = 0
            continue
        else:
            points = [[]] #тут хранятся координаты букв и номер буквы в заданом слове (номер буквы, point[x], point[x][y])
            points[0].append((0, index_of_elem, i))# добавляем координату первой буквы
            if check_around(0, 0, 1, points, board, word):
                return True
            else:
                index_of_elem += 1
    return False


def check_around(i, j, word_index, points, board, word):
    x = points[i][j][1]# x координата текущей буквы на board (координаты начинаются слева сверху(0.0))
    y = points[i][j][2]# y координата текущей буквы на board

    if word_index < len(word):
        old_len = len(points)
        old_len_i = len(points[i])

        if (y + 1) < len(board) and board[y + 1][x] == word[word_index]:
            if points[i][j][0] == word_index:
                points.append(points[i][:len(points[i]) - 1])
                points[-1].append((word_index, x, y + 1))
            else:
                points[i].append((word_index, x, y + 1))
                j += 1

        if (y - 1) >= 0 and board[y - 1][x] == word[word_index]:
            if points[i][j][0] == word_index:
                points.append(points[i][:len(points[i]) - 1])
                points[-1].append((word_index, x, y - 1))
            else:
                points[i].append((word_index, x, y - 1))
                j += 1

        if (x + 1) < len(board[y]) and board[y][x + 1] == word[word_index]:
            if points[i][j][0] == word_index:
                points.append(points[i][:len(points[i]) - 1])
                points[-1].append((word_index, x + 1, y))
            else:
                points[i].append((word_index, x + 1, y))
                j += 1

        if (x - 1) >= 0 and board[y][x - 1] == word[word_index]:
            if points[i][j][0] == word_index:
                points.append(points[i][:len(points[i]) - 1])
                points[-1].append((word_index, x - 1, y))
            else:
                points[i].append((word_index, x - 1, y))
                j += 1

        if len(points[i]) > old_len_i:
            word_index += 1
            j = len(points[i]) - 1
            return check_around(i, j, word_index, points, board, word)

        elif len(points) > old_len or i + 1 < len(points):
            j = len(points[i + 1]) - 1
            word_index = points[i + 1][j][0] + 1
            return check_around(i + 1, j, word_index, points, board, word)

        else:
            return False

    print(points[i])
    return True



assert function(board_, word='BEC') is False
assert function(board_, word='SEAT')
assert function(board_, word='TEA')
assert function(board_, word='AGTAI') is False
assert function(board_, word='AJEQNTEAEGBC')
assert function(board_, word='KAFQEJ')
assert function(board_, word='EASTE') is False
assert function(board_, word='CAGTAI') is False