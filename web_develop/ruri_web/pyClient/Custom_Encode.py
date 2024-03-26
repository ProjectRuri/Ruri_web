def c_Encode(address, s):
    byte_s = s.encode('utf-8')
    with open(address, 'r') as original:
        with open(address+".cry", 'w+') as encode_file:
            n = 0
            for line in original:
                temp_line = bytearray(line, 'utf-8')
                for i in range(len(temp_line)):
                    temp_line[i] ^= byte_s[n]
                    n += 1
                    if n >= len(byte_s):
                        n = 0
                encode_file.write(temp_line.decode('utf-8'))


            