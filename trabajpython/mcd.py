def mcd(nro1, nro2):
  while nro2 != 0:
    nro1, nro2 = nro2, nro1 % nro2
  return nro1

def mcdcuatronumeros(nro1, nro2, nro3, nro4):
  mcd_ab = mcd(nro1, nro2)
  mcd_cd = mcd(nro3, nro4)
  return mcd(mcd_ab, mcd_cd)

#ejemplo
nro1 = 18
nro2 = 36
nro3 = 54
nro4 = 27

mcd_cuatro = mcdcuatronumeros(nro1, nro2, nro3, nro4)
print(f"El MCD de {nro1}, {nro2}, {nro3} y {nro4} es: {mcd_cuatro}")