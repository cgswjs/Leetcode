# def findMedianSortedArrays(nums1 , nums2):
# 	temp = sorted(nums1+nums2)
# 	if len(temp)%2:
# 		med = temp[len(temp)//2]
# 	else:
# 		med = (temp[len(temp)//2-1]+temp[len(temp)//2])/2

# 	return med

nums1 = [1,3,4,6,8]
nums2 = [2,7,9,10]





med= findMedianSortedArrays(nums1,nums2)

print(med)