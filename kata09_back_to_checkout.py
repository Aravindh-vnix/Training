#kata09-Back to the checkout http://codekata.com/kata/kata09-back-to-the-checkout/

"""Value of the each product"""
A = 50
B = 30
C = 20
D = 15
"""Getting the total number of items"""
tot_a = input("Enter the total number of A you want to buy:")
tot_b = input("Enter the total number of B you want to buy:")
tot_c = input("Enter the total number of C you want to buy:")
tot_d = input("Enter the total number of D you want to buy:")

Total = (A*tot_a)+(B*tot_b)+(C*tot_c)+(D*tot_d)

print "Total amount before offer", Total

of_b = tot_b//2
z = tot_b*30
if (of_b==0):
    y = z-(tot_b*7.5)
else:
    y = z-(z/6)

After_offer = (A*tot_a)+y+(C*tot_c)+(D*tot_d)
print "Total amount after offer", After_offer