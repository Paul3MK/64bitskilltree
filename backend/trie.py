from nltk.tokenize import word_tokenize

class TrieNode:
    """
    This class is an implementation of a trie. Apparently, it will supercharge information retrieval from job postings.
    The current implementation has PhraseId as a number, but I'm thinking of turning it into dictionary keys, so each index
    corresponds to values.
    """
    Children = {}
    PhraseId = -1

    def __init__(self):
        self.Children = TrieNode.Children
        self.PhraseId = TrieNode.PhraseId

    def addPhrase(self, root, phrase, phraseId): # root will have to be a TrieNode
        node = root
        words = word_tokenize(phrase, language="english", preserve_line=False) # this change truly fixes issue #1
        
        for i in range(len(words)):
            if words[i] not in node.Children:
                node.Children[words[i]] = TrieNode()
            
            node = node.Children[words[i]]

            if i == (len(words) - 1):
                node.PhraseId = phraseId


    def findPhrases(self, root, textBody):
        node = root;
        foundPhrases = []

        words = word_tokenize(textBody, language="english", preserve_line=False)

        for i in range(len(words)):
            if words[i] in node.Children:
                node = node.Children[words[i]]
                print(words[i])
                ++i
            else:
                if node.PhraseId != -1:
                    foundPhrases.append(node.PhraseId)
                if node == root:
                    ++i
                else:
                    node = root
        if node.PhraseId != -1:
            foundPhrases.append(node.PhraseId)

        return foundPhrases



if __name__ == "__main__": # perhaps write a proper test for this class
    pass