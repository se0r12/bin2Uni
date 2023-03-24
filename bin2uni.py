import sys

def bytes2Uni(byte):
    print(byte.decode("utf-8"))


def int2Bytes(integer):

    length = len(bin(integer)[2::])

    byte = int.to_bytes(integer, length // 8, "big")
    bytes2Uni(byte)

def main():
    string = sys.argv[1]
    base = sys.argv[2]

    match base:
        case "2":
            integer = int(string, 2)
            int2Bytes(integer)

        case "16":
            integer = int(string, 16)
            int2Bytes(integer)

        case _:
            quit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("python3 bin2uni.py binary base")
        quit(1)

    main()
