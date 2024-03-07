# menu = {
#     1: {"name": 'espresso',
#         "price": 1.99},
#     2: {"name": 'coffee', 
#         "price": 2.50},
#     3: {"name": 'cake', 
#         "price": 2.79},
#     4: {"name": 'soup', 
#         "price": 4.50},
#     5: {"name": 'sandwich',
#         "price": 4.99}
# }



# def calculate_subtotal(order):
#     """ Calculates the subtotal of an order

#     [IMPLEMENT ME] 
#         1. Add up the prices of all the items in the order and return the sum
    
#     Args:
#         order: list of dicts that contain an item name and price

#     Returns:
#         float = The sum of the prices of the items in the order
#     """
#     print('Calculating bill subtotal...')
#     ### WRITE SOLUTION HERE
#     sum = 0
#     for item in order:
#         sum += item["price"]

        
#     return round(sum,2)

        
#     raise NotImplementedError()

# def print_order(order):
#     print('You have ordered ' + str(len(order)) + ' items')
#     items = []
#     items = [item["name"] for item in order]
#     print(items)
#     return order

# # This function is provided for you, and will display the menu
# def display_menu():
#     print("------- Menu -------")
#     for selection in menu:
#         print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
#     print()

# # This function is provided for you, and will create an order by prompting the user to select menu items
# def take_order():
#     display_menu()
#     order = []
#     count = 1
#     for i in range(3):
#         item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
#         count += 1
#         order.append(menu[int(item)])
#     return order

# '''
# Here are some sample function calls to help you test your implementations.
# Feel free to change, uncomment, and add these as you wish.
# '''
# def main():
#     order = take_order()
#     print(type(order))
#     print_order(order)

#     subtotal = calculate_subtotal(order)
#     print("Subtotal for the order is: " + str(subtotal))

#     # tax = calculate_tax(subtotal)
#     # print("Tax for the order is: " + str(tax))

#     # items, subtotal = summarize_order(order)

# if __name__ == "__main__":
#     main()


data = [2,3,5,7,11,13,17,19,23,29,31]

data = [x+3 for x in data]
print("Updating the list:",data)

new_data = [x*2 for x in data]
print("Creating new list", new_data)

fourx = [x for x in new_data if x%4==0]
print("Divisible by four",fourx)

fourxsub = [x-1 for x in new_data if x%4==0]
print("Divisible by four minius one", fourxsub)

nines = [x for x in range(100) if x%9==0]
print("Nines:", nines)

data = [x+3 for x in data]

using_range = {x:x*2 for x in range(12)}
print("Using Range()",using_range)

months = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

numdict = {x:x**2 for x in number}
print("Using one input list to create dict:", numdict)

months_dict = {key:value for (key,value) in zip(number,months)}
print("Using two lists", months_dict)


data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end=" ")