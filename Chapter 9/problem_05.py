words = ["donkey","ganda","good"]
with open("chapter 9\\problem_05.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#" * len(word))

with open("chapter 9\\problem_05.txt", "w") as f:
    content = f.write(content)
