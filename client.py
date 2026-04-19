import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 98.90.53.6 -p 11000")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

res1 = printer.printString("Hello World!")
print(f"Resultado printString: {res1}")

soma = printer.add(10, 25)
print(f"Resultado add(10, 25): {soma}")

invertida = printer.reverseString("ZeroC Ice")
print(f"Resultado reverseString: {invertida}")
