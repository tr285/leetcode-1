class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0

        while i < len(words):
            line = []
            letters = 0

            while i < len(words) and letters + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                letters += len(words[i])
                i += 1

            spaces = maxWidth - letters
            gaps = len(line) - 1

            if i == len(words) or gaps == 0:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                res.append(s)
            else:
                even = spaces // gaps
                extra = spaces % gaps

                s = ""
                for j in range(gaps):
                    s += line[j]
                    s += " " * (even + (1 if j < extra else 0))

                s += line[-1]
                res.append(s)

        return res