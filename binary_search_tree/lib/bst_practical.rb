require_relative 'binary_search_tree'

def kth_largest(tree_node, k)
  bst = BinarySearchTree.new
  bst.root = tree_node
  (k- 1).times do
    bst.delete(bst.maximum.value)
  end
  bst.maximum
end
