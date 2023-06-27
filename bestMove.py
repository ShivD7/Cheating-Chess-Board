import chess
import random
from stockfish import Stockfish 
from gtts import gTTS  
from playsound import playsound  

stockfish = Stockfish(path ="/Users/Dev/Documents/Chess Engines/stockfish-windows-2022-x86-64-avx2")
board = chess.Board()
playing = True
stockfish.set_depth(20)
stockfish.set_skill_level(20)
playing = True
moves_white = ["e2e4", "a2a4", "f2f4"]
moves_black = ["e7e5", "f7f5", "b7b5"]
count = 0

while playing:
    if count % 2 == 0:
        move = random.choice(moves_white)
    else:
        move = random.choice(moves_black)
    board.push_san(move)
    stockfish.set_fen_position(board.fen())
    best_move = stockfish.get_best_move()

        
        # It is a text value that we want to convert to audio  
    text_val = 'Best Move' + str(best_move)  
        
        # Here are converting in English Language  
    language = 'en'  
        
        # Passing the text and language to the engine,  
        # here we have assign slow=False. Which denotes  
        # the module that the transformed audio should  
        # have a high speed  
    obj = gTTS(text=text_val, lang=language, slow=False)  
        
        #Here we are saving the transformed audio in a mp3 file named  
        # exam.mp3  
    obj.save("exam.mp3")  
        
        # Play the exam.mp3 file  
    playsound("exam.mp3")  
    count += 1









