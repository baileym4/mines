# Mines N-D

*Mines N-D* is an extension of the classic computer game Minesweeper, introducing a captivating twist by allowing gameplay on an N-dimensional board. Modeled after Minesweeper, *Mines N-D* retains the familiar rules where players navigate a grid, uncovering hidden squares without triggering mines.

## Gameplay Overview

The game unfolds on a grid, with each square containing either a number indicating adjacent mine count or a mine itself. The objective is to strategically use numerical hints, deducing mine locations, and ultimately clearing the entire board without triggering any mines.

### Two-Dimensional Gameplay

The main code, located in `lab.py`, initially focuses on the traditional two-dimensional Minesweeper experience. Key functions include:

- **Board Creation:** Generates a board based on user-defined parameters like rows, columns, and mines.
- **Dig Function:** Reveals the appropriate space based on the user's chosen square.
- **Rendering:** Produces a dictionary with essential game information and a depiction of the current game board.

### N-Dimensional Gameplay

Following the two-dimensional code, *Mines N-D* introduces gameplay on an N-dimensional board. Functions include:

- **Game Initialization:** Creates a new N-dimensional game with user-defined dimensions and mine count.
- **Dig_nd Function:** Utilizes recursion to update the game board after digging in the N-dimensional space.
- **Rendering:** Creates a representation of the N-dimensional game board.

## Testing

The `test.py` file, crafted by MIT 6.101 staff and complemented by additional doctests, ensures the reliability of each function.

## Server Integration

For interactive gameplay, *Mines N-D* includes server functionalities. Run `server_2d.py` and `server_nd.py` in your environment to set up a server where users can engage in the game.
