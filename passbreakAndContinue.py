for i in range(10):
    if i == 5:
        print("processing is enough... plz break")

    print(i)

lt = [10, 20, 400, 60, 70, 350]
for item in lt:
    if item > 300:
        print("please break the condition")
        continue
    print(item)

print("---")
for i in range(10):
    if i==7:
        print("skip the current iteration value: ")
        continue
    print(i)


def fun():
    pass
print(fun())