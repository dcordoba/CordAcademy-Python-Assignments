# Summary
In this assignment, you will be simulating a chess piece moving across a
chessboard. Luckily, our chess game will only have pawns, so movement will be
much simpler.

Given a starting position on the board and a list of moves, we want to know
where the chess piece will end up. If the moves ever move our pawn off of the
board, we will want to return None.

# The Chess Board
A normal chessboard is an 8x8 grid. Unfortunately, we won't know the dimensions
of our board until our method is called.

Positions on the board are denoted by their x and y coordinates, starting at the
top left of the board. See below for an example of a 3x4 grid.

```
            x
      0     1     2
  0 (0,0) (1,0) (2,0)
y 1 (0,1) (1,1) (2,1)
  2 (0,2) (1,2) (2,2)
  3 (0,3) (1,3) (2,3)
```

# Movement
You will define a method named get_end_position that takes a starting position,
the dimensions of the grid, and a list of moves, and returns the ending position
of the pawn once it has made all of the moves listed. If the pawn moves off of
the board, you should return None.

Moves will be either 'UP', 'DOWN', 'LEFT', or 'RIGHT.'

# The Code

Helper classes for representing a position and size are provided for you, as
well as some simple test cases to check your solution.

The method definition for get_end_position is provided for you as well. In order
for the tests to pass, this should return the ending position once the given
moves are made. This is the only method definition provided for you, but you can
(and probably should) define other helper methods.

# Example Run
```
moves = ['RIGHT', 'DOWN', 'DOWN']
start_position = Position(x=1, y=1)
board_size = Size(width=3, height=4)
end_position = get_end_position(start_position, board_size, moves)
# After those moves, the pawn should be at the bottom right corner of the board.
assert end_position.x == 2
assert end_position.y == 3
```

To see the movement of the piece, look at the board below.
```
            x
      0     1     2
  0 (0,0) (1,0) (2,0)
y 1 (0,1) (1,1) (2,1)
  2 (0,2) (1,2) (2,2)
  3 (0,3) (1,3) (2,3)
```

The piece will start at point (1, 1). After moving 'RIGHT', the piece would move
to (2,1). 'DOWN' would move the piece to (2,2), and another 'DOWN' would move
the piece to it's ending position of (2,3).
