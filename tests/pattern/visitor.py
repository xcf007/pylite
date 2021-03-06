class Wheel:
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        visitor.visitWheel(self)
 
class Engine:
    def accept(self, visitor):
        visitor.visitEngine(self)
 
class Body:
    def accept(self, visitor):
        visitor.visitBody(self)
 
class Car:
    def __init__(self):
        self.engine = Engine()
        self.body  = Body()
        self.wheels = [Wheel("front"), Wheel("back")]
 
    def accept(self, visitor):
        visitor.visitCar(self)
        self.engine.accept(visitor)
        self.body.accept(visitor)
        for wheel in self.wheels:
            wheel.accept(visitor)
 
class PrintVisitor:
    def visitEngine(self, engine):
        print "Visiting engine"

    def visitBody(self, body):
        print "Visiting body"

    def visitWheel(self, wheel):
        print "Visiting "+wheel.name+" wheel"

    def visitCar(self, car):
        print "Visiting car"
 
car = Car()
visitor = PrintVisitor()
car.accept(visitor)
