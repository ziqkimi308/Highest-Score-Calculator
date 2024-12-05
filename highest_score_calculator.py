"""
********************************************************************************
* Project Name:  Highest Score Calculator
* Description:   It calculates the highest number of all input
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

print("Welcome to the Highest Score Calculator!")
scores = input("Enter scores separated by space: ").split()

for i in range(0, len(scores)):
    scores[i] = int(scores[i])

highest_score = 0
for score in scores:
    if score > highest_score:
        highest_score = score

print(f"Highest score: {highest_score}")
