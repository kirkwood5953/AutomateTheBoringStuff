# Write your code here :-)
board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(boardCheck):
    bking, wking, wPieces, bPieces = 0,0,0,0
    #Checks Number of Pieces
    for color in boardCheck.values():
        if color[0] == 'w':
            wPieces += 1
        elif color[0] == 'b':
            bPieces += 1

    if bPieces >= 17 or wPieces >= 17:
        return False

    #Checks if valid location
    for location in boardCheck.keys():
        if int(location[0]) >8 or int(location[0]) <1:
            return False

    return True
print(isValidChessBoard(board))
