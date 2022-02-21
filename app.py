valor = 0
escribir_num = input('Ingrese un número: ')
largo = len(escribir_num)
valor = int(escribir_num)
escritura = f'El número {valor}, se escribe:'


numeros_1_9 = {
  '1': 'Uno',
  '2': 'Dos',
  '3': 'Tres',
  '4': 'Cuatro',
  '5': 'Cinco',
  '6': 'Seis',
  '7': 'Siete',
  '8': 'Ocho',
  '9': 'Nueve'
}

def for1_al_9():
  for i in range(len(escribir_num)):
    for k, v in numeros_1_9.items():
      if escribir_num[i] == k:
        print(f'{escritura} {v}')
        break

def validar_10a15():
  if valor == 10:
    print(f'{escritura} Diez')
  elif valor == 11:
    print(f'{escritura} Once')
  elif valor == 12:
    print(f'{escritura} Doce')
  elif valor == 13:
    print(f'{escritura} Trece')
  elif valor == 14:
    print(f'{escritura} Catorce')
  elif valor == 15:
    print(f'{escritura} Quince')

def validar_16a99():
  global valor
  if valor < 20:
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Diez y {v}') # Evalua si es 16, 17, 18, 19
        break
  elif valor >= 20:
    if valor == 20:
      print(f'{escritura} Veinte')  # Evalua si es 20
    elif valor < 30:
      for k, v in numeros_1_9.items():
        if k == escribir_num[1]:
          print(f'{escritura} Veinti{v}') # Evalua si es del 21 hasta 29
          break
    else:
      if valor == 30:
        print(f'{escritura} Treinta')  # Evalua si es 30
      elif valor > 30 and valor < 40: # Evalua si es de 31 a 39
        for k, v in numeros_1_9.items():
          if k == escribir_num[1]:
            print(f'{escritura} Treinta y {v}')
            break
  if valor == 40:
    print(f'{escritura} Cuarenta') # Evalua si es 40
  elif valor > 40 and valor < 50: # Evalua si es de 41 a 49
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Cuarenta y {v}')
        break
  if valor == 50:
    print(f'{escritura} Cincuenta') # Evalua si es 50
  elif valor > 50 and valor < 60: # Evalua si es de 51 a 59
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Cincuenta y {v}')
        break
  if valor == 60:
    print(f'{escritura} Sesenta') # Evalua si es 60
  elif valor > 60 and valor < 70: # Evalua si es de 61 al 69
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Sesenta y {v}')
        break
  if valor == 70:
    print(f'{escritura} Setenta') # Evalua si es 70
  elif valor > 70 and valor < 80: # Evalua si es de 71 al 79
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Setenta y {v}')
        break
  if valor == 80:
    print(f'{escritura} Ochenta') # Evalua si es 80
  elif valor > 80 and valor < 90: # Evalua si es de 81 al 89
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Ochenta y {v}')
        break
  if valor == 90:
    print(f'{escritura} Noventa') # Evalua si es 90
  elif valor > 90 and valor < 100: # Evalua si es de 91 al 99
    for k, v in numeros_1_9.items():
      if k == escribir_num[1]:
        print(f'{escritura} Noventa y {v}')
        break

if largo <= 3:
  if largo == 3:
    print(escribir_num[0], escribir_num[1], escribir_num[2])
  else:
    if largo == 2:
      valor = int(escribir_num)
      if valor > 15:
        validar_16a99()
      else:
        validar_10a15()
    else:
      valor = int(escribir_num[0])
      if valor == 0:
        print(f'{escritura} Cero')
      else:
        for1_al_9()
        
else:
  print('Cantidad muy grande')

