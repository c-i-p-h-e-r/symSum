#Coded by : The SymSum Team
#libSymSum.py : Supporting functions for SymSum

import os
import binascii


#Generates the base message
def getBaseMsg(rate, sha3):

        sLen = rate - 8
        freeSymLanes = (rate / 64) - 1

        #last lane manipulation to handle suffix + padding
        rnd = binascii.b2a_hex(os.urandom(3))
        if(sha3[:4] == 'SHA3'):
                suffix = rnd + '86' + rnd
        else:
                suffix = rnd + '9f' + rnd

        #prefix generation
        s = ""
        for subStrCnt in range(0, freeSymLanes):
                subStr = binascii.b2a_hex(os.urandom(4))
                subStr = subStr * 2
                s = s + subStr

        s = s + suffix
        return [sLen, s]

#Generates individual messages from base message
def genMsg(baseMsg, msgIndex):

	#------------Variable Bits Selection-----------#
	#Index of substring inside base message #Don't use last substring
	subStrPosition = 6
	#Actual position inside base message
	offset = 16 * subStrPosition

	#Maximum Nuber of bits to be changed <= order of derivative
	#In this version of the code this is fixed to 24. Do Not Change
	numBits = 24
	#Preparing formatting for variable bits
	fmtNum = '0' + str(numBits/4) + 'x'

        m = baseMsg

	#The value to assigned to the variable bits
        numHexStr = format(msgIndex, fmtNum)

	#Finally generated message
        m = m[:offset + 2] + numHexStr + m[offset + 8:offset + 2 + 8] + numHexStr + m[offset + 8 + 8:]

	return m


#Verifies property exhibited by Output-Sum
def verifySymSum(outputSum, rate, hashLen):

	#Output Formatting
	fmtStr = '0' + str(hashLen/4) + 'x'
	hexstring = format(outputSum, fmtStr)
	print '\n Output-Sum = ' + hexstring

	#For XOFs, truncation to r if h > r
	if(hashLen > rate):
		hexstring = hexstring[:rate / 4]
		hashLen = rate

	#Getting 64-prefix of Output-Sum
	betaPrefixLen = (len(hexstring)//16) * 16
	hexstring = hexstring[:betaPrefixLen]
	print '\n 64-prefix = ' + hexstring
	
	#First Check For Vectorial ZeroSum
	zeroSum = 0
	for c in hexstring:
		zeroSum = zeroSum + int(c, 16)
	if(zeroSum == 0):
		print '\n We have ZeroSum! \n'
		return

	#Next Check For SymSum
	hexlist = [hexstring[i:i + 8] for i in range(0, len(hexstring), 8)]
	it = iter(hexlist)

	sumSym = 0
	for i in it:
        	nxt = next(it, "End")
	        symSum = int(i, 16) ^ int(nxt, 16)
        	sumSym = sumSym + bin(symSum).count("1")
	        #print (i, nxt, format(symSum, '08x'))

	if(symSum == 0):
		print '\nWe have SymSum! \n'
	else:
		print '\nWe have Non-Symmetric Sum! \n'
