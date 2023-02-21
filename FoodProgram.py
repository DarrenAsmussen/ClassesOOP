import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0


# customer = fc.customer(570,"Danni Sellyar", "97 Mitchell Way Hewit Texas 76712", "dsellyarft@gmpg.org","254-555-9362",False,)

customer = fc.customer(
    569,
    "Aubree Himsworth",
    "1172 Moulton Hill Waco Texas 76710",
    "ahimsworthfs@list-manage.com",
    "254-555-2273",
    True,
)

print(f"Customer NAme: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for key, value in dict.items():
    transaction = fc.transaction(value[0], value[1], value[2], value[3])
    if customer.get_customerid() == transaction.get_customerid():
        print(
            f"Order Item: {transaction.get_item_name()} Price: ${float(transaction.get_cost())}"
        )
        order_total += transaction.get_cost()

print(f"Total Cost: ${float(order_total)}")
memberdiscount = order_total * 0.2

if customer.get_memberstatus == True:
    print(f"Member Discount: ${memberdiscount}")
    print(f"Total Cost After Discount: ${order_total - memberdiscount}")
