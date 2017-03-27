#Coded by : The SymSum Team
#symSum.py : SymSum computation using Keccak class by Keccak Team

import sys
import time
import os
import binascii
import Keccak
import libSymSum

#Processing command-line arguments
sha3Var = sys.argv[1]
print sha3Var
num_of_rounds = int(sys.argv[2])
degree = int(sys.argv[3])

if(sha3Var[:5] == 'SHAKE'):
        hashLenShake = int(sys.argv[4])  # Only for SHA3-XOFs
else:
        hashLenShake = 'undefined'

#SHA3 paramertes as per FIPS 202
sha3Dictionary = {
    'SHAKE128': [1344, 256, 0x1F, hashLenShake],
    'SHAKE256': [1088, 512, 0x1F, hashLenShake],
    'SHA3_224': [1152, 448, 0x06, 224],
    'SHA3_256': [1088, 512, 0x06, 256],
    'SHA3_384': [832, 768, 0x06, 384],
    'SHA3_512': [576, 1024, 0x06, 512],
}

#Get Paramters
rate = sha3Dictionary[sha3Var][0]
capacity = sha3Dictionary[sha3Var][1]
suffix = sha3Dictionary[sha3Var][2]
hashLen = sha3Dictionary[sha3Var][3]

#Get Base Message
[bLen, baseMsg] = libSymSum.getBaseMsg(rate, sha3Var)
print '\n Base Message = ' + baseMsg


#Initialize Keccak Object
myKeccak = Keccak.Keccak()

#Set Number of Rounds
#Introduction of this function is the only modification
#done to original Keccak provided by designers
myKeccak.setNR(num_of_rounds)

#Computing Output-Sum
outputSum = 0
for msgIndex in range(0, (2 ** degree)):
        #Generating individual messages
        msg = libSymSum.genMsg(baseMsg, msgIndex)
        #Computing hash value as per FIPS 202
        digest = myKeccak.Keccak((bLen, msg), rate,
                        capacity, suffix, hashLen, False)

        outputSum = outputSum ^ int(digest, 16)

#Verifying Output-Sum
libSymSum.verifySymSum(outputSum, rate, hashLen)
