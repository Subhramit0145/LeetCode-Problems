from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        words = set(wordList)
        words.discard(beginWord)
        level = {beginWord}
        parents = defaultdict(list)
        found = False

        while level and not found:
            next_level = set()

            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == word[i]:
                            continue

                        nxt = word[:i] + c + word[i + 1:]

                        if nxt in words:
                            next_level.add(nxt)
                            parents[nxt].append(word)

                            if nxt == endWord:
                                found = True

            words -= next_level
            level = next_level

        if not found:
            return []

        ans = []

        def backtrack(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                backtrack(parent, path + [parent])

        backtrack(endWord, [endWord])
        return ans