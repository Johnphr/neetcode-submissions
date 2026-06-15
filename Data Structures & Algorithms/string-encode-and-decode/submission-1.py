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
            length = int(s[i:j])
            strings.append(s[j+1:j+length+1])
            i = j+length+1
        return strings