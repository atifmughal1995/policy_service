
# CREDIT POLICY SERVICE - ASSIGNMENT

## APPROACH
At first, I did some search on the credit policies from simple ones to complex ones. To get an idea about the factors on which these policies depend and what could be the other factors in our case. And how to design a service in a way that can be shape easily for complex use cases. 

## DESIGN
I broke down the service into four main parts:

### •	Base Service Class (base_service_class.py)

This class provides a basic template to develop a service. It has the necessary functions like "request_data" which extracts POST request data, "success_response" which is used to send response in case of success and "error_response" in case of failure. And it can also be used to develop new services.


### •	Validators (validators.py)

This class has different validation methods that are used to validate POST request data.
For complex credit policies more validation methods can be added here. And can also be used easily in a service to validate data.


### •	Policy Service (policy_service.py)

This is the main class which uses base service class and validators. It consists of core logic which evaluates the credit eligibility against the input data.


### •	Server (run_server.py)

This file contains a function which takes service (class name), IP and port and starts a server and provides an endpoint through which request can be sent to that server. 
	

## BENEFITS OF THIS DESIGN

### •	Scalability/Flexibility
This design provides us a great scalability and flexibility in terms of adding functionality and making changes to our service. Like we can write a function that can handle a GET Request in our service. Similarly, if we require other validation checks we can easily write a new validation method without making a big change to our service instead of just calling that function in our service. 

### •	Reusability
As we can see a Base Service Class is implemented in order to provide us basic functionality for a service. In case if we develop a new service, we don’t have to implement the basic functionality for a service again. Similarly, Validators class can be used in other services too for validation purpose.


## HOW TO SETUP
There isn’t anything that is required to run the project except from Python obviously.
Preferred Python version is 3.6.5 or greater.


## HOW TO RUN
1.	Go to /assignment folder.

2.	Run the policy_service.py file. Using following command:
python policy_service.py
3.	The server is started now. Now open a new command prompt. Use the following command (curl command) to send POST request to the server:

curl -H "Content-Type: application/json" -X POST http://127.0.0.1:8000 -d "{\"customer_income\": 1000, \"customer_debt\": 300, \"payment_remarks_12m\": 0, \"payment_remarks\": 1, \"customer_age\": 18}"



## EXAMPLES

### Input 1:
{
    "customer_income": 1000,
    "customer_debt": 300,
    "payment_remarks_12m": 0,
    "payment_remarks": 1,
    "customer_age": 18
}	
### Output 1:
{
  "status": "ACCEPT"
}

### Input 2:
{
    "customer_income": 500,
    "customer_debt": 300,
    "payment_remarks_12m": 0,
    "payment_remarks": 1,
    "customer_age": 18
}	
### Output 2:
{
  "status": "REJECT",
  "reason": "LOW_INCOME"
}

### Input 3:
{
    "customer_income": 1000,
    "customer_debt": 700,
    "payment_remarks_12m": 0,
    "payment_remarks": 1,
    "customer_age": 18
}	
### Output 3:
{
  "status": "REJECT",
  "reason": "HIGH_DEBT_FOR_INCOME"
}

### Input 4:
{
    "customer_income": 1000,
    "customer_debt": 300,
    "payment_remarks_12m": 0,
    "payment_remarks": 1,
    "customer_age": 13
}	
### Output 4:
{
  "status": "REJECT",
  "reason": "UNDERAGE"
}

### Input 5:
{
    "customer_income": 1000,
    "customer_debt": 300,
}	
### Output 5:
{
  "status": "REJECT",
  "reason": "INVALID_INPUT",
  "message": "payment_remarks_12m, payment_remarks & customer_age fields are required."
}

### Input 6:
{
    "customer_income": -10,
    "customer_debt": 300,
    "payment_remarks_12m": 0,
    "payment_remarks": -1,
    "customer_age": 18
}	
### Output 6:
{
  "status": "REJECT",
  "reason": "INVALID_INPUT",
  "message": "customer_income & payment_remarks fields are invalid. Input should be a non-negative number."
}

