m = {
    "A": { "n": "CB", "+": None, "*": None, "(": "CB", ")": None, "$": None },
    "B": { "n": None, "+": "+CB", "*": None, "(": None, ")": "", "$": "" },
    "C": { "n": "ED", "+": None, "*": None, "(": "ED", ")": None, "$": None },
    "D": { "n": None, "+": "", "*": "*ED", "(": None, ")": "", "$": "" },
    "E": { "n": "n", "+": None, "*": None, "(": "(A)", ")": None, "$": None }
}

#input
var1 = input("donner l'expression : ")
print(list(var1))

def estTerminal(x):
    if x in list("()+*n")[::-1]:
        return True 
    else:
        return False
var1 = ["(","n","+","n",")","$"]


def Analyseursyntax(entree):
    lapile = ["$","A"]  # la pile des symbole
    a = entree.pop(0)
    i=0

    while (True):
        i+=1
        print("here : ", lapile, end='')
        print("-------entree : ", ''.join(entree))
        x = lapile[-1]

        if (x == "$" and a == "$"):
            return True

        # etape 2  x est le sommet de la pile  & a est le symbole pointé
        if (x == a and x != "$"):
            lapile.pop()
            a = entree.pop(0)
            continue

        # etape 3
        if (not estTerminal(x)):
            p=m[x][a] # la derive de x 

            if (p == None): 
                return false
            else:    
                # dépiler        
                lapile.pop()

                # empiler la derivé à la place du symbole
                lapile.extend(list(p)[::-1])                
                continue                

        return false



print(Analyseursyntax(var1))