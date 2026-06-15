class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length  = int(s[i:j])
            start = j + 1
            end = start + length
            strings.append(s[start:end])
            i = end
        return strings
