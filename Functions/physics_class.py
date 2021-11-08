# Getting Ready for Physics Class Project Code
# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Write your code below:
def f_to_c(f_temp):
  c_temp = round((f_temp - 32) * 5/9, 1)
  return c_temp

# Testing the function f_to_c:
f100_in_celsius = f_to_c(100)
print("The value of 100 degrees fahrenheit in celsius is", f100_in_celsius)

def c_to_f(c_temp):
  f_temp = round(c_temp * (9/5) + 32, 1)
  return f_temp

# Testing the function c_to_f:
c0_in_fahrenheit = c_to_f(0)
print("The value of 0 degree celsius in fahrenheit is", c0_in_fahrenheit)

def get_force(mass, acceleration):
  return mass * acceleration

#testing the function get_force:
train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies " + str(train_force) + " Newtons of force")

def get_energy(mass, c = 3*10**8):
  return mass*c**2

#Testing the function get_energy:
bomb_energy = get_energy(bomb_mass)
print("A {}kg bomb supplies {} Joules of energy".format(bomb_mass, bomb_energy))

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

#Testing the function get_work:
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over {} meters".format(train_work, train_distance))
