# Session 9: Functions (a reusable recipe)

def check_score(score, par):
    if score < par:
        print("Great job! Under par!")
    elif score == par:
        print("Nice, right on par!")
    else:
        print("Over par, try again next time!")

check_score(3, 4)
check_score(5, 4)

# Your turn: call check_score with different numbers.
# Can you make all three messages print?
