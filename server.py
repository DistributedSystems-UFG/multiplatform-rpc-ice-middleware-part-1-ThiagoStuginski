import sys, Ice
import Demo
 
class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"
        
    def add(self, n1, n2, current=None):
        print(f"Somando: {n1} + {n2}")
        return n1 + n2

    def reverseString(self, s, current=None):
        print(f"Invertendo: {s}")
        return s[::-1]

communicator = Ice.initialize(sys.argv) 

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()
