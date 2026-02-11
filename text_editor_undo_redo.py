"""
Text Editor with Undo/Redo using two stacks.

Idea:
Before every change, store current text in undo_stacl
When undo happens, move current text to redo_stack and restore from undo_stack
When redo happens, move current text to undo_stack and restore from redo_stack
"""


class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []  # previous states
        self.redo_stack = []  # states we can redo

    def write(self, new_text: str):
        # save current state for undo
        self.undo_stack.append(self.text)
        # new action clears redo history
        self.redo_stack.clear()
        self.text += new_text

    def delete(self, k: int):
        if k <= 0:
            return

        self.undo_stack.append(self.text)
        self.redo_stack.clear()

        if k >= len(self.text):
            self.text = ""
        else:
            self.text = self.text[:-k]

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return

        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return

        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()

    def show(self):
        return self.text


if __name__ == "__main__":
    editor = TextEditor()

    editor.write("Hello")
    editor.write(" world")
    print("Text:", editor.show())  # Hello world

    editor.delete(6)
    print("After delete:", editor.show())  # Hello

    editor.undo()
    print("After undo:", editor.show())  # Hello world

    editor.redo()
    print("After redo:", editor.show())  # Hello
