# Even with while loop
i = 1
while i < 30:
    if i % 2 == 0:
        print(i)
    i += 1

# Even with for loop
for n in range(1, 30):
    if n % 2 == 0:
        print(n)


# Odd with while loop
i = 1
while i < 30:
    if i % 2 != 0:
        print(i)
    i += 1

# Odd with for loop
for n in range(1, 30):
    if n % 2 != 0:
        print(n)

# Capstone
amount = 50000
acquisition_per_customer = 5

marketing_expense = amount * (25 / 100)
operation_expense = amount * (50 / 100)
acquisition_cost = amount * (25 / 100)

customers_that_can_be_acquire = acquisition_cost // acquisition_per_customer


print("FINANCIAL STATEMENT \n" + 
"----------------------------------------------\n"
f"MARKETING EXPENSE: GHS {marketing_expense}\n"+
"----------------------------------------------\n"
f"OPERATION EXPENSE: GHS {operation_expense}\n"+
"----------------------------------------------\n"
f"ACQUISITION COST: GHS {acquisition_cost}\n" +
"----------------------------------------------\n"
f"CUSTOMERS THAT CAN BE ACQUIRED: GHS {customers_that_can_be_acquire}\n" +
"----------------------------------------------\n")
