# Sessions 11 and 12: Mini Golf Tracker (TEACHER ANSWER KEY)

player_name = "Jordan"

scores = [3, 4, 5, 2, 4, 3, 5, 4, 3]
par = 36

def check_score(score, hole_par):
    if score < hole_par:
        print("Great job! Under par!")
    elif score == hole_par:
        print("Nice, right on par!")
    else:
        print("Over par, try again next time!")

# Each hole has a par of 4 in this version
for score in scores:
    check_score(score, 4)

total_strokes = sum(scores)
difference = total_strokes - par

print(player_name, "finished with", total_strokes, "strokes.")
print("Compared to par:", difference)

# Polish: a fun final message
if difference < 0:
    print("Great round!")

# Stretch goal (uncomment in Colab): let a friend type in their own scores
# friend_score = int(input("Type a score for hole 1: "))
# check_score(friend_score, 4)
