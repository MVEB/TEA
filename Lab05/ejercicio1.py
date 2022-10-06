chr = "X-DSPAM-Confidence:0.8475"

pi = chr.find(":")
print("Inicia en el Indice: "+ str(pi))

pf = chr.find("5")
print("Termina en: "+ str(pf))

leng = len(chr)
substring = chr[pi+1:leng]
numer = float(substring)

print(numer)
print(type(numer))