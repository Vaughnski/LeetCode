c1 = collections.Counter(nums1)
c2 = collections.Counter(nums2)
c3 = c1 & c2
return list(c3.elements())