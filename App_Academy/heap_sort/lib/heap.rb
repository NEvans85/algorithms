require 'byebug'

class BinaryMinHeap
  attr_reader :store, :prc

  def initialize(prc = proc { |a, b| a <=> b })
    @store = []
    @prc = prc
  end

  def count
    @store.length
  end

  def extract
    @store[0], @store[-1] = @store[-1], @store[0]
    el = @store.pop
    BinaryMinHeap.heapify_down(@store, 0)
    el
  end

  def peek
    @store[0]
  end

  def push(val)
    @store.push(val)
    BinaryMinHeap.heapify_up(@store, @store.length - 1)
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
    raise "root has no parent" if child_index.zero?
    (child_index - 1) / 2
  end

  def self.heapify_down(array, parent_idx, len = array.length, &prc)
    new_idx = parent_idx
    child_idxs = child_indices(len, new_idx)
    prc = proc { |a, b| a <=> b } if prc.nil?
    until child_idxs.empty? ||
          child_idxs.all? { |child_idx| prc.call(array[new_idx], array[child_idx]) == -1 }
      if child_idxs.length == 1
        array[new_idx], array[child_idxs[0]] =
          array[child_idxs[0]], array[new_idx]
        new_idx = child_idxs[0]
      else
        case prc.call(array[child_idxs[0]], array[child_idxs[1]])
        when -1, 0
          array[new_idx], array[child_idxs[0]] =
            array[child_idxs[0]], array[new_idx]
          new_idx = child_idxs[0]
        when 1
          array[new_idx], array[child_idxs[1]] =
            array[child_idxs[1]], array[new_idx]
          new_idx = child_idxs[1]
        end
      end
      child_idxs = child_indices(len, new_idx)
    end
    array
  end

  def self.heapify_up(array, child_idx, len = array.length, &prc)
    raise "index out of bounds" if child_idx >= len
    new_idx = child_idx
    prc = proc { |a, b| a <=> b } if prc.nil?
    until  new_idx.zero? ||
           prc.call(array[new_idx], array[parent_index(new_idx)]) == 1
      switch_idx = parent_index(new_idx)
      array[new_idx], array[switch_idx] =
        array[switch_idx], array[new_idx]
      new_idx = switch_idx
    end
    array
  end
end
