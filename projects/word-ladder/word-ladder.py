'''
Given two words (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Each transformed word must be the same length
Note that begin_word is not a transformed word.
​
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Example:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
'''

from util import Queue
import os

dirname = os.path.dirname(os.path.abspath(__file__))

f = open(dirname + '\\words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neighbors(word):
    '''
    return all words from word_list that are 1 letter different
    change one letter to another letter in the alphabet incrementally
    search the graph for that
    then repeat for each letter in the word
    '''
    neighbors = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(len(word)):
        for letter in alphabet:
            letters = list(word)
            letters[i] = letter
            new_word = ''.join(letters)
            if (new_word != word and new_word in word_set):
                neighbors.append(new_word)
    return neighbors


def find_ladders(start_word, end_word):
    '''
    Do BFS
    Create a queue. Enqueue a path to the starting word
    Create a visited set
    While queue is not empty
        Dequeue the next path
        Grab the last word from the path
        If the word is not visited
            If word equals end_word, return path
            Else, mark word as visited.
            Enqueue a path to each neighbor
    '''
    q = Queue()
    visited = set()
    q.enqueue([start_word])
    while q.size() > 0:
        path = q.dequeue()
        word = path[-1]
        if word not in visited:
            if word == end_word:
                return path
            visited.add(word)
            for neighbor in get_neighbors(word):
                new_path = path.copy()
                new_path.append(neighbor)
                q.enqueue(new_path)

print(find_ladders('hit', 'cog'))
print(find_ladders('happy', 'hungry'))