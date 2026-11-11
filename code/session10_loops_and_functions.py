# Session 10: Loops + functions together

def check_score(score, par):
    if score < par:
        print("Great job! Under par!")
    elif score == par:
        print("Nice, right on par!")
    else:
        print("Over par, try again next time!")

scores = [3, 5, 4, 6, 2]
par = 4

for score in scores:
    check_score(score, par)

# Your turn: build your own version from scratch with
# your own list of 5 scores, your own par, a loop, and check_score.
