class BinaryMinHeap
  attr_reader :store, :prc

  def initialize(&prc)
    @store = []
  end

  def count
  end

  def extract
  end

  def peek
  end

  def push(val)
  end

  public
  def self.child_indices(len, parent_index)
    children = []
    [1, 2].each do |i|
      child = parent_index * 2 + i
      children << child if child < len
    end
    children
  end

  def self.parent_index(child_index)
    (child_index - 1) / 2
  end

  def self.heapify_down(array, parent_idx, len = array.length, &prc)
    
  end

  def self.heapify_up(array, child_idx, len = array.length, &prc)
  end
end
