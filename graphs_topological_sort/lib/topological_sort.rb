require_relative 'graph'

# Implementing topological sort using both Khan's and Tarian's algorithms

# Tarjan's Algorithm

def topological_sort(vertices)
  visited = vertices.map { |v| [v, false] }.to_h
  result = []
  visited.each do |vertex, status|
    begin
      visit(vertex, visited, result) unless status
    rescue
      result = []
      break
    end
  end
  result
end

def visit(vertex, visited, result, chain = [])
  if chain.include?(vertex)
    raise "Cycle Detected"
  end
  if !visited[vertex]
    children = vertex.out_edges.map(&:to_vertex)
    children.each do |child|
      chain << vertex
      visit(child, visited, result, chain)
    end
    visited[vertex] = true
    chain.delete(vertex)
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
