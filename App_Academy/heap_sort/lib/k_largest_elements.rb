require_relative 'heap_sort'


def k_largest_elements(array, k)
  array.heapify!
  result = []
  k.times do
    result << extract(array)
  end
  result
end

def extract(array)
  array[0], array[-1] = array[-1], array[0]
  extracted = array.pop
  BinaryMinHeap.heapify_down(array,0){ |a, b| -1 * (a <=> b) }
  extracted
end
