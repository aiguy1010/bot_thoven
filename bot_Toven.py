import notation
import cheating

def main():
    f = open('jank.txt','r')
    raw = f.read().split()
    rawInput = []
    for i in range(len(raw)):
        rawInput.append(int(raw[i]))
    print(rawInput)
    #notation.notation()
    notation.notation(rawInput)

if __name__ == '__main__':
    main()
