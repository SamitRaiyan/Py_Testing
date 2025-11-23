f = open('marks.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0]) # splitting line at comma and converting to int
  m2 = int(line.split(",")[1]) # splitting line at comma and converting to int
  m3 = int(line.split(",")[2]) # splitting line at comma and converting to int
  print(f"Marks of student {i} in Maths is: {m1}")
  print(f"Marks of student {i} in English is: {m2}")
  print(f"Marks of student {i} in SST is: {m3}")

#   print(line)
  print("")


f.close()