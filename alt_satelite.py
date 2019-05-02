G=6.67e-11
mt=5.97e24
Rt=6371e3
pi=3.1416
T=float(input("ingrese el periodo T en segundos..:"))
H=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("la altura del satelite en km del periodo ingresado es..: ",H*(1e-3))
T=5400
H=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("la altura en km para 90 min (5400 seg) es..:",H*(1e-3))
T=2700
H=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("la altura en km para 45 min (2700 seg) es..:",H*(1e-3))
T=86400
H=(((G*mt*T**2)/(4*pi**2))**(1/3))-Rt
print("la altura en km  para 1 dia (86400 seg) es..:",H*(1e-3))
T_1=86148
H_1=(((G*mt*T_1**2)/(4*pi**2))**(1/3))-Rt
print("la altura en km  para 1 dia sideral (86148 seg) es..:",H_1*(1e-3))
print("la diferencia en km de alturas entre un dia(24h) y un dia sideral(23.93h) es..:",(H-H_1)*(1e-3))
