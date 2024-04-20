price = 0
order = []



def orderFood():
    global price

    order_food = int(input('What would you like to get?\n1. Burger\n2. Pizza\n3. Pie\n: '))

    match order_food:
        case 1:
            burger = int(input('Which burger would you like?\n1. Big Eddy - R54.99\n'
                               '2. Cool Joe - R44.99\n3. Slim Andy - R29.99\n: '))
            match burger:
                case 1:
                    num = int(input('How many Big Eddies would you like?\n: '))
                    price = price + (54.99 * num)
                    confirm_order = str(input(f'Confirm order: Big Eddy x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{54.99 * num}\n: '))

                    if confirm_order.lower() == 'y':
                        order.append(f'Big Eddie x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

                case 2:
                    num = int(input('How many Cool Joes would you like?: '))
                    price = price + (44.99 * num)
                    confirm_order = str(input(f'Confirm order: Cool Joe x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{44.99 * num}\n: '))

                    if confirm_order.lower() == 'y':
                        order.append(f'Cool Joe x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

                case 3:
                    num = int(input('How many Slim Andy would you like?: '))
                    price = price + (29.99 * num)
                    confirm_order = str(input(f'Confirm order: Slim Andy x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{29.99 * num}\n: '))

                    if confirm_order.lower() == 'y':
                        order.append(f'Slim Andy x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

        case 2:
            pie = int(input('1. Chicken and Mushroom - R49.99\n2. BBQ and Onion - R45.99'
                            '\n3. Creamy Cabbage - R53.99\n: '))
            match pie:
                case 1:
                    num = int(input('How many Pizzas would you like?: '))
                    price = price + (49.99 * num)
                    confirm_order = str(input(f'Confirm order: Chicken & Mushroom x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{49.99 * num}\n: '))
                    if confirm_order.lower() == 'y':
                        order.append(f'Chicken and Mushroom Pizza x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

                case 2:
                    num = int(input('How many Pizzas would you like?: '))
                    price = price + (45.99 * num)
                    confirm_order = str(input(f'Confirm order: BBQ & Onion Pizza x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{45.99 * num}\n: '))
                    if confirm_order.lower() == 'y':
                        order.append(f'BBQ and Onion Pizza x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

                case 3:
                    num = int(input('How many Pizzas would you like?: '))
                    price = price + (53.99 * num)
                    confirm_order = str(input(f'Confirm order: Creamy cabbage x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{53.99 * num}\n: '))
                    if confirm_order.lower() == 'y':
                        order.append(f'Creamy Cabbage Pizza x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

        case 3:
            pie = int(input('1. Chicken Pie - R19.99\n2. Beef Pie - R24.99: '))
            match pie:
                case 1:
                    num = int(input('How many Chicken Pies would you like?: '))
                    price = price + (19.99 * num)
                    confirm_order = str(input(f'Confirm order: Chicken Pie x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{19.99 * num}\n: '))
                    if confirm_order.lower() == 'y':
                        order.append(f'Creamy Cabbage Pizza x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True

                case 2:
                    num = int(input('How many Beef Pies would you like?: '))
                    price = price + (24.99 * num)
                    confirm_order = str(input(f'Confirm order: Beef Pie x{num}\n'
                                              f'Press Y for Yes and N for NO'
                                              f'\nPrice - R{24.99 * num}\n: '))
                    if confirm_order.lower() == 'y':
                        order.append(f'Beef Pie x{num}')
                        print(order)
                        print('Total price: R',price)
                        return True


def welcome():
    print('****Welcome to ABC fast food****\nWe sell Burgers, Pizzas, Sandwiches, Pie and beverages')

welcome()
orderFood()
while True:
    order_again = input('Do you want to order something else?\nPress y for yes or n for no\n: ')
    if order_again.lower() == 'y':
        orderFood()

    else:
        print(f'Your order for:  {order} for R{price} has been placed\nThank you :)')
        break
