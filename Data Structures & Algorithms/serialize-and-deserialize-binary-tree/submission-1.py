# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        traversed = []
        node_to_idx = {}
        self.pre_order_traversal(root, traversed, node_to_idx)
        return ','.join([self.transform_node_to_str(node, node_to_idx) for node in traversed])

    def transform_node_to_str(self, node: TreeNode, mapping: Dict[TreeNode, int]) -> str:
        squished = [str(node.val)]
        if node.left:
            squished.append(str(mapping[node.left]))
        else:
            squished.append('-1')
        if node.right:
            squished.append(str(mapping[node.right]))
        else:
            squished.append('-1')
        return ':'.join(squished)

    def pre_order_traversal(self, root: Optional[TreeNode], result: List[TreeNode], node_to_idx: Dict[TreeNode, int]) -> None:
        if not root:
            return
        idx = len(result)
        result.append(root)
        node_to_idx[root] = idx
        self.pre_order_traversal(root.left, result, node_to_idx)
        self.pre_order_traversal(root.right, result, node_to_idx)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        nodes = data.split(',')
        if len(nodes) == 0:
            return None
        raw_nodes: List[TreeNode] = []
        for node in nodes:
            val, _, _ = node.split(':')
            raw_nodes.append(TreeNode(int(val)))
        print(raw_nodes)
        for i, node in enumerate(nodes):
            _, left_idx, right_idx = node.split(':')
            if left_idx != '-1':
                raw_nodes[i].left = raw_nodes[int(left_idx)]
            if right_idx != '-1':
                raw_nodes[i].right = raw_nodes[int(right_idx)]
        return raw_nodes[0]
