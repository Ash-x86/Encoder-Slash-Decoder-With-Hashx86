import code
import Encoder as E

print("This is a Encoder/Decoder to a Hashing Algorithm like base64 by Ash_x86")
string = input("> ")
cc = "";
for i in range(len(string)):
    c = str(string[i:len(string)])
    cc = cc+str(E.Code(c))
print(cc)