def move_water(a1, a2, collect = {}):
    j1, j2, target = 10, 3, 1

    if (a1 == target and a2 == 0):
        print(a1, a2)
        return True

    if (a1, a2) not in collect:
        collect[(a1, a2)] = True
        print(a1, a2)

        return (
            move_water(j1, a2)
            or move_water(a1, j2)
            or move_water(a1, 0)
            or move_water(0, a2)
            or move_water(a1 + min(a2, (j1 - a1)), a2 - min(a2, (j1 - a1)))
            or move_water(a1 - min(a1, (j2 - a2)), a2 + min(a1, (j2 - a2)))
            )
    else:
        return False

def main():
    move_water(0, 0)

if __name__ == '__main__':
    main()