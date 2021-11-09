
n=(int(input("Digite el numero de trabajadores")))

for i in range(n):

 Horas=(int(input("Digite el numero de horas trabajadas")))
 if (Horas<=40):
   salario=Horas*20
 else:
    HorasExt=Horas-40
    salario= (HorasExt *25)+40*20
  
 x=str(i)
 sl=str(salario)
 print('El salario para el trabajador '+x+' es de: '+sl)

  

