import math

v = int(input('Enter a velocity in m/s:')) # With which bird was flung
a = int(input('Enter an angle in degrees:')) # With respect to the horizontal
d = int(input('Enter distance to structure in m:'))
h = int(input('Enter a height in m:')) #Height of structure
g = -9.8 # m/s^2

tower_height = h - 5

degC = math.pi / 180 
ar = a * degC  # Degrees into radians for computational purposes 

x = v * math.cos(ar)
y = v * math.sin(ar)

t = d / x # Time to reach structure
vf = d / t # Final velocity
dy = (y * t) +  ((1/2) * (t ** 2) * g) # Vertical position
dx = (y * t) +  ((1/2) * (t ** 2) * g) # Horizontal position
'''
if dy + 5 > h or dy + 5 < 0:
    boolean = 'did not hit'
else:
    boolean = 'hit'
'''    
print('Did the Red Bird hit the structure? Let\'s review the results:\n')
print('Your Red Bird reached the structure in ', t, 's')
print('and was traveling at a velocity of ', vf, 'm/s')
print('The Red Bird was at a height of', dy + 5, 'm from the ground')
print('when it reached your intended structure, so your Red Bird', '', 'the structure.')

