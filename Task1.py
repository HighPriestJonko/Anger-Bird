import math

v = int(input('Enter a velocity in m/s:')) # With which bird was flung
a = int(input('Enter an angle in degrees:')) # With respect to the horizontal
d = int(input('Enter distance to structure in m:'))
h = int(input('Enter a height in m:')) # Height of structure
g = 9.8 # m/s^2

degC = math.pi / 180
ar = a * degC  # Degrees into radians for computational purposes 

# Tips to you, you should use meaningful name for variables,
# instead of using x,y,z and it is a bad thing.
horizontal_speed = v * math.cos(ar)
vertical_speed = v * math.sin(ar)

t = d / horizontal_speed # Time to reach structure
vf_vertical = vertical_speed + g*t # Final vertical velocity

dy = (vertical_speed * t) +  ((1/2) * g * (t ** 2)) # Vertical position
dx = horizontal_speed * t # Horizontal position

v_co_speed = math.sqrt(vf_vertical * vf_vertical + horizontal_speed * horizontal_speed)

print('Did the Red Bird hit the structure? Let\'s review the results:\n')
print('Your Red Bird reached the structure in ', t, 's')
print('and was traveling at a velocity of ', v_co_speed, 'm/s')
print('The Red Bird was at a height of', dy + h, 'm from the ground')
print('when it reached your intended structure, so your Red Bird', '', 'the structure.')

