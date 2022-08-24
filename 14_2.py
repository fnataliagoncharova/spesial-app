total_num = int(input("сколько чисел будем вводить?  "))
cod = int(input("введите код операции: 1 - сложение , 2- вычитание, 3- умножение, 4 - деление "))
summ = 0
str_ = ""

if cod == 1:

  for i in range(1, total_num+1):
    j = int(input("введите число "))
    summ += j
    if i == 1:
      str_ = str(j)
    else:
      str_ += "+" + str(j)
if cod == 2:
  for i in range(1, total_num+1):
    j = int(input("введите число "))
    if i == 1:
      summ = j
      str_ = str(j)
    else:
      summ -= j
      str_ += "-" + str(j)
if cod == 3:
  for i in range(1, total_num+1):
    j = int(input("введите число "))
    if i == 1:
      summ = j
      str_ = str(j)
    else:
      summ *= j
      str_ += "*" + str(j)
if cod == 4:
  for i in range(1, total_num+1):
    j = int(input("введите число ку кк "))
    #str_ += "/" + str(j)
    if i == 1:
      summ = j
      str_ = str(j)
    else:
      summ /= j
      str_ += "/" + str(j) 
 
print(str_, "= ", summ )