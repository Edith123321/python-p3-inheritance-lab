#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge = []):
       super().__init__(first_name, last_name)
       self.knowledge = knowledge
    
    def learn(self, new_knowledge):
        return  self.knowledge.append(new_knowledge)


Edith = Student("Edith", "Mackena")
print(Edith.learn("English"))
print(Edith.learn("Java"))
print(Edith.knowledge)