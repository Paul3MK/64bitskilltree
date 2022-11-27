from nltk.tokenize import word_tokenize

lang_count = {
    1: 0,
    2: 0
}

class TrieNode:
    """
    This class is an implementation of a trie. Apparently, it will supercharge information retrieval from job postings.
    The current implementation has PhraseId as a number, but I'm thinking of turning it into dictionary keys, so each index
    corresponds to values.
    """
    # Children = {}
    # PhraseId = -1

    def __init__(self):
        self.Children = {}
        self.PhraseId = -1

    def addPhrase(self, root, phrase, phraseId): # root will have to be a TrieNode
        node = root
        # node.Children = {}
        words = word_tokenize(phrase.lower(), language="english", preserve_line=False) # this change truly fixes issue #1
        
        for i in range(len(words)):
            if words[i] not in node.Children:
                node.Children[words[i]] = TrieNode()
            
            node = node.Children[words[i]]

            if i == (len(words) - 1):
                node.PhraseId = phraseId


    def findPhrases(self, root, textBody, legend):
        node = root
        foundPhrases = []

        words = word_tokenize(textBody.lower(), language="english", preserve_line=False)

        for i in range(len(words)):
            if words[i] in node.Children:
                node = node.Children[words[i]]
                # print(words[i])
                ++i
            else:
                if node.PhraseId != -1:
                    foundPhrases.append(node.PhraseId)
                    legend[node.PhraseId] += 1
                if node == root:
                    ++i
                else:
                    node = root
        if node.PhraseId != -1:
            foundPhrases.append(node.PhraseId)
            legend[node.PhraseId] += 1

        return [foundPhrases, legend]



if __name__ == "__main__": # perhaps write a proper test for this class
    pass