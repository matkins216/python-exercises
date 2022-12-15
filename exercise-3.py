# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

age = input("input a dog's age in human years: ")

int(age)

if int(age) <= 2:
    age = int(age) * 10
    print(age)
else: 
    age = int(age) - 2 
    age = int(age) * 7
    age = int(age) + 20
    print(age)