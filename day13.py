

def main():
    #filename = '.\\input\day10test.txt'
    filename = '.\\input\day10.txt'

    with open(filename) as f:
        lines = [x.strip() for x in f.readlines() if x.strip() != ""]
        f.close()


if __name__ == "__main__":
    main()