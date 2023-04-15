acl=int(input("Porfavor ingrese el numero de su acl: "))

if acl >=1 and acl <=99:
	print("la acl ingresada es estandar")
elif acl >=100 and acl <=200:
	print("la acl ingresada es extendida")
else:
	print("la acl no es extendida ni estandar, no corresponde")
