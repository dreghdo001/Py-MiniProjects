from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
print(logo)

#Here we select "+"
ending = False
answers = []
while not ending:
    num1 = int(input("What's the first number?: "))
    
    for symbol in operations:
      print(symbol)  
    operation_symbol = input("Pick an operation: ")
    
    num2 = int(input("What's the next number?: "))
    
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {first_answer}")
    
    continue_thread = input(("Continue ? Press 'y' !!! Exit type 'n' !!!"))
    
    while continue_thread == 'y':
      operation_symbol = input("Pick an operation: ") 
      num3 = int(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      answer = calculation_function(first_answer, num3)
      
      first_answer = answer
      
      print(f"{answer} {operation_symbol} {num3} = {answer}")
      continue_thread = input(("Continue ? Press 'y' !!! Exit type 'n' !!!"))
    if continue_thread == 'n':
      ending = True
    print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")