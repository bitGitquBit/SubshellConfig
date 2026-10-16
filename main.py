# give subshell config after recieving Z as input
# TODO: incorporate n+l rule

orbital_sizes = [2, 6, 10, 14]

Z = int(input("Proton Number: "))
orbital_config = [0]
cnt = 0
n,l = 1,0 #(initiall s orbital)

def display_config(config):
    maps = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f']
    for orbital_i in range(len(config)):
        print(maps[orbital_i] + '^' + str(config[orbital_i]), end = ' ')
    print()


while cnt < Z:
    orbital_config[-1] += 1

    if orbital_config[-1] == orbital_sizes[l]: # if subshell filled, move on to the next
        orbital_config.append(0)
        l = (l+1) % n
        if l == 0:
            n += 1

    cnt += 1

display_config(orbital_config)
