# 文档 http://algorithmicbotany.org/papers/abop/abop-ch1.pdf
from turtle import *
speed(0)
pensize(2)


def split_path(path):
    i = 0
    l = []
    while i < len(path):
        if path[i] == "F":
            l.append(path[i:i+2])
            i += 2
        else:
            l.append(path[i])
            i += 1
    return l


def apply_rule(path, rules):
    l = split_path(path)
    for i in range(len(l)):
        symbol = l[i]
        if symbol in rules:
            l[i] = rules[symbol]
    path = "".join(symbol for symbol in l)
    return path


def draw_path(path):
    l = split_path(path)
    for symbol in l:
        if symbol == "Fl"or symbol == "Fr":
            forward(length)
        elif symbol == "-":
            right(angle)
        elif symbol == "+":
            left(angle)


length = 6
angle = 60

path = "Fr"
A_rules = {
    "Fl": "Fl+Fr+",
    "Fr": "-Fl-Fr",
}
B_rules = {
    "Fl": "Fr+Fl+Fr",
    "Fr": "Fl-Fr-Fl",
}
for _ in range(10):
    path = apply_rule(path, B_rules)
draw_path(path)
exitonclick()
