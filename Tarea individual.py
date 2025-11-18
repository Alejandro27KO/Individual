total_segundos= int(input("ingrese el total de segundos "))
horas= total_segundos // 3600
segundos_restantes = total_segundos % 3600
minutos= segundos_restantes // 60
segundos= segundos_restantes % 60
print(f" {total_segundos} segundos son:{horas} horas,{minutos} minutos,{segundos} segundos.")