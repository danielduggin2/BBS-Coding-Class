# BBS-Coding-Class
# Intro to Python — 6-Week Lesson Plan (Golf Theme)
**For 4th grade (starting), Becca's classes — Days 1 & 4, 1:00-3:25pm, 50-minute periods**

**Tool to use:** replit.com or Google Colab (colab.research.google.com) — both run Python right in the browser, no install needed. (Trinket.io has shut down, so it's not an option.)

**Theme:** Everything builds toward one running project — a "Mini Golf Tracker" — using golf scores, holes, and par. Kids don't need to know golf well; just tell them: "golf is a game where lower numbers are better, and you're trying to hit a ball into a hole in as few tries (strokes) as possible."

**Session structure (roughly, for every 50-minute class):**
- Warm-up / recap (5-8 min) — re-explain last session's concept before moving on
- Talking points (5-10 min) — new concept
- Guided coding together (15-20 min) — type it as a class, everyone follows along
- Independent practice (10-15 min) — they try it on their own
- Wrap-up / share (5 min) — a couple kids show what they got

Expect a lot of repeat questions in the first few weeks — that's normal and the warm-up blocks are built in for exactly that.

---

# WEEK 1

## SESSION 1: What is a programming language? Getting set up + print()

### Warm-up (5 min)
Introduce the golf theme. Ask: "Has anyone played golf or mini golf?" Explain: lower score is better, you're trying to get the ball in the hole in as few tries (strokes) as possible. Tell them: by the end of this unit, everyone will build their own computer program that acts like a mini golf scorecard.

### Talking points: what is a programming language? (10 min)
- People talk to each other using languages like English or Spanish. A **programming language** is how people talk to computers — it's a language the computer understands and can act on.
- Computers are very literal. They only do exactly what you type, nothing more, nothing less, and they do it exactly in order, one step at a time.
- There are lots of programming languages (mention a couple kids may have heard of, like Scratch, JavaScript, or Python) — today we're using **Python**, one of the most widely used languages in the real world.
- What can you actually build with a programming language? Websites, video games, phone apps, robots, even the recommendation system that picks videos for you. Basically: anything on a screen or a device that reacts to you was built by someone writing code.
- Our version today is small but real: we're going to build the first piece of a "golf scorecard" program, and we'll keep adding to it every week until it can track a full round of golf — with scores, math, and messages that react to how you did.

### Getting set up (10 min)
Walk everyone through logging into replit.com or Colab and creating a new Python file/notebook. Expect this to eat some time in Session 1 only — budget for it.

### Guided coding (15 min)
Type this together and click Run:
```python
print("Welcome to the golf course!")
```
Ask: What happened? (The computer said back exactly what we told it to say — this is our first real program.)

Then try a few more, letting kids call out what to print:
```python
print("Let's play 9 holes today!")
print("Good luck!")
```
Mini "fix the bug" game: write `print("Hello")` with a missing quote or parenthesis on the board and ask kids to spot what's wrong. This introduces the idea that computers need things typed exactly right — that's part of what a programming language is.

### Independent practice (5 min)
Have each student write 3 print statements of their own choosing and run them.

### Wrap-up (5 min)
A couple kids read one thing they printed out loud. Remind them: this print statement is the first building block of the golf scorecard program we'll be building together all semester.

---

## SESSION 2: Variables

### Warm-up / recap (8 min)
Quick verbal check: "What does print() do?" Have a student come up and type a print statement from memory. Re-run one of last session's examples together as a reminder of the tool.

### Talking points (8 min)
- A **variable** is like a labeled box that holds information for later.
- Analogy: imagine a golf ball bag with a name tag on it. The tag is the variable name; what's inside is the value.

### Guided coding (18 min)
```python
player_name = "Jordan"
favorite_club = "Putter"
hole_number = 1

print(player_name)
print(favorite_club)
print(hole_number)
```
Point out:
- `=` doesn't mean "equals" like in math class — it means "put this value in the box."
- Words need quotes (`"Jordan"`), numbers don't (`1`).

Have kids predict what will print before running it — good habit to build early.

### Independent practice (10 min)
Have each student create 3 variables about themselves (name, favorite color, grade number) and print all three. This is their "player profile" — they'll reuse this idea later.

### Wrap-up (6 min)
A few students share their player profile output.

---

# WEEK 2

## SESSION 3: Math with variables

### Warm-up / recap (8 min)
Quick oral quiz: "What symbol do we use to put a value in a variable box?" Have a student write a variable on the board and have the class predict the print() output.

### Talking points (8 min)
- Python can do math just like a calculator: `+` add, `-` subtract, `*` multiply, `/` divide.
- In golf, **par** is the number of strokes you're "supposed to" take on a hole.

### Guided coding (18 min)
```python
hole_1 = 4
hole_2 = 5
hole_3 = 3

total_strokes = hole_1 + hole_2 + hole_3
print("Total strokes:", total_strokes)
```
Let kids change the numbers and re-run to see the total change.

### Independent practice (11 min)
Give students 3 new hole scores of their choosing and have them add up the total, printing the result.

### Wrap-up (5 min)
Share totals — see who has the lowest (best) score, tying back to the golf theme.

---

## SESSION 4: Comparing to par

### Warm-up / recap (8 min)
Recap addition example from last session — re-run it together, ask what `total_strokes` means.

### Talking points (5 min)
- If you take more strokes than par, you did worse; fewer, you did better.

### Guided coding (15 min)
```python
par = 12
total_strokes = 12

difference = total_strokes - par
print("Strokes vs par:", difference)
```
Explain: if `difference` is 0, you matched par. Negative means you beat par (great!). Positive means you went over.

### Independent practice (15 min)
Give students 3 new hole scores. Have them:
1. Add up the total strokes.
2. Compare it to a par of 12.
3. Print both results as a full sentence, e.g. `print("My total score was", total_strokes, "strokes, which is", difference, "compared to par.")`

### Wrap-up (7 min)
Share results, talk about what negative vs. positive differences mean.

---

# WEEK 3

## SESSION 5: Conditionals — if / elif / else

### Warm-up / recap (8 min)
Recap `difference = total_strokes - par` — ask a couple kids what a negative vs positive number meant last time.

### Talking points (8 min)
- A **conditional** lets the computer make a decision and do different things depending on what's true.
- Golf analogy: depending on your score, you'd react differently — celebrate, shrug, or try again.

### Guided coding (18 min)
```python
score = 3
par = 4

if score < par:
    print("Great job! Under par!")
elif score == par:
    print("Nice, right on par!")
else:
    print("Over par, try again next time!")
```
Walk through it: the computer checks each condition in order and runs the first one that's true.

### Independent practice (11 min)
Have students change `score` and `par` to different values and predict which message will print before running it.

### Wrap-up (5 min)
Ask a few kids to share a combination that triggered each of the three messages.

---

## SESSION 6: Extending conditionals + review game

### Warm-up / recap (5 min)
Quick recap: what do `if`, `elif`, and `else` each do?

### Talking points (5 min)
- We can chain more conditions together for more detail — like golf terms: eagle, birdie, par, bogey.

### Guided coding (20 min)
```python
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
```

### Independent practice (12 min)
Students try different `score` and `par` combinations to hit each message.

### Wrap-up review game (8 min)
Call out a score/par pair verbally and have kids shout the term (eagle/birdie/par/bogey) before checking it in code — fun, fast-paced recap.

---

# WEEK 4

## SESSION 7: Lists

### Warm-up / recap (8 min)
Quick recap of variables and conditionals — ask a student to explain what `if` does in their own words.

### Talking points (8 min)
- A **list** is a way to store many values in one variable — like a full scorecard instead of one hole at a time.

### Guided coding (18 min)
```python
scores = [4, 5, 3, 6, 4]

print(scores)
print(scores[0])
print(scores[1])
```
Explain: the numbers in brackets tell Python which position to look at, and counting starts at 0 (this trips kids up — spend extra time here).

### Independent practice (11 min)
Have students create their own list of 5 scores and print a couple of individual holes by their position.

### Wrap-up (5 min)
Ask: "What's `scores[0]` in your list?" for a couple of students.

---

## SESSION 8: Loops

### Warm-up / recap (8 min)
Recap lists and indexing — re-run last session's example together.

### Talking points (8 min)
- A **loop** lets the computer repeat instructions without typing them over and over.
- Golf analogy: instead of writing "print the score" 9 times for 9 holes, we tell the computer "repeat this for every hole."

### Guided coding (18 min)
```python
scores = [4, 5, 3, 6, 4]

for score in scores:
    print("Hole score:", score)
```
Let kids change the numbers in the list and re-run — the loop automatically handles however many scores are there.

### Independent practice (11 min)
Have students loop through their own list of scores and print each one.

### Wrap-up (5 min)
Ask: "What would happen if you added a 6th score to your list? Do you need to change your loop?" (No — that's the point.)

---

# WEEK 5

## SESSION 9: Functions

### Warm-up / recap (8 min)
Recap loops — have a student explain what `for score in scores:` does.

### Talking points (8 min)
- A **function** is a reusable set of instructions you can use again and again, like a recipe.
- You give it information, it does something with it, and can react differently depending on what you gave it.

### Guided coding (18 min)
```python
def check_score(score, par):
    if score < par:
        print("Great job! Under par!")
    elif score == par:
        print("Nice, right on par!")
    else:
        print("Over par, try again next time!")

check_score(3, 4)
check_score(5, 4)
```
Walk through it line by line: `def` starts a new function, `check_score` is its name, `score` and `par` are boxes it expects to be filled in when it's used.

### Independent practice (11 min)
Have students call `check_score` with a few different number combinations of their own choosing.

### Wrap-up (5 min)
Ask: "Why is a function better than writing the if/elif/else every single time?"

---

## SESSION 10: Combining loops and functions

### Warm-up / recap (8 min)
Recap functions — re-run last session's `check_score` example.

### Talking points (5 min)
- Now we combine everything: loop through a list of scores, and call the function on each one.

### Guided coding (15 min)
```python
scores = [3, 5, 4, 6, 2]
par = 4

for score in scores:
    check_score(score, par)
```
This is the big "aha" moment — the loop repeats, and each time it calls the function to check that hole's score.

### Independent practice (17 min)
Have students build their own version from scratch: their own list of 5 scores, their own `par`, a loop, and calling `check_score` inside it. This is effectively a rehearsal for the final project.

### Wrap-up (5 min)
Ask a few kids to share their full output.

---

# WEEK 6 — FINAL PROJECT: Mini Golf Tracker

## SESSION 11: Project work day

### Warm-up (5 min)
Introduce the final project: a Mini Golf Tracker that uses everything learned — variables, math, a list, a loop, and a function.

### Project requirements (5 min)
Explain what it needs to include:
1. A list of 9 hole scores
2. A `par` variable
3. A loop that goes through every score and uses `check_score` to react to it
4. A total strokes calculation
5. A difference from par calculation
6. A final printed summary sentence

Give them a starter template with blanks to fill in, for example:
```python
scores = [___, ___, ___, ___, ___, ___, ___, ___, ___]
par = ___

def check_score(score, par):
    # fill in the if/elif/else here

total_strokes = ___
difference = ___

for score in scores:
    check_score(score, par)

print("Total strokes:", total_strokes)
print("Compared to par:", difference)
```

### Work time (35 min)
Students build their tracker, teacher circulates to help. Expect this to take most of the period, and that's fine.

### Wrap-up (5 min)
Quick check-in: "How far did you get?" No pressure to be finished — Session 12 is for finishing.

---

## SESSION 12: Finish, polish, and showcase

### Warm-up (5 min)
Continue project work from last session.

### Work time (25 min)
Finish the tracker. For kids who finish early, offer a stretch goal: use `input()` so a friend can type in their own scores live.

### Polish (10 min)
Encourage adding a fun final message, like printing "Great round!" if their total beats par, or letting them personalize their player name variable at the top.

### Showcase (10 min)
Have volunteers run their tracker for the class and share their results.

---

## Notes for you (the instructor)
- Don't worry about over-explaining `if / elif / else` the first time it comes up — kids absorb it faster by seeing it run than by hearing it described. Re-explain as needed; that's what the warm-up blocks are for.
- List indexing starting at 0 is consistently the trickiest concept — plan extra time there in Session 7.
- If a session runs short, the wrap-up/share time is the easiest thing to extend. If a session runs long, cut the wrap-up short rather than the independent practice.
- Common typos to watch for: missing colons `:` after `for`, `if`, and `def` lines, and indentation (Python cares about spacing at the start of a line).
- This plan is a living document — if the class needs an extra session on any topic, it's easy to split a session in two and push the rest back a week.
