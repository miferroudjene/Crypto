##################################challenge 1####################################
##Convert hex to base64##
# Rules:
# 1-Always operate on raw bytes
# 2-never on encoded strings
# 3-Only use hex and base64 for pretty-printing

base64Dictionary = {
    "000000": "A",           "010001": "R",       "100010": "i",           "110011": "z",
    "000001": "B",           "010010": "S",       "100011": "j",           "110100": "0",
    "000010": "C",           "010011": "T",       "100100": "k",           "110101": "1",
    "000011": "D",           "010100": "U",       "100101": "l",           "110110": "2",
    "000100": "E",           "010101": "V",       "100110": "m",           "110111": "3",
    "000101": "F",           "010110": "W",       "100111": "n",           "111000": "4",
    "000110": "G",           "010111": "X",       "101000": "o",           "111001": "5",
    "000111": "H",           "011000": "Y",       "101001": "p",           "111010": "6",
    "001000": "I",           "011001": "Z",       "101010": "q",           "111011": "7",
    "001001": "J",           "011010": "a",       "101011": "r",           "111100": "8",
    "001010": "K",           "011011": "b",       "101100": "s",           "111101": "9",
    "001011": "L",           "011100": "c",       "101101": "t",           "111110": "+",
    "001100": "M",           "011101": "d",       "101110": "u",           "111111": "/",
    "001101": "N",           "011110": "e",       "101111": "v",
    "001110": "O",           "011111": "f",       "110000": "w",
    "001111": "P",           "100000": "g",       "110001": "x",
    "010000": "Q",           "100001": "h",       "110010": "y"
    # (complément) =
}
hexDictonary = {
    "0": "0000", "4": "0100", "8": "1000", "c": "1100",
    "1": "0001", "5": "0101", "9": "1001", "d": "1101",
    "2": "0010", "6": "0110", "a": "1010", "e": "1110",
    "3": "0011", "7": "0111", "b": "1011", "f": "1111"
}


def hexToBase64(string):
    """Convert hex to base64"""
    b64 = ""
    out = ""
    i = 0
    while 3 <= len(string[i:i+3]):
        b64 = F"{hexDictonary[string[i]]}{hexDictonary[string[i+1]]}{hexDictonary[string[i+2]]}"
        j = 0
        while j < len(b64):
            out = F"{out}{base64Dictionary[b64[j:j+6]]}"
            j += 6
        i += 3
    if len(string[i:i+3]) == 1:
        b64 = F"{hexDictonary[string[i]]}00"
        out = F"{out}{base64Dictionary[b64[j:j+6]]}=="

    if len(string[i:i+3]) == 2:
        b64 = F"{hexDictonary[string[i]]}{hexDictonary[string[i+1]]}0000"
        while j < len(b64):
            out = F"{out}{base64Dictionary[b64[j:j+6]]}"
            j += 6
        out = F"{out}="
    return(out)


def FixedXor(buff, xorBuff):
    if len(buff) == len(xorBuff):
        return (hex(int(buff, 16) ^ int(xorBuff, 16)))
    return(-1)
