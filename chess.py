def display_board(board):
    line = ""
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            line += str(board[i][j])
        line += "\n"
    print(line)

def add_queen(tx,ty,board):
    
    if(board[ty][tx] == 2):
        print("can't do it")
        return False, board
    else:
        for i in range(0, 4):
            board[i][tx] = 2
        for i in range(0, 4):
            board[ty][i] = 2
      
        
        px = 0
        py = 0
        if(tx < ty):
            px = 0
            py = ty - tx
        if(tx > ty):
            py = 0
            px = tx - ty
        
        for i in range(0,4):
            if(px + i < len(board) and py + i < len(board)):
                board[py + i][px + i] = 2
            
        board[ty][tx] = 1
        
        display_board(board)
        return True, board

def problem():
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    tx = 0
    ty = 0
    result = True
    failCount = 0
    
    display_board(board)
    
    while(True):
        result,board = add_queen(tx, ty, board)
        if(result and tx != len(board) - 1):
            tx += 1
            ty = 0
        elif(result and tx == len(board) - 1):
            break
        else:
            if(ty < len(board) - 1):
                ty += 1
            else:
                
                
                
                board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                tx = 0
                failCount += 1
                ty = failCount


    
    
    
    
    
    
problem()