import SimpleVector as sv 


v1 = (-1,0.5,0)
v2 = [0,1.0,-1]

print("\nScaled Vector: {}".format(sv.scale(v1,2)))
print("Addition: {}".format(sv.add(v1,v2)))
print("Subtraction: {}".format(sv.sub(v1,v2)))
print("Unit vector: {}".format(sv.unit(v1)))
print("New Vector: {}".format(sv.calcVec(v1,v2)))
print("Cross Product: {}".format(sv.cross3(v1,v2)))
print("Dot Product: {}".format(sv.dot(v1,v2)))
print("Magnitude of v1: {}".format(sv.magnitude(v1)))
print("Angle between v1 and v2: {}".format(sv.angle(v1,v2)))
print("Angle between v1 and v2: {}".format(sv.angle(v1,v2,u_type='rad')))
print("Angle between v1 and v2: {}".format(sv.angle(v1,v2,u_type='potato')))
print("Angle between v1 and v2: {}\n".format(sv.angle(v1,v2,u_type='deg')))
