from typing import Optional
from Python._lib.imports import TreeNode, inOrderTraversal


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        if root.left or root.right:
            root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    print("invert_binary_tree")
    # input case 1
    tree1 = TreeNode(4)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(7)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(3)
    tree1.right.left = TreeNode(6)
    tree1.right.right = TreeNode(9)

    # input case 2
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)

    # expected output 1
    tree3 = TreeNode(4)
    tree3.left = TreeNode(7)
    tree3.right = TreeNode(2)
    tree3.left.left = TreeNode(9)
    tree3.left.right = TreeNode(6)
    tree3.right.left = TreeNode(3)
    tree3.right.right = TreeNode(1)

    # input case 2
    tree4 = TreeNode(2)
    tree4.left = TreeNode(3)
    tree4.right = TreeNode(1)

    input_cases = [tree1, tree2]
    output_cases = [tree3, tree4]
    solution = Solution()
    for test_number, element in enumerate(zip(input_cases, output_cases)):
        input_case, output_case = element
        if inOrderTraversal(solution.invertTree(input_case)) == inOrderTraversal(
            output_case
        ):
            print("\033[92m {}\033[00m".format("."), end=" ")
        else:
            print("\033[91m {}\033[00m".format("F"), end=" ")
    print("\n")
