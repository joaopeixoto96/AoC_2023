import os
file_path = os.path.join('AoC_2023','day16.txt')

g = {complex(i,j): c for j, r in enumerate(open(file_path))
                     for i, c in enumerate(r.strip())}

def fn(todo):
    done = set()
    while todo:
        pos, dir = todo.pop()
        while not (pos, dir) in done:
            done.add((pos, dir))
            pos += dir
            match g.get(pos):
                case '|': dir = 1j; todo.append((pos, -dir))
                case '-': dir = -1; todo.append((pos, -dir))
                case '/': dir = -complex(dir.imag, dir.real)
                case '\\': dir = complex(dir.imag, dir.real)
                case None: break

    return len(set(pos for pos, _ in done)) - 1

print('Part 1 -',fn([(-1, 1)]))

print('Part 2 -',max(map(fn, ([(pos-dir, dir)] for dir in (1,1j,-1,-1j)
                        for pos in g if pos-dir not in g))))