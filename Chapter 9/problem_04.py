word = "donkey"
with open("chapter 9\\problem_04.txt", "r") as f:
    content = f.read()

contentnew = content.replace(word,"####")

with open("chapter 9\\problem_04.txt", "w") as f:
    content = f.write(contentnew)
