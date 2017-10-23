print "Super Market Pricing"

print "Stock_checking"
print  " "

cans = int(input("Enter the number of cans in the stock:"))
print " "
cans = int(cans)
print "Total number of cans are" ,cans



cp = 15
x = cans * cp


sp = 30
y = cans * sp


profit = y-x
print "Profit before offer",profit


print "You put an offer of:BUY_2 GET_1 FREE"

offer = cans//3
z = cans - offer
cpao = z * cp
spao = z * sp
pao = spao - cpao

print "Profit after offer", pao




