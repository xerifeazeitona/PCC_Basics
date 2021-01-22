# 7-5. Movie Tickets
# A movie theater charges different ticket prices depending on a
# person’s age. If a person is under the age of 3, the ticket is free;
# if they are between 3 and 12, the ticket is $10; and if they are over
# age 12, the ticket is $15. Write a loop in which you ask users their
# age, and then tell them the cost of their movie ticket.
prompt = "\nEnter your age to find out the ticket price:"
prompt += "\n(Enter 'q' when you're done) "

while True:
    age = input(prompt)

    if age == 'q':
        break
    else:
        age = int(age)
        if age < 3:
            message = 'The ticket is free.'
        elif age > 12:
            message = 'The ticket is $15.'
        else:
            message = 'The ticket is $10.'

        print(message)
