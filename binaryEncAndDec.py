import sys

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def main(argv):
    try:
        if sys.argv[1] == '-h' :
            print ('Usage : python3 binaryEncAndDec encode')
            print ('           will convert text to binary\n')
            print ('Usage : python3 binaryEncAndDec decode')
            print ('           will convert binary to text')

        if sys.argv[1] == 'encode' :
            print('print your text : ')
            user_txt_input = input()
            print('\n')
            print(text_to_bits(user_txt_input))

        if sys.argv[1] == 'decode' :
            print('print your binary number :')
            user_txt_input = input()
            print('\n')
            print(text_from_bits(user_txt_input))

    except Exception:

        print ('Usage : python3 binaryEncAndDec encode')
        print ('           will convert text to binary\n')
        print ('Usage : python3 binaryEncAndDec decode')
        print ('           will convert binary to text')
    


if __name__ == "__main__":
    main(sys.argv[1:])
