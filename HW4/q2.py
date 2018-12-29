#------QUESTION 2-------
# Return if a given key is in list of pairs.
# Pre: List constructed with sublists of size 2
#	   which first element is a key and second element is a value.
# 	   And a key in type of string.
# Post: No side effects.
# Return: True if value exists for a key, false otherwise.
def isToken (mapOfTokens, value) :
	for x in mapOfTokens :
		temp = stringToList(x[1])
		if temp == value :
			return True
	return False

# Converts a string literal to list of chars
# Pre: None
# Post: No side effects
def stringToList(string) : 
	chars = []
	for c in string :
		chars.append(c.lower())
	return chars

# Wrapper function for pattern validation
# Checks if the given string is constructed by the provided pattern
def isPatternValid(pattern, string) :
	token = []
	stringAsChars = stringToList(string)
	stringAsChars.reverse()
	return validation(pattern, stringAsChars, token)

# This function should be called via the wrapper, do not call this on its own
# Pre: A dictionary of posible tokens 
# 	   A string construtcted as list of characters
#	   An empty list for temporary tokens 
# Post: Provided list of characters will be deleted
def validation(pattern, string, token) :
	if len(string) == 0 and len(token) > 0 and isToken(pattern,token):
		return True

	if isToken(pattern, token) and len(string) >= 1 :
		token = []
		return validation(pattern, string, token)

	if len(string) >= 1:
		token.append(string.pop())
		return validation(pattern, string, token)

	else :
		return False


#Driver code for Q2
def main () : 
	string = "itwasthebestoftimesitwastheworstoftimesitwastheageofwisdom"
	pattern = [
				["1", "it"], 
			   	["2", "was"],
			   	["3", "the"],
			   	["4", "best"],
			   	["5", "times"],
			 	["6", "worst"],
			 	["7", "age"],
			 	["8", "wisdom"],
			 	["9", "foolishness"],
			 	["10", "epoch"],
			 	["11", "age"],
			 	["12", "of"],
			 	["13", "darkness"],
			 	["14", "before"],
			 	["15", "despair"],
			 	["16", "heaven"],
			 	["17", "nothing"]
			  ]
	print isPatternValid(pattern, string)

main()	
