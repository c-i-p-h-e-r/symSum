Content
-------

SysSum implementation in Python, Using Keccak implementation supporting the FIPS 202 standard instances.

Files :
	- Keccak.py : The Keccak and KeccakError classes - From Keccak Team : keccak.noekeon.org
	  - Modification : Added function to explicitly set number of round and modified output visuatization
	- diff.txt : File diff with original Keccak Implementation
	- libSymSum.py : Supporting functions for SymSum computation - getBaseMsg, genMsg, verifySymSum
	- symSum.py: Python Script to test nature of Output-Sum

Usage : 
	python symSum.py <SHA3-Variant> <#Rounds> <Order of Derivative> <Output Hash-Length (Optional)>

Example:
	python symSum.py 'SHA3_224' 3 5 
	python symSum.py 'SHA3_256' 3 8 
	python symSum.py 'SHA3_384' 4 10 
	python symSum.py 'SHA3_512' 5 20 
	python symSum.py 'SHAKE128' 4 16 2196
	python symSum.py 'SHAKE256' 4 14 96

Note: No sanity check done. Responsibility of User to conform to usage.
      For SHAKE output hash length must be multiple of 8 due to Keccak implementation.
 

Sample Output 1:-------------------------------------------------------------------- 

python symSum.py 'SHA3_224' 4 8 96

 Base Message = b50c169ab50c169a9d2f49ff9d2f49ff6c76a1fc6c76a1fcd1774952d1774952ff87b7c0ff87b7c014529dc014529dc0bfd5ba30bfd5ba304708247c4708247c4c5a35794c5a357951d9efaf51d9efaf364a5bb2364a5bb297acc4a697acc4a62fed3b032fed3b03b5946acbb5946acb02153ec002153ec03529ed463529ed468e7329c08e7329c01de841861de841

 Output-Sum = a60eca6c6ba829c0aac1f2d3fd5777ff3920a5c0e3366accc27a2ccd

 64-prefix = a60eca6c6ba829c0aac1f2d3fd5777ff3920a5c0e3366acc

We have Non-Symmetric Sum! 


Sample Output 2:--------------------------------------------------------------------



python symSum.py 'SHAKE256' 4 16 96

 Base Message = 6b8f30796b8f3079fd8e410bfd8e410b4ba0462d4ba0462d6604d2436604d24354068e3c54068e3c7628befc7628befcba48dc44ba48dc440a675de50a675de512eb538412eb53841d7f2a361d7f2a36a4d2808aa4d2808ae60ea4aae60ea4aadcf40345dcf403453c19ff283c19ff28ff33ce63ff33ce63b1f0cadeb1f0cade5828369f582836

 Output-Sum = 000000000000000000000000

 64-prefix = 0000000000000000

 We have ZeroSum! 


Sample Output 2:--------------------------------------------------------------------


python symSum.py 'SHAKE128' 4 14 96

 Base Message = 5bc4c4285bc4c42819532a6219532a626b2be4a66b2be4a6ef83066cef83066c3d5acdd53d5acdd5cb466b95cb466b95bde7bae3bde7bae347b59eac47b59eac644175be644175be4320d59b4320d59be90ba381e90ba38136665883366658838b7db0ce8b7db0ced4a3a55cd4a3a55c0fb6dce00fb6dce0bf1bdeaabf1bdeaa7f6e733d7f6e733dae933e32ae933e325062717950627179191a162a191a162a98b6cc9f98b6cc

 Output-Sum = 502d0543502d054316a6b2c5

 64-prefix = 502d0543502d0543

We have SymSum! 

