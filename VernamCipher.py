"""
Created By: Uee
Modified By:
"""

"""
	NB!!!
	The ASCII values between 0-31 are not represented in a readable format. These ASCII values usually are
	displayed by a '' Character.
"""


def VernamCipher(text = "", key = ""):
	"""
	Vernam Cipher Function converts a plain text message to an encrypted message using the XOR Bitwise Function or
	converts an encrypted text message to a plain text message using the XOR Bitwise Function.

	:param text: Plain Text | Encrypted Message
	:param key: Secret Key
	:return: Encrypted | Decrypted Message
	"""

	# Convert Text and Key strings to a list of ASCII Values or Codes.
	KEY_ASCII = list (ord (c) for c in key)
	TEXT_ASCII = list (ord (c) for c in text)

	# Resize the Key ASCII list if the Length of the Text ASCII list is greater.
	if len (text) > len (key):
		ResizeKey (KEY_ASCII, len (text) - len (key))

	# Compute the XOR values using the ASCII values of the Text and Key characters.
	cipherASCII = list (TEXT_ASCII[i] ^ KEY_ASCII[i] for i in range (len (TEXT_ASCII)))

	# Convert the cipher ASCII values to readable characters using the 'chr' function.
	cipherTEXT = "".join (chr (c) for c in cipherASCII)

	# return all the computed values
	return cipherTEXT


def ResizeKey(keyAscii = list (), length = 0):
	"""
	Resize the KEY ASCII List by appending additional elements to it.
	:param keyAscii: List of ASCII Values or Codes made from the Key string.
	:param length: Difference between the Length of the Text and Key strings
	:return: Resized List of KEY ASCII Values or Codes.
	"""
	for i in range (length):
		keyAscii.append (keyAscii[i])
