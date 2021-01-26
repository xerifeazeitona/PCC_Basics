"""
9-15. Lottery Analysis
You can use a loop to see how hard it might be to win the kind of
lottery you just modeled. Make a list or tuple called my_ticket. Write a
loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning
ticket.
"""

from random import choice

HAT = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E')

def draw_ticket():
    """Randomly select four numbers or letters from the hat."""
    ticket = []
    for dummy in range(1, 5):
        ticket.append(choice(HAT))
    return ticket

def match_ticket(ticket):
    """
    Keep pulling tickets until the pulled ticket matches the provided
    one.
    """
    tries = 0
    active = True

    print("Pulling random tickets...")
    while active:
        tries += 1
        pulled_ticket = draw_ticket()
        print(pulled_ticket, end="")
        print("                    ", end="\r")
        active = pulled_ticket != ticket
    print("\n...done!")
    print(f"The loop had to run {tries} times to pull a matching ticket.")


my_ticket = draw_ticket()
print(f"Your ticket is: {my_ticket}")
match_ticket(my_ticket)
