n,dict1,ans = len(nums1),{},0
for a in range(n):
    for b in range(n):
        if nums1[a]+nums2[b] not in dict1:
            dict1[nums1[a]+nums2[b]]=1
        else:
            dict1[nums1[a]+nums2[b]]+=1
for a in range(n):
    for b in range(n):
        if 0-(nums3[a]+nums4[b]) in dict1:
            ans+= dict1[0-(nums3[a]+nums4[b])]
