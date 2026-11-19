# Cheating Chess Board

A Python prototype that reads out a Stockfish move suggestion.

* Tracks a chess position with python-chess.
* Finds a suggested move with Stockfish at depth 20.
* Turns the suggestion into speech with gTTS.
* Saves the audio as an MP3 and plays it.
* Includes a separate speech playback test.

The current script uses a fixed opening move and a local Stockfish path. It does not read moves from a physical board.
