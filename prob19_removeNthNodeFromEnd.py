class Solution:
	def removeNthFromEnd64(self,head,n):
		def index(node):
			if not node:
				return 0
			i = index(node.next)+1
			if i>n:
				node.next.val = node.val
			return i
		index(head)
		return head.next

	def removeNthFromEnd56(self,head,n):
		def remove(head):
			if not head:
				return 0,head
			i,head.next = remove(head.next)
			return i+1,(head,head.next)[i+1==n]
		return remove(head)[1]


	#fast pointer is always n spaces ahead of slow pointer
	def removeNthFromEnd48(self,head,n):
		fast=slow=head
		for _ in range(n):
			fast = fast.next
		if not fast:
			return head.next
		while fast.next:
			fast=fast.next
			slow=slow.next
		slow.next=slow.next.next
		return head