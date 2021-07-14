#!/usr/bin/env python
# coding: utf-8

# In[26]:
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.value = False
        self.itemset = set()
        self.items = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.items[char] = TrieNode()    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        c_node = self.root
        for ch in word:
            if ch not in c_node.items:
                c_node.insert(ch)
            
            c_node = c_node.items[ch]
        
        c_node.value = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        c_node = self.root

        for ch in prefix:
            if ch not in c_node.items:
                return None
            
            c_node = c_node.items[ch]
        
        return c_node
# In[27]:
class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.value = False
        self.itemset = set()
        self.items = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.items[char] = TrieNode()
                
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        if self.items:
            for ch, node in self.items.items():
                if node.value:
                    n_results.append(suffix + ch)
                node.suffixes(suffix + ch)

        return list(n_results)  
# In[28]:
n_results = list()
custom_Trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    custom_Trie.insert(word)

# In[]:

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    
    if prefix != '':
        prefixNode = custom_Trie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
        
        
interact(f,prefix='')
results=[]
interact(f,prefix='tr')
results=[]
interact(f,prefix='f')
results=[]
interact(f,prefix='ant')
# In[ ]: