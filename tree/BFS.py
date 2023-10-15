from collections import deque
from tree.Node import Node, conversation
from bson import ObjectId
from constants import py_path, log_path, example_path
from tree.parser import extract_python_source_code
from open_ai_interfacing import *

examples = ["slide2tangent", "slide4", "slide10", "slide11"]

def BFS(text: str, depth: int):
    my_deque = deque()
    my_deque.append(Node(id = ObjectId(), level = 0, parent = None, text=text))
    level = 0
    sublevel = 0
    while my_deque:
        temp = my_deque.popleft()
        if (temp.level != level):
            level = temp.level
            sublevel = 0
        else:
            sublevel += 1
        if (sublevel >= 2):
            continue
        if (temp.level == depth):
            '''
            if (sublevel == 0):
                counter = 0
                chat_gpt("I have some examples of manim code. I want you to follow these", conversation, privilage='system')
                for example in examples:
                    with open(example_path.format(example), "r") as file:
                        print(counter)
                        chat_gpt(file.read(), conversation, privilage='system')
                        counter += 1
            '''
            txt = temp.last_query()
            print(level, sublevel, "\n", txt)
            try:
                open(py_path.format(sublevel), "x")
            except:
                pass
            with open(py_path.format(sublevel), "w") as file:
                file.write(extract_python_source_code(txt))
            temp.debug(sublevel)
        else:
            txt = temp.query()
            print(level, sublevel, "\n", txt)
            try:
                open(log_path.format(level, sublevel), "x")
            except:
                pass
            with open(log_path.format(level, sublevel), "w") as file:
                file.write(txt)
            for child in temp.children:
                my_deque.append(child)