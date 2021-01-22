# The input() function pauses your program and waits for the user to
# enter some text
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# We can make the program run as long as the user wants by putting most
# of the program inside a while loop
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'q' to end the program. "

message = ""
while message != 'q':
    message = input(prompt)

    if message != 'q':
        print(message)

# A new version of the same program, now with a control flag to define
# whether the program should stop or continue running
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'q' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'q':
        active = False
    else:
        print(message)

