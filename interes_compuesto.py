#INPUT

C= float(input ( "Digite la capital inicial :"  ) ) 


# PROCESSING

n=0

d= 2*C

while ( C<=d) : 

    C= 1.05*C

    n= n+1 

# Output

print ( "La capital acumulada es :"  , C )

print ( "Su capital inicial se duplico en: " , n ,"meses")