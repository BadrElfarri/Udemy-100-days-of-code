# Calculate the bill per person@
print('Welcome to the tip calculator!')
total = int(input('What was the total bill?\n'))
tip = int(input('How much tip would you like to give in % (write 10 for 10% \
                    of total bill)?\n'))
split_on = int(input('How many people to split the bill?\n'))

price_per_person = round(total*(1+tip/100)/split_on, 2)
print('price per person {0}$'.format(str(price_per_person)))
