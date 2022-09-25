# number of vaccines

vaccines = []

timesVaccines = int(input("number of times when no person received the vaccine: "))
vaccines.append(timesVaccines)

for count in range(1, 4):
    timesVaccines = int(input("Enter the number of {} times: ".format(count)))
    vaccines.append(timesVaccines)


# return the array sorted by ascending order
def sortArrayAsc(array):
    return sorted(array)


# return the total sum of all numbers in the array
def getAccumulatorOfVaccines(arrayOfVaccines):
    totalVaccinesApplied = 0
    for i in arrayOfVaccines:
        totalVaccinesApplied += i

    return totalVaccinesApplied


print("sorted Vaccines Ascended {}\nand the total of vaccines are {}"
.format(
    sortArrayAsc(vaccines),
    getAccumulatorOfVaccines(vaccines)
))
