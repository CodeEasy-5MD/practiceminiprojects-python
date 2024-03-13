bpay= float(input("Enter basic pay\n"))
ohours= int(input("Enter overtime hours worked\n"))

#code for overtime pay
if ohours >=1 and ohours <=50:
    opay = ohours * 300
if ohours > 50:
    opay = (50*300) + ((ohours-50)*350)

#calculate gpay
gpay = bpay + opay

#code to find paye
if gpay >= 50000:
    paye = 0.14 * gpay
elif gpay >= 40000 and gpay < 50000:
    paye = 0.12 * gpay
elif gpay >= 35000 and gpay < 40000:
    paye = 0.11 * gpay
elif gpay >= 25000 and gpay < 35000:
    paye = 0.08 * gpay
elif gpay >= 16000 and gpay < 25000:
    paye = 0.05 * gpay
elif gpay >= 9500 and gpay < 16000:
    paye = 0.03 * gpay
else:
    paye = 0

#defining constants (deductions)
NSSF = 80.00
NHIF = 320.00
SC = 100.00

#calculating net pay
npay = gpay - (NSSF + NHIF + SC + paye)

#display values in tabular format
print ("Gross Pay, paye, Net paye\n")
print (gpay, paye, npay)




