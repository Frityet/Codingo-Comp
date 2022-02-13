# CBO Coding Challenge Question 20 - 4 points

For this problem, program an interactive hangman game.

The parameters of this game are as follows:

- The function takes a secret word or phrase as input
- The command line will display the secret word or phrase with underscores
- As the user guesses the letters, any hits should replace underscores. Any misses should deduct a life.
- Instead of drawing out the hangman character, you may use a "life" counter.

For example, a board for "Hello world!" might look like:
`..... .....!`

After the user inputs "l" as a guess, it would look like:
`..ll. ...l.!
