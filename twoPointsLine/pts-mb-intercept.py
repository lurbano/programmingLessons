import matplotlib.pyplot as plt

f = plt.figure()
f.set_figwidth(5)
f.set_figheight(5)

x = [1,5]
y = [2,4]

xl = [1,3,]
yl = [2,6]

# for i in range(21):
#     x.append(i)
#     y.append(i*0.25)

#plt.plot(x,y, 'o', color='black')
plt.scatter(x,y, edgecolor='black')
#plt.plot(xl,yl)     #draw line
#plt.text(2, 1.5, "Δx", ha='center')
#plt.text(3.5, 4, "Δy", va='center')
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

f.savefig("pts-mv-02.svg")
#f.savefig("pts-mb-02.png")
plt.show()
