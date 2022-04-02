def permutations(start, end=[]):
    if len(start) == 0:
        print(end)
    else:
        for i in range(len(start)):
            permutations(start[:i] + start[i+1:], end + start[i:i+1])

def converir():
    n_str = input("ingresa los numeros con un espacio: ").split(' ')
    print(n_str)
    n = [int(x) for x in  n_str]
    print(n)
    permutations(n)

converir()

