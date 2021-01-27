"""
Testing a class is similar to testing a function—much of your work
involves testing the behavior of the methods in the class. But there are
a few differences, so let’s write a class to test. 
"""

class AnonymousSurvey:
    """Collects anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store answers."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a singe response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
            