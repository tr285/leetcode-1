# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, words, master):
        """
        :type words: List[Str]
        :type master: Master
        :rtype: None
        """
        def match(w1, w2):
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        while words:
            groups = collections.defaultdict(int)

            # Count how many words have each match score
            for w1 in words:
                for w2 in words:
                    if w1 != w2:
                        groups[(w1, match(w1, w2))] += 1

            # Choose the word with the smallest worst-case group
            guess = min(
                words,
                key=lambda w: max(groups[(w, k)] for k in range(7))
            )

            x = master.guess(guess)

            if x == 6:
                return

            words = [w for w in words if match(guess, w) == x]