from zeep import Client

# WSDL URL of the web service
wsdl_url = 'http://www.dneonline.com/calculator.asmx?WSDL'

# Create a SOAP client
client = Client(wsdl=wsdl_url)

# Get user input
try:
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
except ValueError:
    print("Please enter valid integers.")
    exit()

# Call and display results from WSDL service
try:
    add_result = client.service.Add(intA=a, intB=b)
    print(f"Add({a}, {b}) = {add_result}")

    subtract_result = client.service.Subtract(intA=a, intB=b)
    print(f"Subtract({a}, {b}) = {subtract_result}")

    multiply_result = client.service.Multiply(intA=a, intB=b)
    print(f"Multiply({a}, {b}) = {multiply_result}")

    if b != 0:
        divide_result = client.service.Divide(intA=a, intB=b)
        print(f"Divide({a}, {b}) = {divide_result}")
    else:
        print("Cannot divide by zero.")

except Exception as e:
    print("An error occurred while calling the SOAP service:", e)
