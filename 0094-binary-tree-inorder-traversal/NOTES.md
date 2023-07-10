tree-problem: Python
```
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
answer, stack = [], []
curr = root
while curr or stack:
while curr:
stack.append(curr)
curr = curr.left
curr = stack.pop()
answer.append(curr.val)
curr = curr.right
return answer
```
```
def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
answer = []
def dfs(node):
if not node:
return
dfs(node.left)
answer.append(node.val)
dfs(node.right)
dfs(root)
return answer
```