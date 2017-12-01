class KMP:
    @staticmethod
    def prefix_suffix(pattern):
        """
        Calculate prefix_suffix match table: String -> [Int]
        from the pattern
        """
        ret = [0]

        for idx in range(1, len(pattern)):
            jdx = ret[idx - 1]
            while jdx > 0 and pattern[jdx] != pattern[idx]:
                jdx = ret[jdx - 1]
            ret.append(jdx + 1 if pattern[jdx] == pattern[idx] else jdx)
        return ret

    @staticmethod
    def search(string, pattern):
        """
        Knuth-Morris-Pratt Algorithm is algorithm to search a string pattern
        into another given presumably large piece of text.
        """
        prefix_suffix = KMP.prefix_suffix(pattern)
        ret = []
        jdx = 0

        for idx in range(len(string)):
            while jdx > 0 and string[idx] != pattern[jdx]:
                jdx = prefix_suffix[jdx - 1]
            if string[idx] == pattern[jdx]:
                jdx += 1
            if jdx == len(pattern):
                ret.append(idx - (jdx - 1))
                jdx = 0
        return ret
