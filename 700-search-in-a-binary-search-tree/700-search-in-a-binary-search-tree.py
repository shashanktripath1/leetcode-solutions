class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root==None:
            return None
        if root.val==val:
            return root
        if val<root.val:
            return self.searchBST(root.left,val)
        return self.searchBST(root.right,val)