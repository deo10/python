# python
# This task requires you to utilize Copilot to generate Python functions
# for the following scenarios, providing clean and efficient code:

# Calculate the sum of all prime numbers up to a given integer 'n'.
def sum_of_primes(n):
    if n < 2:
        return 0
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sum(i for i, is_prime in enumerate(sieve) if is_prime)

# Convert a string to title case (first letter of each word capitalized),
# taking a 'String input' and returning the modified string.
def convert_to_title_case(input_string):
    # Use str.title() but fix for words with mixed case and preserve non-alpha chars
    def fix_word(word):
        if not word:
            return word
        return word[0].upper() + word[1:].lower()
    return ' '.join(fix_word(w) for w in input_string.split(' '))

# Given an array of strings ["eat","tea","tan","ate","nat","bat"],
# group the anagrams together. Result can be returned in any order,
# as example: [["bat"],["nat","tan"],["ate","eat","tea"]]
def group_anagrams(strs):
    from collections import defaultdict
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

# Example usage:
if __name__ == "__main__":
    example_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(example_data)
    print(result)