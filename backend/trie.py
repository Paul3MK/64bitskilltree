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
        words = word_tokenize(phrase, language="english", preserve_line=False)
        
        for i in range(len(words)):
            if words[i] not in node.Children:
                node.Children[words[i]] = TrieNode()
            
            node = node.Children[words[i]]

            if i == (len(words) - 1):
                node.PhraseId = phraseId


    def findPhrases(self, root, textBody):
        node = root;
        foundPhrases = []

        words = textBody.split()

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



if __name__ == "__main__":
    t = TrieNode()

    t.addPhrase(t, "ut", 1)
    t.addPhrase(t, "at", 2)
    t.addPhrase(t, "in", 3)

    # print(t)
    o = t.findPhrases(t, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id feugiat elit. Duis laoreet nisl sed elit placerat maximus. Nulla facilisi. Nam scelerisque vestibulum dolor, tincidunt commodo dolor cursus eu. Ut id ultrices mi. Etiam id sapien ut erat mattis viverra a et sapien. Nulla ante erat, tristique sed cursus a, aliquet eget turpis. Proin nunc sem, fermentum at bibendum non, maximus et justo. Mauris eu gravida arcu, at dignissim quam. Curabitur commodo, nisi vel commodo vestibulum, eros ex facilisis justo, nec placerat est nunc sit amet nisl. Nunc consequat mi non urna interdum pellentesque. Vestibulum eleifend accumsan purus, non consequat libero malesuada ut. Ut mattis arcu sit amet arcu tincidunt, id euismod neque placerat. Fusce interdum dignissim neque in consectetur. Cras tempus gravida pharetra. In gravida, quam eu accumsan iaculis, ante eros rhoncus est, et mollis leo est et augue. Vestibulum vehicula vitae turpis nec pharetra. Aenean maximus felis dolor, pulvinar eleifend turpis aliquet et. Etiam condimentum orci sed ullamcorper volutpat. Mauris viverra at erat finibus tempus. Vivamus tempor nisi dolor, sit amet porta ante bibendum ut. Proin nunc justo, mattis ac erat id, finibus condimentum tortor. Aenean malesuada fringilla nulla, eget viverra urna molestie et. Praesent fringilla, magna eget finibus egestas, ligula diam cursus augue, nec sollicitudin augue nibh sit amet felis. Donec et pellentesque neque, nec posuere orci. Donec sit amet sem sit amet augue gravida viverra. Proin in leo pellentesque, placerat orci eu, blandit risus. Ut sed rhoncus purus. Proin enim enim, fermentum eget velit posuere, aliquet suscipit felis. Pellentesque elementum, justo ut volutpat pharetra, neque lacus sagittis metus, nec imperdiet nisl sem eget purus. Phasellus turpis metus, maximus sit amet eros ut, faucibus mollis felis. Integer ut elit a lorem laoreet faucibus. Cras augue ante, tempor nec porttitor id, scelerisque a leo. Phasellus vitae erat ultricies, consectetur orci non, dignissim orci. Aliquam erat volutpat. Nulla non nisl ac nibh fermentum venenatis id ut ipsum. Mauris feugiat mi a nibh finibus accumsan. Ut nec nunc in nisl mattis iaculis sit amet ut augue. Sed ac hendrerit nulla. Quisque eu neque est. In non bibendum purus, eu dapibus ligula. Nulla vel ex eleifend, tempor libero in, vehicula lacus. Nunc in ex at lacus cursus cursus. Nulla maximus nibh eget justo pretium, nec commodo nibh mattis. Donec ut imperdiet lectus, id suscipit lorem. Phasellus vel dapibus elit, non maximus lorem. Integer a elit in urna ultrices accumsan. Praesent dolor tellus, imperdiet quis velit id, varius elementum nunc. Nulla facilisi. Etiam pulvinar a velit nec bibendum. Nam at est eget neque tristique sollicitudin vel vel nisi. Praesent eget est est. Nullam consequat laoreet tellus vel aliquam. Nunc vehicula suscipit semper. Praesent tincidunt, ipsum et aliquet tristique, diam justo maximus risus, eget rutrum ligula turpis sit amet purus. Mauris gravida, quam vel aliquam gravida, eros nisi pharetra mauris, quis dapibus purus tortor nec neque. Aliquam ut dolor vestibulum, scelerisque libero id, tristique lacus. Maecenas felis justo, lacinia at tellus non, tristique commodo tellus. Maecenas rhoncus scelerisque velit non volutpat. Nam consequat tortor lacus, ac semper mi convallis ac. Aliquam consectetur consectetur pretium. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam erat volutpat. Ut consequat orci ex, in semper erat iaculis in. Fusce eleifend lorem in gravida accumsan. Vestibulum pharetra ligula ante. Fusce vel odio sed nisi euismod mattis. Fusce at sagittis lectus, sed fermentum quam. Integer vehicula tincidunt diam at congue. Fusce orci urna, porttitor quis iaculis eget, efficitur volutpat diam. Aenean gravida pellentesque dapibus. Donec condimentum ante nec nulla volutpat, vel cursus turpis faucibus. Morbi vel pharetra turpis. Nam sit amet leo iaculis, consequat augue molestie, tincidunt metus. Vestibulum arcu libero, tincidunt non pellentesque eu, aliquet at velit. Nam hendrerit orci nec massa lacinia vestibulum. In faucibus lacus vitae auctor maximus. Phasellus quis accumsan leo. In finibus eros at lacinia varius. Curabitur rhoncus commodo laoreet. Pellentesque eu nunc et quam tempor accumsan. Donec vitae dui odio. Quisque sit amet mauris sed arcu aliquam tristique. Vestibulum libero elit, imperdiet eget consequat a, feugiat rutrum urna. Ut ultrices tempus ornare. In hac habitasse platea dictumst. In lobortis accumsan arcu, id eleifend urna. Morbi lorem mi, facilisis eget urna et, commodo maximus felis. Praesent non elit ultrices, malesuada enim vitae, venenatis nibh. In vitae eros nulla. Quisque sit amet ullamcorper sapien, eget mattis libero. Morbi ac massa fermentum, suscipit dui non, vehicula dui. Sed dapibus, odio id laoreet vestibulum, massa neque condimentum velit, sit amet varius sem diam id nulla. Nullam porta, dui ac suscipit eleifend, odio nisi fermentum justo, in pharetra orci velit sed magna. Etiam in consequat metus. Sed commodo ac purus ac tincidunt. Sed ex diam, facilisis at rhoncus vel, volutpat ac odio. Vivamus rutrum sagittis finibus. Cras in aliquam metus. Praesent et velit blandit, tempus lacus et, egestas metus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed egestas felis risus, sed suscipit odio egestas nec. Aliquam ullamcorper efficitur odio ut ultrices. Mauris id velit sed ligula congue rutrum. Donec pulvinar mattis turpis, vel porttitor mi interdum non. Donec interdum neque purus, eget molestie lectus auctor venenatis. Fusce vitae urna at elit convallis cursus sit amet et magna. Nullam eu est ante. Ut et est eu mi fermentum dictum. Sed eget elit at ligula dapibus sollicitudin sed vel augue. Integer varius elit consequat consequat rhoncus. Phasellus volutpat turpis lectus, eget elementum diam mollis sit amet. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nullam vitae leo elementum, viverra neque sit amet, scelerisque mauris. Mauris vel orci non risus blandit rhoncus. In vel ipsum nibh. Nullam sed erat ut diam vehicula vulputate. Sed quis ex ac lorem iaculis varius. Suspendisse potenti. Nulla aliquet semper pulvinar. Duis turpis tellus, bibendum id porttitor at, vehicula ut turpis. Morbi porta, justo sit amet ultrices congue, dui lacus semper velit, a hendrerit ipsum lectus sed nibh. In vulputate orci tortor, in gravida felis varius eget. Fusce eget aliquet lectus. Aenean in nunc purus. Etiam ullamcorper lectus in placerat tincidunt. Aenean cursus, leo sit amet mattis sagittis, ipsum turpis finibus urna, sed placerat lectus ante a felis. Curabitur vitae vehicula dolor. In nulla augue, dictum sed purus vel, placerat scelerisque tellus. Etiam consequat euismod ornare. Aliquam congue ultricies ultrices. Quisque ut nulla tincidunt, suscipit lectus sit amet, fringilla nisl. Vivamus vel interdum nulla, sit amet dignissim mi. Ut a varius ligula. Maecenas ut magna pharetra, vulputate risus vitae, rhoncus quam. Etiam ac ex diam. Cras bibendum pretium dictum. Nam venenatis nunc efficitur eros lacinia, at hendrerit nunc scelerisque. Sed malesuada arcu non metus pellentesque, id venenatis erat rutrum. Etiam sit amet tellus non tellus hendrerit imperdiet eget vel sem. Donec sed iaculis purus. Aliquam sed arcu magna. Nullam sit amet arcu vitae nisl interdum maximus ut vitae neque. Etiam vulputate est enim, sodales suscipit tellus porta non. Nam sit amet ornare tellus, at maximus tellus. Sed at leo risus. In id metus at urna lacinia venenatis. Sed non euismod metus, in ultricies massa. Vestibulum laoreet congue risus, nec volutpat enim dapibus id. Nam eget nulla lectus. Sed bibendum porta mauris. Maecenas bibendum, ex ut euismod condimentum, leo leo maximus diam, non venenatis lorem arcu non arcu. Pellentesque blandit sem in dui commodo, et fringilla magna cursus. In vehicula placerat ullamcorper. Curabitur egestas velit vitae libero dapibus, hendrerit rutrum elit tristique. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec vestibulum nisi eget nulla eleifend malesuada. Nullam non sapien at diam feugiat dapibus. Phasellus non volutpat metus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In ornare accumsan nisl quis finibus. Sed sapien velit, lobortis eleifend tortor sed, ornare faucibus lectus. Sed sed eleifend justo, eget dignissim quam. Vestibulum nec justo sagittis, laoreet est ut, suscipit erat. Donec nisi libero, suscipit tempor mattis non, euismod sit amet dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc convallis, felis nec elementum placerat, tortor enim vulputate velit, interdum pulvinar massa nulla a elit. Maecenas at porta quam, efficitur consequat eros. Maecenas sodales odio eu orci convallis finibus interdum et dolor. Nunc quis hendrerit mi. Ut viverra convallis tellus, ut mattis enim cursus sed. Quisque molestie augue vel augue fermentum, quis condimentum massa ornare. Vivamus aliquet at tortor eleifend vulputate. Nam varius lorem erat, at maximus sapien interdum sed. Nam sem justo, pellentesque sit amet condimentum scelerisque, viverra ut odio. Aenean tincidunt nulla a tortor mollis, eu ullamcorper diam ullamcorper. Vestibulum pharetra accumsan massa ac imperdiet. Praesent aliquet dolor suscipit, malesuada felis venenatis, pharetra dolor. Etiam lobortis orci eu fermentum imperdiet. Sed iaculis sapien in consequat rutrum. Aenean elementum, urna fermentum molestie tempor, urna tortor iaculis nunc, sed porttitor nisi tortor facilisis diam. In et semper odio. Phasellus rhoncus ipsum et sem fringilla posuere. Pellentesque luctus ut ex non porta. Etiam placerat mattis ultrices. Maecenas mollis facilisis justo, vel viverra justo consequat at. Fusce sodales elit eu lacus tempor viverra. Integer eget mi sit amet lectus feugiat tempus eget nec neque.")

    print(o)