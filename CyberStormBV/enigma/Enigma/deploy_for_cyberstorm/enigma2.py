# -*- coding: utf-8 -*-
"""
Template for enigma machine challange
See https://py-enigma.readthedocs.io/en/latest/guide.html#building-your-enigma-machine
for more information
"""


from enigma.machine import EnigmaMachine
from sys import stdin, stderr
from itertools import permutations

#All Wehrmacht models
LIST_OF_ROTORS = ['I','II','III']
#Kriegsmarine M3 & M4
#LIST_OF_ROTORS = ['I','II','III', 'IV', 'V', 'VI', 'VII', 'VIII']

RING_SETTINGS = ["F","O","M"]

#X is not in use, to make your life easier
ALPHABET=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']

#there are more reflectors, but this will be bad enough for you to deal with.
LIST_OF_REFLECTORS = ['B', 'C']

message = stdin.read().rstrip("\n")

for i in list(permutations(LIST_OF_REFLECTORS)):
    reflector = i[0]
    for j in list(permutations(LIST_OF_ROTORS)):
        rotor = " ".join(j)
        for k in list(permutations(RING_SETTINGS)):
            ring_settings = " ".join(k)
            print("{} {} {}".format(reflector, rotor, ring_settings))
    
            #This is one way to create an enigma machine, there are others ;)
            machine = EnigmaMachine.from_key_sheet(
                rotors=rotor,
                reflector=reflector,
                ring_settings=ring_settings,
                plugboard_settings='QZ WG EC RV TB YN UM IK OL PA')
                
            decrypted_message = machine.process_text(message)
            decrypted_message = decrypted_message.split("X")
            decrypted_message = " ".join(decrypted_message)
            print(decrypted_message)