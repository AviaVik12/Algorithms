class StackError(Exception):
    pass


class Stack:
    def __init__(self):
        self._arr = []

    def push(self, item):
        self._arr.append(item)

    def pop(self):
        if self.is_empty():
            raise StackError('Impossible to pop an item from an empty stack')
        return self._arr.pop()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._arr)


brackets = [
    '(()())()'
    '',
    '(',
    ')',
    '(((((())))))',
    ')))(((',
    '(()()()',
    '()()()(',
    '()(()()((()())))'
]


def are_brackets_correct(seq: str) -> bool:
    if len(seq) == 0:
        return True
    stack = Stack()
    stack.push(seq[0])
    for item in seq[1:]:
        if item == '(':
            stack.push(item)
        else:
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


# for seq in brackets:
#     status = are_brackets_correct(seq)
#     print(f'{seq}: {status}')


for seq, status in zip(brackets, map(are_brackets_correct, brackets)):
    print(f'{seq}: {status}')


print('------------------------------------------')


# Easier way
def are_brackets_correct_2(seq: str) -> bool:
    if len(seq) == 0:
        return True
    stack = []
    stack.append(seq[0])
    for item in seq[1:]:
        if item == '(':
            stack.append(item)
        else:
            if not len(stack):
                return False
            stack.pop()
    return not len(stack)


for seq, status in zip(brackets, map(are_brackets_correct_2, brackets)):
    print(f'{seq}: {status}')


