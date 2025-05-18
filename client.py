from zeep import Client

# WSDL URL of the web service
wsdl_url = 'http://www.dneonline.com/calculator.asmx?WSDL'

# Create a client
client = Client(wsdl=wsdl_url)

# Example operations
a = 10
b = 5

# Calling Add method
add_result = client.service.Add(intA=a, intB=b)
print(f"Add({a}, {b}) = {add_result}")

# Calling Subtract method
subtract_result = client.service.Subtract(intA=a, intB=b)
print(f"Subtract({a}, {b}) = {subtract_result}")

# Calling Multiply method
multiply_result = client.service.Multiply(intA=a, intB=b)
print(f"Multiply({a}, {b}) = {multiply_result}")

# Calling Divide method
divide_result = client.service.Divide(intA=a, intB=b)
print(f"Divide({a}, {b}) = {divide_result}")
