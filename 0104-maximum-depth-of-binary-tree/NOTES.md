tree-problem: Python
```
def maxDepth(self, root: Optional[TreeNode]) -> int:
if not root:
return 0
left_depth = 1 + self.maxDepth(root.left)
right_depth = 1 + self.maxDepth(root.right)
return max(left_depth, right_depth)
```
​
```
def maxDepth(self, root: Optional[TreeNode]) -> int:
if not root:
return 0
level = 0
q = deque([root])
while q:
for _ in range(len(q)):
node = q.popleft()
if node.left:
q.append(node.left)
if node.right:
q.append(node.right)
level += 1
return level
```