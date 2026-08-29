# Программа для проверки кредитных карт

# ? 1. Удалить все символы с " " (пробелом) и "-"
# ? 2. Сложите все цифры, стоящие на нечетных позициях, считая справа налево.
# ? 3. Удвойте каждую вторую цифру, считая справа налево. Если результат — 
# ? двузначное число, сложите его цифры, чтобы получить однозначное число.
# ? 4. Сложите итоговые значения, полученные на шагах 2 и 3.
# ? 5. Если сумма делится на 10, номер кредитной карты действителен.

#14 (01:32:58) credit card validator 💳 [DIFFICULT]
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
# Переворачивает последовательность
card_number = card_number[::-1]
print(card_number)

# Step 2
for x in card_number[::2]:
  sum_odd_digits += int(x)

# Step 3
for x in card_number[1::2]:
  x = int(x) * 2
  if x >= 10:
    sum_even_digits += (1 + (x % 10))
  else: 
    sum_even_digits += x

# Step 4
total = sum_odd_digits + sum_even_digits

# Step 5
if total % 10 == 0:
  print("VALID")
else: 
  print("INVALID")

# Examples valid = 4111111111111111, 5555555555554444, 378282246310005