import random

fruits = ['Apple', 'Banana', 'Grape', 'Orange', 'Kiwi','Dragonfruit','Gauaw','Pomogranate']

dice_art = {
          1: ("---------",
              "|       |",
              "|   *   |",
              "|       |",
              "---------"),
          2: ("---------",
              "| *     |",
              "|       |",
              "|     * |",
              "---------"),
          3: ("---------",
              "| *     |",
              "|   *   |",
              "|     * |",
              "---------"),
          4: ("---------",
              "| *   * |",
              "|       |",
              "| *   * |",
              "---------"),
          5: ("---------",
              "| *   * |",
              "|   *   |",
              "| *   * |",
              "---------"),
          6: ("---------",
              "| *   * |",
              "| *   * |",
              "| *   * |",
              "---------"),
            }

dice = []
num_of_dice = int(input("Enter the number of dice: "))
total = 0

for i in range(num_of_dice):
    dice.append(random.randint(1, 6))

print(dice)

#for i in dice:
#   for line in dice_art.get(i):
#      print(line)

for i in range(5):
    for die in dice:
        print(dice_art.get(die)[i], end=" ")
    print()

for i in range(num_of_dice):
    total += dice[i]
    
print(f"Total = {total}")