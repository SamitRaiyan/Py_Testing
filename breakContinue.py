for i in range(0,15):
    if i == 10:
        continue
    print("didn't skipped this number:", i)
    if i == 12:
        break
print("-----")
print("Loop ended. Cause it found:", i)