def count_vowels(word):
	count = 0
	vowel = ['a', 'e', 'i', 'o' , 'u']
	
	for letter in word:
		if letter in vowel:
			count += 1
	return count

count_vowels('aeiouoiuesa')
