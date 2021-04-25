import binascii
x = "óÂ§£¾ÞÕríPÇgê"
# x="nguyenvudiemkieu"
j =""
for i in x:
    # de = ord(i)
    # print(de)
    bi = hex(ord(i))[2:]
    if len(bi)==1:
        # print(bi)
        bi='0'+bi

    print(bi)
    # j+=bi
    # if bi <= 'f'
    #     print(bi)
# print(len(j))