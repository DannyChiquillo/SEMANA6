#Si gasto hasta $100, pago con dinero en efectivo. Si no, si gasto más de $100 pero menos de $300, pago con tarjeta de débito. Si no, pago con
#tarjeta de crédito
#Obtencion de datos 
compra = int(input("Coloque el dato de su compra"))
#En el primer if estamos comparando todos aquellos datos
#Que sean menores o igual que a 100
if compra <= 100: 
 print ("Pago en efectivo")
#Elif significa que vamos evaluar otra condicion 
#And significa que vamos a evaluar 2 condiciones o 2 resultados
#Que se cumplan las condiciones de la izquierda y la derecha 
elif compra > 100 and compra < 300: 
 print ("Pago con tarjeta de débito")
#Permite que un programa ejecute unas instrucciones cuando se cumple 
#Una condición y otras instrucciones cuando no se cumple esa condición.
else: 
 print ("Pago con tarjeta de crédito")