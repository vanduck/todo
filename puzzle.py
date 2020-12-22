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
           index_of_elem = board[i].index(word[0], index_of_elem)
        except ValueError:
            i += 1
            index_of_elem = 0
            continue
        else:
            if check_around(index_of_elem, i, board, word, 1):
                return True
            else: index_of_elem += 1
    return False

def check_around(x, y, board, word, word_index):
    if word_index < len(word):
        if (y + 1) < len(board) and board[y + 1][x] == word[word_index]:
                word_index += 1
                return check_around(x, y + 1, board, word, word_index)
        elif (y - 1) > 0 and board[y - 1][x] == word[word_index]:
                word_index += 1
                return check_around(x, y - 1, board, word, word_index)
        elif (x + 1) < len(board[y]) and board[y][x + 1] == word[word_index]:
                word_index += 1
                return check_around(x + 1, y, board, word, word_index)
        elif (x - 1) > 0 and board[y][x - 1] == word[word_index]:
                word_index += 1
                return check_around(x - 1, y, board, word, word_index)
        else: return False
    return True


#function(board_, word='TEA')

#assert function(board_, word='BEC') is False
#assert function(board_, word='SEAT')
#assert function(board_, word='TEA')
#assert function(board_, word='AGTAI') is False
assert function(board_, word='AJEQNTEAEGBC')
assert function(board_, word='KAFQEJ')
assert function(board_, word='EASTE') is False
assert function(board_, word='CAGTAI') is False
