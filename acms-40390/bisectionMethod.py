def f(x):
	# Insert function here
	return x**3 - 25

def calculatePBound(a, b,):
	return (a + b) / 2

# Set parameters
initInterval = tuple([2, 3])
aBound = initInterval[0]
bBound = initInterval[1]
approximationError = 5 # 10^(-approximationError)

while abs(aBound - bBound) >= 10**(-approximationError):
	pBound = calculatePBound(aBound, bBound)
	if f(pBound)*f(aBound) >= 0:
		aBound = pBound
	elif f(pBound)*f(bBound) >= 0:
		bBound = pBound
	else:
		break

print(f"The root of f(x) is on the interval [{aBound}, {bBound}].")