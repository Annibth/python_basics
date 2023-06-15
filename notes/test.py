class A :
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        
class B:
    def __init__(self,b) -> None:
        self.b = b
        
second = A("a",B("b"))

print(second.b)