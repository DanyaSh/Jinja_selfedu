"""
Lesson 01
code dict

"""

from jinja2 import Template

name='Федор'
age=28

tm=Template("Привет {{n.upper()}}, мне {{a+2}} лет!")

#-----------------The same functional of F-strings-----------------
msg_jinja=tm.render(n=name, a=age)
msg_fstr=f"Привет {name.upper()}, мне {age+2} лет!"

#-----------------The same functional of F-strings-----------------class
print(msg_jinja)
print(msg_fstr)

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

per=Person(name="Федор", age=28)

msg_jinja_1=tm.render(n=per.name, a=per.age)

tm=Template("Привет {{p.getName().upper()}}, мне {{p.getAge()+2}} лет!")
msg_jinja_2=tm.render(p=per)
msg_fstr_1=f"Привет {per.name.upper()}, мне {per.age+2} лет!"

print(msg_jinja_1)
print(msg_jinja_2)
print(msg_fstr_1)

#-----------------The others functional of F-strings-----------------
#find the data in dictionary like in object
dict_per={"name":"Федор", "age":28}

tm=Template("Привет {{p.name.upper()}}, мне {{p.age+2}} лет!")
msg_jinja_3=tm.render(p=dict_per)

msg_fstr_3=f"Привет {dict_per['name']}, мне {dict_per['age']} лет!"

print(msg_jinja_3)
print(msg_jinja_3)