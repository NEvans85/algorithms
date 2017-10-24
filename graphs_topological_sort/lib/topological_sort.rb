require_relative 'graph'
require 'byebug'

# Implementing topological sort using both Khan's and Tarian's algorithms

# Tarjan's Algorithm

def topological_sort(vertices)
  visited = vertices.map { |v| [v, false] }.to_h
  result = []
  debugger
  visited.each do |vertex, status|
    visit(vertex, visited, result) unless status
  end
  result
end

def visit(vertex, visited, result)
  unless visited[vertex]
    children = vertex.out_edges.map(&:to_vertex)
    children.each do |child|
      visit(child, visited, result)
    end
    visited[vertex] = true
    result.unshift(vertex)
  end
end

# Kahn's Algorithm

# def topological_sort(vertices)
#   queue = vertices.select { |vertex| vertex.in_degree.zero? }
#   sorted = []
#   until queue.empty?
#     curr_vertex = queue.shift
#     curr_vertex.out_edges.each do |edge|
#       edge.to_vertex.in_degree -= 1
#       queue << edge.to_vertex if edge.to_vertex.in_degree.zero?
#     end
#     sorted << curr_vertex
#   end
#   vertices.each { |vertex| vertex.in_degree = vertex.in_edges.count }
#   sorted.length == vertices.length ? sorted : []
# end
