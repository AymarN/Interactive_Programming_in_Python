A reminder about the Honor Code
For previous mini-projects, we have had instances of students submitting solutions that have been copied from the web. Remember,
if you can find code on the web for one of the mini-projects, we can also find that code. Submitting copied code violates the Honor
Code for this class as well as Coursera's Terms of Service. Please write your own code and refrain from copying. If, during peer 
evaluation, you suspect a submitted mini-project includes copied code, please evaluate as usual and email the assignment details to
iipphonorcode@online.rice.edu. We will investigate and handle as appropriate.


Mini-project description - “Guess the number” game

One of the simplest two-player games is “Guess the number”. The first player thinks of a secret number in some known range while the second player attempts to guess the number. After each guess, the first player answers either “Higher”, “Lower” or “Correct!” depending on whether the secret number is higher, lower or equal to the guess. In this project, you will build a simple interactive program in Python where the computer will take the role of the first player while you play as the second player.

When discussing ranges in this mini-project, we will follow the standard Python convention of including the low end of the range and excluding the high end of the range. Mathematically, we will express ranges via the notation [low, high). The square bracket of the left of the range indicates that the corresponding bound should be included. The left parenthesis on the right of the range indicates that corresponding bound should be excluded. For example, the range [0, 3)consists of numbers starting at 0 up to, but not including 3. In other words 0, 1, and 2.

You will interact with your program using an input field and several buttons. For this project, we will ignore the canvas and print the computer's responses in the console. Building an initial version of your project that prints information in the console is a development strategy that you should use in later projects as well. Focusing on getting the logic of the program correct before trying to make it display the information in some “nice” way on the canvas usually saves lots of time since debugging logic errors in graphical output can be tricky.

Mini-project development process

We have provided a basic template for this mini-project here. Our suggested development strategy for the basic version of “Guess the number” is below. Remember to run your program after each step to ensure that you implemented that step correctly.

1.	Add code to the program template that creates a frame with an input field whose handler has the name input_guess. You will use this input field to enter guesses.

2.	Add code to the event handler input_guess(guess) that takes the input string guess, converts it to an integer, and prints out a message of the form "Guess was 37" (or whatever the guess actually was). Hint: We have shown you how to convert strings to numbers in the lectures.

3.	Add code to the function new_game that initializes a global variable secret_number to be a random number in the range [0, 100). (Note that this range should not include 100 as a possible secret number.) Remember to include a global statement. Hint: Look at the functions in the random module to figure out how to easily select such a random number. Observe that the call to new_game() at the bottom of the template ensures that secret_number is always initialized when the program starts running.

4.	Add code to input_guess that compares the entered number to secret_number and prints out an appropriate message such as "Higher", "Lower", or "Correct".

5.	Test your code by playing multiple games of “Guess the number” with a fixed range. At this point, you will need to re-run your program between each game (using the CodeSkulptor “Run” button). You are also welcome to use this testing template http://www.codeskulptor.org/#examples-gtn_testing_template.py. The bottom of the template contains a sequence of calls to 𝚒𝚗𝚙𝚞𝚝_𝚐𝚞𝚎𝚜𝚜() for three games of "Guess the number". Uncomment each sequence of calls and check whether the output in the console matches that provided in the comments below. Note that your output doesn't have to be identical, just of a similar form.
From this minimal working version of “Guess the number”, the rest of this project consists of adding extra functionality to your project. There are two improvements that you will need to make to get full credit:

6.	Using function(s) in the simplegui module, add buttons to restart the game so that you don't need to repeatedly click “Run” in CodeSkulptor to play multiple games. You should add two buttons with the labels "Range is [0,100)" and "Range is [0,1000)" that allow the player to choose different ranges for the secret number. Using either of these buttons should restart the game and print out an appropriate message. They should work at any time during the game. In our implementation, the event handler for each button sets the desired range for the secret number (as a global variable) and then call new_game to reset the secret number in the desired range. As you play “Guess the number”, you might notice that a good strategy is to maintain an interval that consists of the highest guess that is “Lower” than the secret number and the lowest guess that is “Higher” than the secret number. A good choice for the next guess is the number that is the average of these two numbers. The answer for this new guess then allows you to figure a new interval that contains the secret number and that is half as large. For example, if the secret number is in the range [0, 100), it is a good idea to guess 50. If the answer is "Higher", the secret number must be in the range [51, 100). It is then a good idea to guess 75 and so on. This technique of successively narrowing the range corresponds to a well-known computer algorithm known as binary search.

7.	Your final addition to “Guess the number” will be to restrict the player to a limited number of guesses. After each guess, your program should include in its output the number of remaining guesses. Once the player has used up those guesses, they lose, the game prints out an appropriate message, and a new game immediately starts. Since the strategy above for playing “Guess the number” approximately halves the range of possible secret numbers after each guess, any secret number in the range [low, high) can always be found in at most n guesses where n is the smallest integer such that 2 ** n >= high - low + 12**n>=high-low+1. For the range [0, 100), n is seven. For the range [0, 1000), n is ten. In our implementation, the function new_game() set the number of allowed guess to seven when the range is [0, 100) or to ten when the range is [0, 1000). For more of a challenge, you may compute n from low and high using the functions math.logmath.log and math.ceilmath.ceil in the mathmath module.

When your program starts, the game should immediately begin in the range [0, 100). When the game ends (because the player either wins or runs out of guesses), a new game with the same range as the last one should immediately begin by calling new_game(). Whenever the player clicks one of the range buttons, the current game should stop and a new game with the selected range should begin.