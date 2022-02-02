# Prediction calculator using a teams pass success rate
# Will return prediction for how many passes can be expected to be made in a row
# based on the current pass success rate. Credit @pythonFC for function.
# Functionality expanded to iterate 100,000x and print the average for more accuracy.

import random

keepPossession = True
passSkill = 77.6
passesComplete = 0
count = 0
iterations = 0
totalNumberIterations = 100000

while iterations <= totalNumberIterations:
    while keepPossession:
        if random.randint(0, 100) > passSkill:
            keepPossession = False
        else:
            passesComplete += 1
    count = count + passesComplete
    iterations = iterations + 1
else:
    average = count / totalNumberIterations
print("You can expect the team to make ", "{:.0f}".format(average), " passes before losing possession.")
