import chess
from stockfish import Stockfish 
from gtts import gTTS  
from playsound import playsound  

stockfish = Stockfish(path ="/Users/Dev/Documents/Chess Engines/stockfish-windows-2022-x86-64-avx2")
board = chess.Board()
playing = True
stockfish.set_depth(20)
stockfish.set_skill_level(20)
playing = True
move = "e2e4"

def bestMove():
    global move
    board.push_san(move)
    stockfish.set_fen_position(board.fen())
    best_move = stockfish.get_best_move()
    return best_move

def audio():
    # It is a text value that we want to convert to audio  
    text_val = 'Best Move' + bestMove() 
        
        # Here are converting in English Language  
    language = 'en'  
        
        # Passing the text and language to the engine,  
        # here we have assign slow=False. Which denotes  
        # the module that the transformed audio should  
        # have a high speed  
    obj = gTTS(text=text_val, lang=language, slow=False)  
        
        #Here we are saving the transformed audio in a mp3 file named  
        # exam.mp3  
    obj.save("move.mp3")  
        
        # Play the exam.mp3 file  
    playsound("move.mp3")  

audio()









