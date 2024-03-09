#Натуральные числа, в которых строго чередуются четные и нечетные цифры. Список используемых в числах четных цифр выводить отдельно прописью. - Вариант 20

def checkNum(strNum):
  if "-" in strNum or strNum == "": return False
  else:
    flag = True
    oneChar = True if int(strNum[0])%2==0 else False
    for i in range(1, len(strNum)):
      char = True if int(strNum[i])%2==0 else False
      if char != oneChar:
        oneChar = char
      else: flag = False
    return flag

nums = []
fileName = "ref1.txt"
dc_cifr = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
try:
  open(fileName, "r")
except:
  print("Файл отсутствует")

with open(fileName, "r") as file:
  while True:
    line = file.readline().replace('\n', '')
    if not(line): break
    if (line.replace(" ", "")).isalpha() == False and (line.replace(" ", "")).isdigit() == False: continue
    num = ""
    if line.isdigit(): nums.append(line)
    else:
      for index in range(0, len(line)):
        if line[index].isdigit():
          num += line[index]
        if not(line[index].isdigit()) or index == (len(line) - 1):
          if checkNum(num): nums.append(num)
          num = ""
          
for num in nums:
  print(num)
  acceptChar = []
  for char in num:
    if int(char) % 2 == 0: acceptChar.append(char)
  print("Четные цифры этого числа: " + ", ".join(list(map(lambda x: dc_cifr[x], acceptChar))))
  print("____________________")

