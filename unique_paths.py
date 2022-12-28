@lru_cache(maxsize=None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m ==1 and n ==1:
            return 1
        if (m ==1 and n ==2 or m ==2 and n ==1):
            return 1
        out =0 
        if m > 1:
            out+=self.uniquePaths(m-1, n)
        if n > 1:
            out+=self.uniquePaths(m, n-1)
        return out