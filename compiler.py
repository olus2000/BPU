### Errors ###
class CompilerError(Exception):
    '''Base class for exceptions in compilers'''
    pass

class ProgramTooBigError(CompilerError):
    '''When a compiled program would be bigger than 256 bytes'''
    pass


### Compilers ###

commands = {'+': 0, '-': 1, '>': 2, '<': 3, '[': 4, ']': 5, ',': 6, '.': 7}
def bytes_compiler(s):
    out = b''
    i = 0
    c = -1
    n = -1
    while i < len(s):
        if s[i] in '0123456789':
            n = max(0, n)
            n = n * 10 + int(s[i])
        else:
            if c >= 6:
                out += bytes(((n * 8 + c) % 256,))
            elif c >= 0:
                n = max(n, 1)
                out += bytes(((n * 8 - 8 + c) % 256,))
            elif n >= 0:
                out += bytes((n % 256,))
            if s[i] in '+-><[],.':
                n = 0
                c = commands[s[i]]
            else:
                n = -1
                c = -1
        i += 1
    if c >= 6:
        out += bytes(((n * 8 + c) % 256,))
    elif c >= 0:
        out += bytes(((n * 8 - 8 + c) % 256,))
    elif n >= 0:
        out += bytes((n % 256,))
    if len(out) > 256:
        raise ProgramTooBigError('Program exceeded 256 bytes')
    while len(out) < 256:
        out += b'\x00'
    return out

def logisim_compiler(b):
    out = 'v2.0 raw\n'
    x = b[0]
    n = 0
    for c in b:
        if c == x:
            n += 1
        else:
            if n > 1:
                out += str(n) + '*'
            out += hex(x)[2:] + ' '
            x = c
            n = 1
    if x > 0:
        if n > 1:
            out += str(n) + '*'
        out += hex(x)[2:] + ' '
    return out


### Interface ###

def interface():
    print('Brainfuck Assembly Language interactive compiler\n'
          '               v.1.0 by olus2000')
    while True:
        success = False
        while not success:
            print()
            source = input('Insert input file name: ')

            print('Reading...')
            try:
                with open(source, 'r') as f:
                    source = f.read()
            except Exception as e:
                print('Unexpected error while reading:')
                print(e)
                continue

            print('Compiling...')
            try:
                binary = bytes_compiler(source)
            except CompilerError as e:
                print('Compiler stopped with the following error message:')
                print(e.message)
                continue
            except Exception as e:
                print('Unexpected error while compiling:')
                print(e)
                continue
            success = True

        print('Compilation complete.\n'
              'Select action:\n'
              '1. Save as a binary file\n'
              '2. Convert to a Logisim ROM dump')
        action = input('>>> ')
        while action not in '12':
            print('Please choose 1 or 2')
            action = input('>>> ')

        success = False
        while not success:
            print()
            dest = input('Insert output file name: ')

            if action == '2':
                print('Converting...')
                try:
                    dump = logisim_compiler(binary)
                except CompilerError as e:
                    print('Converter stopped with the following error message:')
                    print(e.message)
                    continue
                except Exception as e:
                    print('Unexpected error while converting:')
                    print(e)
                    continue

            print('Saving...')
            try:
                if action == '1':
                    with open(dest, 'wb') as f:
                        f.write(binary)
                else:
                    with open(dest, 'w') as f:
                        f.write(dump)
            except Exception as e:
                print('Unexpected error while saving:')
                print(e)
                continue

            success = True


### main ###

if __name__ == '__main__':
    interface()
