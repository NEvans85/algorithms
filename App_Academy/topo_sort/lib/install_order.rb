# Given an Array of tuples, where tuple[0] represents a package id,
# and tuple[1] represents its dependency, determine the order in which
# the packages should be installed. Only packages that have dependencies
# will be listed, but all packages from 1..max_id exist.

# N.B. this is how `npm` works.

# Import any files you need to
require_relative 'topological_sort'

def install_order(arr)
  vertex_dict = {}
  max_id = arr.max { |tuple| tuple[0] }[0]
  (1..max_id).each do |i|
    vertex_dict[i] = Vertex.new(i)
  end
  arr.each do |tuple|
    Edge.new(vertex_dict[tuple[1]], vertex_dict[tuple[0]])
  end
  sorted_vertices = topological_sort(vertex_dict.values)
  sorted_vertices.map(&:value)
end
