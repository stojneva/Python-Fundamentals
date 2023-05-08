class Qna:

    def __init__(self, name):
        self.name = name

    def say_bye(self):
        return f"Bye {self.name}"

    def congrats(self):
        return f"You are the best {self.name}!"


q = Qna("Qna")

print(q.say_bye())
print(q.congrats())




