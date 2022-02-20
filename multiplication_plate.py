#Multiplication plate
numeric=1
while numeric <= 10:
   rowspan = 1
   while rowspan <= 10:
       print(numeric*rowspan, end='\t')
       rowspan = rowspan + 1
   print()
   numeric = numeric+1
