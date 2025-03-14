#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  
        self.knowledge =knowledge = [
             "str is a data type in Python",
             "programming is hard, but it's worth it",
             "JavaScript async web request",
             "Python function call definition",
             "object-oriented teacher instance",
             "programming computers hacking learning terminal",
             "pipenv install pipenv shell",
             "pytest -x flag to fail fast",
        ]
    

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) -1)]
   

teacher1 =Teacher("Edith", "Mackena")
print(teacher1.teach())
print(teacher1.teach())