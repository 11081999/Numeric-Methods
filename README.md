# Numeric-Methods

Need to download matplotlib and sympy libraries 

# Mathematica #

(*Reliable Solution*)
f[x_] := x - Exp[-x]
NSolve[{f[x] == 0, x > 0}, x] // N
