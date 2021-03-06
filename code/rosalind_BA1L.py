# Convert a DNA string to a number.

# Given: A DNA string Pattern.

# Return: PatternToNumber(Pattern).
def PatternToNumber(pattern):
	seq = {'A':0, 'C':1, 'G':2, 'T':3}
	k = len(pattern)
	num = 0
	for i in range(k):
		# print pattern[i], k-i-1
		num += seq[pattern[i]] * pow(4, k - i - 1)
	return num

# string = 'AGT'
# print PatternToNumber(string) 