dict = {}
        for index, value in enumerate(nums):
            if (value in dict):
                del dict[value]
            else:
                dict.update({value: 1})
        return next(iter(dict))