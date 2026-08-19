from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        patterns = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                patterns[word[:i] + "*" + word[i + 1:]].append(word)

        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, steps = q.popleft()

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]

                for nxt in patterns[pattern]:
                    if nxt == endWord:
                        return steps + 1

                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, steps + 1))

                patterns[pattern] = []

        return 0