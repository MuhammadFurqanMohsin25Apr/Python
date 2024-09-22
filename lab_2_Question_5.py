call_num = int(input("Enter the number of calls: "))
charges_1 = 2000

if call_num <= 100:
    print("Your monthly telephone bill is: Rs", charges_1)
elif call_num > 100 and call_num <= 150:
    bill = charges_1 + (call_num - 100) * (0.60)
    print("Your monthly telephone bill is: Rs", bill)
elif call_num > 150 and call_num <= 200:
    bill = charges_1 + (50 * 0.60) + (call_num - 150) * (0.50)
    print("Your monthly telephone bill is: Rs", bill)
else:
    bill = charges_1 + (50 * 0.60) + (50 * 0.50) + (call_num - 200) * (0.40)
    print("Your monthly telephone bill is: Rs", bill)
