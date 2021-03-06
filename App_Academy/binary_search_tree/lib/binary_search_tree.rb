# There are many ways to implement these methods, feel free to add arguments
# to methods as you see fit, or to create helper methods.
require_relative 'bst_node'

class BinarySearchTree
  attr_accessor :root

  def initialize
    @root = nil
  end

  def insert(value)
    if @root.nil?
      @root = BSTNode.new(value)
    else
      append(value, @root)
    end
  end

  def find(value, tree_node = @root)
    return nil if tree_node.nil?
    case tree_node.value <=> value
    when 0
      tree_node
    when 1
      find(value, tree_node.left)
    when -1
      find(value, tree_node.right)
    end
  end

  def delete(value)
    d_node = find(value)
    return nil if d_node.nil?
    case d_node.children.count
    when 0
      remove_childless_node(d_node)
    when 1
      remove_one_child_node(d_node)
    when 2
      remove_two_child_node(d_node)
    end
  end

  # helper method for #delete:
  def maximum(tree_node = @root)
    return tree_node if tree_node.right.nil?
    maximum(tree_node.right)
  end

  def depth(tree_node = @root)
    return 0 if tree_node.children.empty?
    branch_depths = tree_node.children.map { |child| 1 + depth(child) }
    branch_depths.max
  end

  def is_balanced?(tree_node = @root)
    children = tree_node.children
    return true if children.empty?
    return depth(children[0]).zero? if children.length == 1
    return false if (depth(children[0]) - depth(children[1])).abs > 1
    is_balanced?(tree_node.left) && is_balanced?(tree_node.right)
  end

  def in_order_traversal(tree_node = @root, arr = [])
    if tree_node.children.empty?
      arr << tree_node.value
      return arr
    end
    in_order_traversal(tree_node.left, arr) if tree_node.left
    arr << tree_node.value
    in_order_traversal(tree_node.right, arr) if tree_node.right
  end

  def in_order_traversal_iter(tree_node = @root)
    # 1. initialize an empty stack
    # 2. init curr_node as root
    # 3. push curr_node onto the stack
    #    then set curr_node to Curr_node.left until curr_node == nil
    # 4. if curr_node is nil and stack is not empty
      # a. pop from stack
      # b. set curr_node to popped.right
      # c. go back to 3
    # 5. if curr_node == nil, empty the stack
  end


  private
  # optional helper methods go here:
  def append(value, tree_node)
    if value > tree_node.value
      if tree_node.right.nil?
        tree_node.right = BSTNode.new(value, tree_node)
      else
        append(value, tree_node.right)
      end
    else
      if tree_node.left.nil?
        tree_node.left = BSTNode.new(value, tree_node)
      else
        append(value, tree_node.left)
      end
    end
  end

  def remove_childless_node(node)
    if node == @root
      @root = nil
    else
      parent = node.parent
      if parent.value < node.value
        parent.right = nil
      else
        parent.left = nil
      end
    end
  end

  def remove_one_child_node(node)
    parent = node.parent
    if parent.nil?
      @root = node.children[0]
    elsif parent.left == node
      parent.left = node.children[0]
    else
      parent.right = node.children[0]
    end
    node.children[0].parent = parent
  end

  def remove_two_child_node(node)
    replacement = maximum(node.left)
    children = node.children
    parent = node.parent
    rep_parent = replacement.parent
    rep_descendents = replacement.descendents
    if rep_parent == node
      node.left = nil
    else
      rep_parent.right = nil
    end
    if parent.nil?
      @root = replacement
    elsif parent.children.find_index(node).zero?
      parent.left = replacement
    else
      parent.right = replacement
    end
    replacement.parent = parent
    replacement.left, replacement.right = children
    rep_descendents.each { |descendent| insert(descendent.value) }
  end
end
