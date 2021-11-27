import matplotlib.pyplot as plt

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(5)

x = [1,5]
y = [2,4]

dx = x[1] - x[0]
dy = y[1] - y[0]

#   calculate the slope
slope = dy / dx
intercept = y[0] - slope * x[0]

xl = [0, x[0], x[1]]
yl = [intercept, y[0], y[1]]

x.append(0)
y.append(intercept)

# for i in range(21):
#     x.append(i)
#     y.append(i*0.25)

#plt.plot(x,y, 'o', color='black')
plt.scatter(x,y, edgecolor='black')
#plt.annotate("intercept", (0, intercept), xytext=(1,intercept-1), arrowprops={'arrowstyle': '->'})
plt.plot(xl,yl)     #draw line
# plt.text((x[0]+x[1])/2, y[0]-0.5, "Δx", ha='center')
# plt.text(x[1]+0.5, (y[0]+y[1])/2, "Δy", va='center', ha='center')
plt.xlabel('x')
plt.ylabel('y')
xint = range(0, 11)
yint = range(0, 11)
plt.xlim(xmin=0, xmax=10)
plt.ylim(ymin=0, ymax=10)
plt.xticks(xint)
plt.yticks(yint)
plt.minorticks_on()
plt.grid(True, which="major", axis="y")
plt.grid(True, which="major", axis="x")

ax = plt.gca()
ax.set_axisbelow(True)

f.savefig("pts-mb-04.svg")
#f.savefig("pts-mb-02.png")
plt.show()
