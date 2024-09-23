x, y, z = [float(e) for e in input("Type 3 numbers : ").split(",")]
print(x, y, z)
zzang = (z if (z>x) else x) if(x>y) else(y if(y>z) else z)
print(zzang)