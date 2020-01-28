class Solution:
	#normal iteratively method
	def mergeTwoListsIterate(self,l1,l2):
		if l1 is None:return l2
		if l2 is None:return l1
		
		dummy=cur=ListNode(0)
		while l1 and l2:
			if l1.val<l2.val:
				cur.next=l1
				l1=l1.next
			else:
				cur.next=l2
				l2=l2.next
			cur=cur.next

		#if l1 and l2 both empty cur.next is None
		cur.next=l1 or l2
		return dummy.next

	#recursively method
	def mergeTwoListsRecurs(self,l1,l2):
		if not l1 or not l2:
			return l1 or l2
		if l1.val<l2.val:
			l1.next = self.mergeTwoListsRecurs(l1.next,l2)
			return l1
		else:
			l2.next=self.mergeTwoListsRecurs(l1,l2.next)
			return l2

