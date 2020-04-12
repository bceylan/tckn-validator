import sys

def tcknValidator(tckn):
    if len(tckn) != 11:
        return None

    odds = list()
    evens = list()

    for i in range(0, 5):
        odds.append(tckn[2*i])
        if i == 4:
            pass
        else:
            evens.append(tckn[2*i + 1])

    tenthDigit = (sum(odds) * 7 - sum(evens)) % 10
    eleventhDigit = (sum(odds) + sum(evens) + tckn[9]) % 10

    return ((tenthDigit == tckn[9]) and (eleventhDigit == tckn[10]))

        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        given_tckn = sys.argv[1]
    else:
        print('Usage: python3 tcknValidator.py <TCKN>')
        sys.exit(2)
    
    tckn = list()

    for i in range(len(given_tckn)):
        tckn.append(int(given_tckn[i]))

    if tcknValidator(tckn):
        print('TCKN valid.')
        sys.exit(0)
    else:
        print('TCKN invalid.')
        sys.exit(1)