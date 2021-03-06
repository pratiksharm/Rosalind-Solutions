# Longest Common Subsequence Problem
# Given: Two strings.
# Return: A longest common subsequence of these strings.

def LongestCommonSubsequence(x, y):
	m = len(x)
	n = len(y)
	lcs_matrix = [[0] * (n + 1) for i in range(m + 1)]
	lcs_str = ''
	if m == 0 or n == 0:
		return lcs_str
	else:
		for i in range(1, m+1):
			for j in range(1, n+1):
				if x[i-1] == y[j-1]:
					lcs_matrix[i][j] = lcs_matrix[i-1][j-1] + 1
								
				else:
					if lcs_matrix[i-1][j] >= lcs_matrix[i][j-1]:
						lcs_matrix[i][j] = lcs_matrix[i-1][j]
					else:
						lcs_matrix[i][j] = lcs_matrix[i][j-1]
	print "the length of the longest common senquence is:", lcs_matrix[m][n]

	t = lcs_matrix[m][n]
	for i in range(m):
		for j in range(n):
			if x[m-i-1] == y[n-j-1] and lcs_matrix[m-i][n-j] == t:
				lcs_str += x[m-i-1]
				t -= 1
				break
				
	print "a longest common senquence is:",len(lcs_str)
	result = ''
	for i in range(len(lcs_str)):
		result += lcs_str[len(lcs_str)-i-1]
	print result

s = 'AACCTTGG'
t = 'ACACTGTGA'
# s1 = 'CTTCATTCCCATTAAGGATAAATACCGAATCGCGAGCCGATATACTGCGGGGGATGGGCGAGGCCAGATATTTCGCGTCTTTGGCAGAGAGTTGACCACTTTATACAGAAGAAATCGGGGAGTTGTTAGTTGTACCCGGTACAGTTTTCTTATGCACGGAGTCTGCCACTGGAGGTAACGAACCAATTACAACGTCTATTTTCAAGGCCTCGCAGTTCGCACGTGTTCAAAGAAAGAGCTATCCAGATATTGTATTGATCGCCCCTCTATTAACAGAGCCGGTGTACCGGATGAGACCGGGACACCGTTATCTCATAACCGTATTGGGATCCTTCCTTCCCATGGTTGTACTTCCAGTCACTAGGTGAAAAGGAATGTTTTTAGCTTCCGGCTAAGTAGCCAGTTGACGAGTTGGTGAATGAAAAAATCTATGCTTGTCGAGAGAGACGAAAGTATAATTATATAGACACAAAACATTAAATCTCGGACACAAGGATGTGACCGGCTGCCTCCTTGTGACGGACAGGCCCACTGGTCCTTGGGAAGGAGGATCCCTGTTTCTAAAGATGAAGTCCTCTGATCTGAGGAGCCCAACTCGCTATGTACTCCCGGACCTGTGAAGTAACTATTTCACGTTACGTTGGTCTACAATGCCTTGGCAGAGGAAGTCATACCATGGCGTGTACACTCTTAACTATCTCATACTGTACCGCACCTTAGCTCCAAATGGTAACATGTGACCAAACTCTCACACGGTTAAAGCACTCCTCATGGCCCGGGATCCTGGTGACCTGTTCAATGATCGCGGATGAATGACGTTTTTGACGAGGTAACGTAATACGATATTCCAAACCTAGATCAAGCCACAAGCCTACTGTTATGTTTCCCATTG'
# t1 = 'TTACACCCGTGTCTCCTCATTCGTACTAGCACGGCGCCAGGGCCTACTACTATTGACGCCCTGGCGGATGGCTCCGGCCCGAACACACCATGAAGACCGCATAAGCGTCCAAGCTGTGTCCTCTTACTCGATAGCCTAAGGCAGGCCGACGCAGTGGAACCGCACAGAAGCCTAATGACAACTTGAAGAAGATCGTAAGCTTCCTGCTCTTGCTCTAACGTGGTTTGAGTTTTGACCCAAAACTTCCCTCTAGGTGCGACTACTGGGTAGTGGCATTACATTTCACTCAGGAAACTCATACATCTGACTGAAGTTGTGGGTTTGCTATACATTACGCTCACGAACACTGTCAGATCGCCACCGAGTTGCGTGAGTGCCTGTTAAACACTCACCTTCCGAACCCTTTCTTCATTAAAGCAAACATAGATTGTCATGAGCACCCTTCAAATCCATAAGCTCCGGGCTACCTCGAACACATGAGTGACGCCAAACGTAAGCTACTCTGGGTTACGCGTACGCAGTGTAGTTGTCGTTGTTCTTTTTTCGTCACCTCAGCATTGCTTCATGCTACGAAAACGTTACCCAGTGTAACTGCCGCAGTTAAACTGACTACACATTGATGTCGCTTGCGATTACTCGACTCACACAGGCGGAACTGGTAGTGACTTGTGATAGACGTTTGAATTGCGACTATTGAGCCATGAGAGCATTTGGTGCGAGCCGCGGACGCATACACGTTTCCGTTGACGTTTTGTCGTAATGTAAGACAACAGTTCATAGGTATACTCTTTTCCAGTACGCTTCCATGAGGCCACGGGATGCGCCCTTTCGTTACGGGTCACGATTGATGAAATAAGTGTATGATCTCGTTTGCCGCGTGATCTTGGCCGTGTTTAATTAGTTGTTATAACTGTTCGTATAGAATGCGCAATTGGCCCACGTGGTGATATATCGAAATACCTTTCAGCAGGGAACGCGGGAGATGG'

# LongestCommonSubsequence(t1, s1)