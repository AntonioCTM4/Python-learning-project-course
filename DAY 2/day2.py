
print("What´s your name? ")
name = input()
print(f"HELLO! '{name}' Please enter your total monthly sales: ")
montly_sells = float(input())

total_sell = round(montly_sells * 0.13,2)

print(f"Well done '{name}',\nif your total sales this month is {montly_sells} \nyou will receive {total_sell} in commissions")



