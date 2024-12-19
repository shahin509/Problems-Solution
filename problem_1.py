class Queue:
    def __init__(self):
        self.en_stack = [] 
        self.de_stack = []  

    def enqueue(self, x: int) -> None:
        self.en_stack.append(x)

    def dequeue(self) -> int:
        try:
            if not self.de_stack:
                while self.en_stack:
                    self.de_stack.append(self.en_stack.pop())

            if not self.de_stack:
                raise IndexError("Dequeue from an empty queue")

            return self.de_stack.pop()
        except IndexError as e:
            print(f"Error: {e}")
            raise

q = Queue()
q.enqueue(1)        # Queue -> 1
q.enqueue(2)        # Queue -> 1 2
print(q.dequeue())  # Queue -> 2
q.enqueue(3)        # Queue -> 2 3
print(q.dequeue())  # Queue -> 3
