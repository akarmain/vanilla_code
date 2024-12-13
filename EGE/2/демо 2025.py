# ((w → y) → x) \/ ¬z,
print("x y w z")
def main():
    for w in (True, False):
        for y in (True, False):
            for x in (True, False):
                for z in (True, False):
                    if not ((w >= y) and y >= x ) or (not z):
                        print(int(x), int(y), int(w), int(z))


if __name__ == '__main__':
    main()
