# Podemos criar funções para modificar outras funções, estas funções são chamadas 'decorators'
# As funções são tratadas como valores em python

def announce(function):
  def otherFunction():
    print("About to run the function...")
    function()
    print("Done with the function")
  
  return otherFunction

@announce
def hello():
  print("Hello, world!")

hello()

# Aqui, definimos que queremos modificar a função hello, por a função que definimos acima
# Seria a mesma coisa de fazer o seguinte:
newFuntion = announce(hello)
newFuntion()