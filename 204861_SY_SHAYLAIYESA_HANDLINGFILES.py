def get_product(code):
    info = products[code]
    return info

def get_property(code,property):
    value = products[code][property]
    return value

def main():

    all_items = []
    americano = 0
    brewed = 0
    cappuccino = 0
    dalgona = 0
    espresso = 0
    frappuccino = 0

    #items list,qty
    while True:
        order = input("Input order: ")
        if order == "/":
            break
        order_list = order.split(",")
        item = order_list[0]
        qty = int(order_list[1])
        if item not in all_items:
            all_items.append(item)
        if item == "americano":
            americano += qty
        elif item == "brewedcoffee":
            brewed += qty
        elif item == "cappuccino":
            cappuccino += qty
        elif item == "dalgona":
            dalgona += qty
        elif item == "espresso":
            espresso += qty
        elif item == "frappuccino":
            frappuccino += qty

    #adding qty
    all_items.sort()
    for i in range(len(all_items)):
        if all_items[i] == "americano":
            get_product("americano")["qty"] = americano
        elif all_items[i] == "brewedcoffee":
            get_product("brewedcoffee")["qty"] = brewed
        elif all_items[i] == "cappuccino":
            get_product("cappuccino")["qty"] = cappuccino
        elif all_items[i] == "dalgona":
            get_product("dalgona")["qty"] = dalgona
        elif all_items[i] == "espresso":
            get_product("espresso")["qty"] = espresso
        elif all_items[i] == "frappuccino":
            get_product("frappuccino")["qty"] = frappuccino

    with open("receipt.txt","w") as receipt:
        total = 0
        receipt.write('''
==
CODE\t\t\t\t\tNAME\t\t\t\t\t\tQUANTITY\t\tSUBTOTAL''')

        for i in range(len(all_items)):
            code = all_items[i]
            name = get_property(code,"name")
            quantity = get_property(code,"qty")
            subtotal = quantity * get_property(code,"price")
            total += subtotal

            if code == "americano":
                receipt.write(f'''
{code}\t\t\t{name}\t\t\t\t{quantity}\t\t\t\t\t\t{subtotal}''')
            elif code == "brewedcoffee":
                receipt.write(f'''
{code}\t{name}\t\t{quantity}\t\t\t\t\t\t{subtotal}''')
            elif code == "cappuccino":
                receipt.write(f'''
{code}\t\t{name}\t\t\t{quantity}\t\t\t\t\t\t{subtotal}''')
            elif code == "dalgona":
                receipt.write(f'''
{code}\t\t\t\t{name}\t\t\t\t\t{quantity}\t\t\t\t\t\t{subtotal}''')
            elif code == "frappuccino":
                receipt.write(f'''
{code}\t\t{name}\t\t\t{quantity}\t\t\t\t\t\t{subtotal}''')
            elif code == "espresso":
                receipt.write(f'''
{code}\t\t\t{name}\t\t\t\t{quantity}\t\t\t\t\t\t{subtotal}''')

        receipt.write(f'''

Total:\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{total}
==
        ''')

main()
