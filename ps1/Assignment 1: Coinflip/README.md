# Summary

In this assignment, you will be simulating a coin flipping game. We want to know
how many coin flips it will take to see 'HEADS' a given amount of times in a
row.

After each flip, you should print the result. Once we see the desired number of
'HEADS' in a row, print the total number of coin flips it took to get there and
exit the program.

# Flipping a Coin

The simulation of a coin flip is done using the python random module. A
flip_coin method is provided for you that returns the string 'HEADS' 50% of the
time and the string 'TAILS' 50% of the time. You will use this method to
simulate a run of your coin flipping game.

# Example Run

```
> python flip.py 3
> Flipping coin until we get 3 HEADS
> TAILS
> HEADS
> TAILS
> HEADS
> HEADS
> TAILS
> HEADS
> HEADS
> HEADS
> It took 9 flips to get 3 HEADS in a row!
```

Of course, since a coin flip is random, your output will vary from this each
time.

