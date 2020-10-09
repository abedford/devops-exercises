

def divisibleBy(number, rule):
    if (number % rule == 0):
        return True
    return False


def print_number(number, rules):
    divisibleBy3bool = divisibleBy(number, 3) and 3 in rules
    divisibleBy5bool = divisibleBy(number, 5) and 5 in rules
    divisibleBy7bool = divisibleBy(number, 7) and 7 in rules
    divisibleBy11bool = divisibleBy(number, 11) and 11 in rules
    divisibleBy13bool = divisibleBy(number, 13) and 13 in rules
    divisibleBy17bool = divisibleBy(number, 17) and 17 in rules

    resultString =""
    if (divisibleBy11bool):
        
        if (divisibleBy13bool):
            resultString += "Fezz"
        resultString += "Bong"
    elif (divisibleBy3bool or divisibleBy5bool or divisibleBy7bool or divisibleBy13bool or divisibleBy17bool):
        
        ruleStrings = []
        if (divisibleBy3bool):
            ruleStrings.append("Fizz")
        
        if (divisibleBy13bool):
            ruleStrings.append("Fezz")
               
        if (divisibleBy5bool):
            ruleStrings.append("Buzz")

        if (divisibleBy7bool):
            ruleStrings.append("Bang")
        
        if (divisibleBy17bool):
            index = len(ruleStrings) - 1
            while(index >= 0):
                resultString += ruleStrings[index]
                index -= 1

        else:
            for ruleString in ruleStrings:
                resultString += ruleString
    else:
        resultString = number

    print(number, " ", resultString)


print("Welcome to the Fizz Buzz exercise program.")
max_number = input("Enter max number to calculate to:")

print("Enter which rules you'd like to use, options are 3, 5, 7, 11, 13, 17, anything else will run the program.")
run_program = False
possibleRules = [3, 5, 7, 11, 13, 17]
user_rules = []
while not(run_program):
    rule = input("Type a rule, or press any other key to stop inputting rules and run the program: ")
    try:
        ruleNumber = int(rule)
        if (ruleNumber in possibleRules):
            user_rules.append(ruleNumber)
        else:
            run_program = True
    except:
        print("That is not a valid rule, starting program.")
        run_program = True


for index in range(0, int(max_number)):
    print_number(index, user_rules)


