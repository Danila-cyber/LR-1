#Натуральные числа, содержащие не более двух групп из 5 подряд идущих 0. Список используемых в числах цифр выводить отдельно прописью. - Вариант 20

def checkNum(strNum):
  if strNum.isdigit():
    flag = True
    oneChar = True if int(strNum[0])%2==0 else False
    for i in range(1, len(strNum)):
      char = True if int(strNum[i])%2==0 else False
      if char != oneChar:
        oneChar = char
      else: flag = False
    return flag
  else: return False

nums = []
fileName = "ref1.txt"
try:
  open(fileName, "r")
except:
  print("Файл отсутствует")

with open(fileName, "r") as file:
  while True:
    line = file.readline().replace('\n', '')
    if not(line): break
    if checkNum(line): nums.append(line)
      
          
for num in nums:
  print(num)
  acceptChar = []
  for char in num:
    if int(char) % 2 == 0: acceptChar.append(char)
  print("Четные цифры этого числа: ")
  print(", ".join(acceptChar))
  print("|____________________|")

