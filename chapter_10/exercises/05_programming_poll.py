"""
10-5. Programming Poll
Write a while loop that asks people why they like programming. Each time
someone enters a reason, add their reason to a file that stores all the
responses.
"""
prompt = "Why do you like programming?"
prompt += "\n(Enter 'q' to quit): "

with open('poll_results.txt', 'w') as file_object:
    while True:
        reason = input(prompt)
        if reason == 'q':
            break
        else:
            file_object.write(reason + "\n")
