# Problem Set 4A
# Name: David Fox

def insert_in_string(string, letter, pos):
    return string[:pos] + letter + string[pos:]

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]
    else:
        sub_perm_list = get_permutations(sequence[1:len(sequence)])
        perm_list = []

        for i in sub_perm_list:
            for j in range(len(i)+1):
                perm_list.append(insert_in_string(i, sequence[0],j))
    return perm_list

if __name__ == '__main__':
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    



