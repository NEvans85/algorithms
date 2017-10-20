# There are many ways to implement these methods, feel free to add arguments
# to methods as you see fit, or to create helper methods.
require_relative 'bst_node'
require 'byebug'
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
  end

  # helper method for #delete:
  def maximum(tree_node = @root)
  end

  def depth(tree_node = @root)
  end

  def is_balanced?(tree_node = @root)
  end

  def in_order_traversal(tree_node = @root, arr = [])
  end


  private
  # optional helper methods go here:
  def append(value, tree_node)
    if value > tree_node.value
      if tree_node.right.nil?
        tree_node.right = BSTNode.new(value)
      else
        append(value, tree_node.right)
      end
    else
      if tree_node.left.nil?
        tree_node.left = BSTNode.new(value)
      else
        append(value, tree_node.left)
      end
    end
  end
end
