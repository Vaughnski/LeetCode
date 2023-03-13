def strStr(self, haystack: str, needle: str) -> int:
    if haystack == needle: return 0;
    n_lng, h_lng = len(needle), len(haystack)
    for let in range(0, h_lng):
        if haystack[let] == needle[0]:
            if haystack[let:let + n_lng] == needle:
                return let
    return -1