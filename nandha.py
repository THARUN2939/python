n=int(input('Enter number of products: '))
bill={}
for i in range(n):
    product=input(f'\nEnter product no.{i+1}: ')
    price=int(input('Enter its price: '))
    bill.update({product:price})
ask=input('\nEnter product to get its price: ')
if ask in bill.keys():
    print(f'\nPrice of {ask} is {bill[ask]}.')
else:
    print(f'\nSorry, {ask} is not in your list.\n')