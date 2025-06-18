import random


num_rolls = 30


count_6 = 0
count_1 = 0
two_6s_in_a_row = 0


previous_roll = 0


for _ in range(num_rolls):
    roll = random.randint(1, 6)
    
    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            two_6s_in_a_row += 1
    elif roll == 1:
        count_1 += 1

    previous_roll = roll  


print("Total rolls:", num_rolls)
print("Number of times 6 was rolled:", count_6)
print("Number of times 1 was rolled:", count_1)
print("Number of times two 6s occurred in a row:", two_6s_in_a_row)
