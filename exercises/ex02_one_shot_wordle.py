"""One Shot Wordle!"""
__author__ = "730239053"

answer: str = "python"
guess: str = input(f"What is your {len(answer)}-letter guess? ")

w: str = "\U00002B1C"
g: str = "\U0001F7E9"
y: str = "\U0001F7E8"

chances: int = 0
idx: int = 0
result: str = ""

ifw: bool = False

while chances < 6:
    if len(answer) != len(guess):
        guess = input(f"That was not {len(answer)}-letters! Try again: ")
        chances = chances + 1
    else: 
        if guess == answer:
            while idx < len(answer):
                result = result + g
                idx = idx + 1
            print(result)
            print("Woo! You got it!")
            break
        else:
            while idx < len(answer):
                ifw = True
                yidx: int = 0
                if guess[idx] == answer[idx]:
                    ifw = False
                    result = result + g
                    idx = idx + 1 
                else: 
                    while yidx < len(answer):
                        if guess[idx] == answer[yidx]:
                            ifw = False
                            result = result + y
                            idx = idx + 1
                            yidx = len(answer) + 1
                        else:
                            yidx = yidx + 1
                if (ifw):
                    result = result + w
                    idx = idx + 1
            print(result)
            print("Not quite. Play again soon!") 
            break
if chances >= 6: 
    print("Not quite. Play again soon!")
