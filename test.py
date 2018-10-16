import random
import operator
import matplotlib


agents = []


agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])
agents.append([random.randint(0,99),random.randint(0,99)])


print (agents)
print (max(agents))
print (max(agents, key=operator.itemgetter(1)))

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
m = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(m[1],m[0], color='red')
matplotlib.pyplot.show()


"""
y0 = random.randint (0,99)
x0 = random.randint (0,99)


#agents.append([random.randint(0,99), random.randint(0,99)]) #how to get rid of y0 and x0

y1 = random.randint (0,99)
x1 = random.randint (0,99)

agents.append([y0,x0])
print (agents)

y0 = 50
x0 = 50

if random.random () < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1

if random.random () < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1

print (y0, x0)


y1 = 50
x1 = 50

if random.random () < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1

if random.random () < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1

print (y1, x1)

#pythagorian distance between y0, x0, and y1, x1
answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print (answer)
"""