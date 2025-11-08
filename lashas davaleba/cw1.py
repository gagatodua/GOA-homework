print("""======Goa Cafe======
1.xinkali 10 lari
2.xachapuri 12 lari
3.burgeri 15 lari
4.pizza 14 lari""")

choice = int(input("enter your choice"))
amount = int(input("enter how many you want"))

if choice == 1:
    total = 10 * amount + 5
    delivery = total + 5
    if total >= 30:
        delivery = delivery - 5
        print(f"total  is  ${delivery}")
    print(f"total  is  ${delivery}")
elif choice == 2:
    total = 12 * amount
elif choice == 3:
    total = 15 * amount
    print(f"total  is  ${total}")
elif choice == 4:
   total = 10 * amount
   print(f"total  is  ${total}")
else:
    print("enter valid choice")