# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class SimpleTextEditor:
    def __init__(self):
        self.word = []
        self.undo_stack = []
        self.redo_stack = []

    def append(self, c):
        self.word.append(c)
        self.redo_stack.clear()
        self.undo_stack.append(('append', c))

    def backspace(self):
        if not self.word: return
        c = self.word.pop()
        self.redo_stack.clear()
        self.undo_stack.append(('bs', c))

    def undo(self):
        if not self.undo_stack: return
        op, c = self.undo_stack.pop()
        if op == 'append':
          self.word.pop()
          self.redo_stack.append((op, c))
        else:
          self.word.append(c)
          self.redo_stack.append((op, c))

    def redo(self):
        if len(self.redo_stack) == 0: return
        op, c = self.redo_stack.pop()
        if op == 'append':
          self.word.append(c)
          self.undo_stack.append((op, c))
        elif op == 'bs':
          self.word.pop()
          self.undo_stack.append((op, c))

    def display(self):
        return("".join(self.word))
