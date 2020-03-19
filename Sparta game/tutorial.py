# TICKET_PRICE = 10
# SERVICE_CHARGE = 2
#
# tickets_remaining = 100
#
#
# def calculate_price():
#     price = (number_tickets * TICKET_PRICE) + SERVICE_CHARGE
#     print("£2 service charge has been added!")
#     return "The total is £{}".format(price)
#
#
# while tickets_remaining >= 1:
#     print("There are {} tickets remaining.".format(tickets_remaining))
#
#     name = input("Hello, What's your name? ")
#     number_tickets = input("How many tickets would you like {}? ".format(name))
#     number_tickets = int(number_tickets)
#
#     try:
#         if number_tickets > tickets_remaining:
#             raise ValueError("There are only {}".format(tickets_remaining))
#     except ValueError as err:
#         print("oh no, we ran into an issue, {} tickets remaining, please try again".format(err))
#     else:
#         print(calculate_price())
#
#         proceed = input("Would you like to proceed? ")
#         if proceed.lower() == "yes":
#             print("SOLD!")
#             tickets_remaining -= number_tickets
#         else:
#             print("Thank you {} for enquiring.".format(name))
#
# print("Sorry The tickets have sold out!!!")
#
# list_data = [10, 111, 24, 56, 78, 65, 80]
# even_list = []
# odd_list = []
# for num in list_data:
#     if num % 2 == 0:
#         even_list.append(num)
#     elif num % 2 != 0:
#         odd_list.append(num)
#     else:
#         continue
# print('Even list:', even_list)
# print('Odd list:', odd_list)

from random import randint

t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissors? ")

    if player == computer:
        print("Tie!")

    elif player == "Rock":

        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)

    elif player == "Paper":

        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)

    elif player == "Scissors":

        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]

