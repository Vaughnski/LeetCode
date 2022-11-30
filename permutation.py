res = []
        self.helper(nums, [], res)
        return res
        
    def helper(self,  dec, path, res):
        
        if not dec:
            res.append(path)
            return
            
        for i in range(len(dec)):
            self.helper(dec[:i] + dec[i+1:], path + [dec[i]], res)