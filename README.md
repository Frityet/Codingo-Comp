# CBO-coding-bingo-template
Welcome to the Codingo challenge! For a central hub for all the questions, check out this web page: https://cbo-challenge.netlify.app/

All question submissions should be uploaded here: https://forms.gle/7RaG58TL4oUvuBAM8

If you have any questions/comments/concerns feel free to ask them in this discord: https://discord.gg/94RJUHft

Before attempting any question please be sure to change the name of the file to include your team number! For example, if you are team #5 and you wish to submit question #1, please make sure that your submission file has the name `Q1_5.py`.

For certain questions there will be a `test.py` file within their respective folders. You can use this file to test your code and there will be output telling you if your code passes our checks or not. Before usage, find the following line of code in the `test.py` file:

```
from Q1_INSERTTEAMNUMBER import sudoku_solver
```

And please make sure to also change this line to reflect your new file name. So your new line of code should be:

```
from Q1_5 import sudoku_solver
```

Now you can run the `test.py` file and it should work!

## Scoring System

The number of points alloted for every completed question is stated in the README of the question. If you complete one full row, column or diagonal (see https://cbo-challenge.netlify.app/ for how the board is layed out), you will get an extra + 3 points added to your overall score.

Questions have an all or nothing scoring scheme, meaning you either get the question completely correct and get all points awarded, or you will get none of the points. No partial points will be awarded.

In the case that there is a tie in points for placements at the end of the competition, the team with the earlier overall submission times will be named as the winners. For example, if teams #1 and #2 get the following points and submission times:

|        | Q1 (5 points)     | Q2 (3 points)     | Q3 (3 points)      | Q4 (10 points) | Total Points |
|--------|-------------------|-------------------|--------------------|----------------|--------------|
| Team 1 | Submitted 9:00 AM | Not Submitted     | Submitted 10:00 AM | Not Submitted  | 8            |
| Team 2 | Submitted 9:30 AM | Submitted 9:45 AM | Not Submitted      | Not Submitted  | 8            |

Then Team 2 will be the winner because all their points were earned earlier than Team 1.
