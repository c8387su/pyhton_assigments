	sayı = int(input("Bir sayı giriniz: "))
	if sayı > 1:
	  for i in range(2, sayı):
	    if (sayı % i) == 0:
	      print(sayı, "is not a prime number")
	      break
	    else:
	      print(sayı, "is a prime number")
	      break
	else:
	  print(sayı, "is not a prime number")


