def find_positions(board): #ใช้เพื่อหาตำแหน่งของหมากแต่ละตัว
    P, B, R, Q, K = [], [], [], [], []
    for i, row in enumerate(board):
        for j, piece in enumerate(row): #ใช้เพื่อหาตำแหน่งของแต่ละค่า ใส่มาเพื่อหาindex
            if piece == 'P':
                P.append([i, j])
            elif piece == 'B':
                B.append([i, j])
            elif piece == 'R':
                R.append([i, j])
            elif piece == 'Q':
                Q.append([i, j])
            elif piece == 'K':
                K = [i, j]
    return K, P, B, R, Q #ใช้เพื่อใส่ค่าคืน

def is_in_bounds(board, r, c):# ตรวจสอบพิกัด(ตำแหน่ง)ว่าอยู่ในตำแหน่งไหม *ที่จะรุกฯคิง
    return 0 <= r < len(board) and 0 <= c < len(board)

def checkmate(board_string):
    board = board_string.split() #คาดการณ์หาตำแหน่งของหมากแต่ละตัว
    king, pawns, bishops, rooks, queens = find_positions(board)

    # Pawn check
    for r, c in pawns:
        for dr, dc in [(-1, -1), (-1, 1)]:
            if [r + dr, c + dc] == king:
                print("Success")
                return

    # Bishop & Queen (diagonal)
    for r, c in bishops + queens:
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            i, j = r + dr, c + dc
            while is_in_bounds(board, i, j): #ใช้เพื่อตรวจสอบเงื่อนไข
                if [i, j] == king:
                    print("Success")
                    return
                if board[i][j] != '.':
                    break
                i += dr
                j += dc

    # Rook & Queen (straight lines)
    for r, c in rooks + queens:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = r + dr, c + dc
            while is_in_bounds(board, i, j):
                if [i, j] == king:
                    print("Success")
                    return
                if board[i][j] != '.':
                    break
                i += dr
                j += dc

    print("Fail")
