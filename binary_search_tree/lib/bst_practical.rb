require_relative 'binary_search_tree'

def kth_largest(tree_node, k)
  bst = BinarySearchTree.new
  bst.root = tree_node
  node_count = 0
  if tree_node.right
    node_count = tree_node.right.descendents.count
    return kth_largest(tree_node.right, k) if node_count >= k
    node_count += 1
    return tree_node.right if node_count == k
  end
  node_count += 1
  return tree_node if node_count == k
  kth_largest(tree_node.left, k - node_count)
end

# The following approach destroys the tree as it searches.
# This is less than ideal.
# def kth_largest(tree_node, k)
#   bst = BinarySearchTree.new
#   bst.root = tree_node
#   (k- 1).times do
#     bst.delete(bst.maximum.value)
#   end
#   bst.maximum
# end
