import math

def find_code (Vout, R1, R2, R3):
  Rls=R1*(1.25/(Vout-1.25))
  Rdp=(Rls*(R2+R3)-R2*R3)/(R2-Rls)
  N_dec=(Rdp-75)*256/10000
  return hex(math.floor(N_dec))

def find_supply (N, R1, R2, R3):
  N_dec = int(N, base=16)
  Rdp=75+10000*N_dec/256
  Rls=R2*(R3+Rdp)/(R2+R3+Rdp)
  Vout=1.25*(1+R1/Rls)
  return Vout

R11=360
R12=4990
R13=499
R21=4220
R22=4020
R23=4990

print ("Vout1 =",find_supply("80", R11, R12, R13))
print ("Vout2 =",find_supply("80", R21, R22, R23))
print ("code1 =",find_code(2, R11, R12, R13))
print ("code2 =",find_code(3.5, R21, R22, R23))