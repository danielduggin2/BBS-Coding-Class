# Session 6: A longer chain of conditions (golf terms)

score = 3
par = 5

difference = score - par

if difference <= -2:
    print("Eagle! Amazing!")
elif difference == -1:
    print("Birdie! Great shot!")
elif difference == 0:
    print("Par, nice and steady!")
elif difference == 1:
    print("Bogey, so close!")
else:
    print("A few extra strokes today, that's OK!")

# Your turn: try different score and par numbers.
# Can you make every message print at least once?
