class Solution:
    def customSortString(self, order: str, s: str) -> str:
        chars = [""] * 26
        ordered = {}
        for i in range(len(order)):
            ordered[order[i]] = i
        tail = "" 
        for char in s:
            if char not in ordered:
                tail += char
            else:
                chars[ordered[char]] += char
        return "".join(chars) + tail

        