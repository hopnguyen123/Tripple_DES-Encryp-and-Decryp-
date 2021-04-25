import Encryption as E
import decryption as D
# plaintext: nguyenvudiemkieu
# key1      : 0123456789ABCDEF
# key2      : 1357908642ACEBDF
# key3      : FEBACD1230984675
# print("Nhap PLAINTEXT: ",end =' ')
plaintext = "CONG_NGHE_THONG_TIN__UIT"
# print("Nhap KEY1: ",end = ' ')
KEY1 = "123456789ABCDEF0"
# print("Nhap KEY2: ",end =' ')
KEY2 = "123456789ABCDEFF"
# print("NHAP KEY3: ",end =' ')
KEY3 = "FEBACD1230984675"

#Mã hoá
print(" --------    MÃ HOÁ      --------")
print("PLAINTEXT: ",plaintext)
A = E.ENCRYPTION(KEY1,plaintext)
print("A: ",A)
# print(type(X_1))
B = D.DECRYPTION(KEY2,A)
print("B: ",end=' ')
print(B)
# print(type(X_2))
CIPHER_TEXT = E.ENCRYPTION(KEY3,B)
print("Cipher_text: ",CIPHER_TEXT)

# Giải mã
print("")
print(" ---------   GIẢI MÃ     ---------  ")
print(CIPHER_TEXT)
# cipher ="00110110111100111001100111100010001101111111011001111101001001001111100101110000000000011000111001101100001010101110110100010110"
# print("Nhap KEY1: ",end = ' ')
# KEY1 = "123456789ABCDEF0"
# print("Nhap KEY2: ",end =' ')
# KEY2 = "123456789ABCDEF0"
# print("NHAP KEY3: ",end =' ')
# KEY3 = "FEBACD1230984675"

# print(plaintext)
# print(KEY1)
# print(KEY2)
# print(KEY3)

B = D.DECRYPTION(KEY3,CIPHER_TEXT)
print("B: ",end=' ')
print(B)
# print(type(X_1))
A = E.ENCRYPTION(KEY2,B)
print("A: ",A)
# print(type(X_2))
plaint = D.DECRYPTION(KEY1,A)
print("PLAIN_TEXT: ",plaint)