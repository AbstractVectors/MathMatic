from bson import ObjectId
from open_ai_interfacing import *
from tree.parser import extract_numbered_points
prompts = ["Identify and list at most 3 sections from the text. These sections should be logical breaking points in the text, with each section having a focus. The text is here: {0}.", 
        "For the {0} section, identify at most 5 key visual features to complement the raw text", 
        "Design an outline for an animation with each section as a slide while including the 5 visual features you described. For each slide, identify the specific elements needed for that animation. These elements include: 1. Geometric features limited to lines, polygons. 2. Mathematical representations limited to graphs, functions, coordinate planes, and matrices. 3. Markup elements limited to text, tables. Do not use categories unless necessary",
        #"For feature {0}, identify the specific elements needed for that animation. These elements include: 1. Geometric features limited to lines, polygons. 2. Mathematical representations limited to graphs, functions, coordinate planes, and matrices. 3. Markup elements limited to text, tables. Do not use categories unless necessary",
        "Design the manim animation to capture the visual for section: {0}. Only put code"]

        #"For the element {0}, create a numerical example",
        #"Design a manim animation to capture the example {0}. Use Code Only"]
parse = [3, 5, None]
debug_prompts = ["Your code had this error, regenerate code: {0}. Only put code"]
conversation = [{'role': 'system', 'content': 'You are an assistant for a math professor.'}]
conversation_level_tracker = {i: [] for i in range(len(prompts))}

from execute_manim import execute, ExitCode
from constants import py_path
from tree.parser import extract_python_source_code

class Node:
    def __init__(self, id, level : int, parent : 'Node', text : str, text2: str = None):
        self.id = id  
        self.children = []
        self.level = level
        self.parent = parent
        self.text = text
        if (len(text) > 1000):
            raise Exception("Input Too Large")
        else:
            self.text = text
        if (len(text) > 1000):
            raise Exception("Input Too Large")

    def query(self) -> str:
        txt = chat_gpt(prompts[self.level].format(self.text), conversation, level=self.level, conversation_level_tracker=conversation_level_tracker)
        parsed_list = extract_numbered_points(txt, parse[self.level])
        for str in parsed_list:
            self.children.append(Node(id = ObjectId(), parent=self, level = self.level + 1, text = str))
        return txt
    
    def last_query(self) -> str:
        return chat_gpt(prompts[self.level].format(self.text), conversation,  level=self.level, conversation_level_tracker=conversation_level_tracker)
        
    def debug(self, sublevel: int) -> bool:
        success = False
        for i in range(3):
            content = ""
            with open(py_path.format(sublevel), "r") as file:
                content = file.read()
            print(content)
            output : tuple = execute(file_path=py_path.format(sublevel))
            print("Debug", i, "\n", output)
            if output[0] == ExitCode.OK:
                success = True
                break
            else:
                updated_code = chat_gpt(debug_prompts[0].format(output[1][-2000:]), conversation)
                with open(py_path.format(sublevel), "w") as file:
                    file.write(extract_python_source_code(updated_code))
        if not success:
            output : tuple = execute(file_path=py_path.format(sublevel))
            if output[0] == ExitCode.OK:
                success = True
        return success

    def verify(self) -> bool:
        prompt = "Return True or False"
        pass

    def isDeep(self) -> bool:
        prompt = ""
        pass

if __name__ == "__main__":
    print("Compiling")