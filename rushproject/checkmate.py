def checkmate(board):
    rows = [row.strip()for row in board.splitlines()]
    h = len(rows)

    kr, kc = -1, -1
    for r in range(h):
        for c in range(len(rows[r])):
            if rows[r][c] == 'K':
                kr, kc = r, c
                break
        if kr != -1:
            break

    for dc in (-1, 1):
        r, c = kr - 1, kc + dc
        if 0 <= r < h and 0 <= c < len(rows[r]) and rows[r][c] == 'P':
            print("Success")
            return

    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
        r, c = kr + dr, kc + dc
        while 0 <= r < h and 0 <= c < len(rows[r]):
            if rows[r][c] != '.':
                if rows[r][c] in ('R', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    for dr, dc in ((1,1), (1,-1), (-1,1), (-1,-1)):
        r, c = kr + dr, kc + dc
        while 0 <= r < h and 0 <= c < len(rows[r]):
            if rows[r][c] != '.':
                if rows[r][c] in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    print("Fail")