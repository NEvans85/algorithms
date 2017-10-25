class Vertex
  attr_accessor :in_edges, :out_edges, :value, :in_degree
  def initialize(value)
    @value = value
    @in_edges = []
    @out_edges = []
    @in_degree = 0
  end

  def inspect
    "Value: #{@value}, in_degree #{@in_degree}"
  end
end

class Edge

  attr_accessor :from_vertex, :to_vertex, :cost
  def initialize(from_vertex, to_vertex, cost = 1)
    @from_vertex = from_vertex
    @from_vertex.out_edges << self
    @to_vertex = to_vertex
    @to_vertex.in_edges << self
    @to_vertex.in_degree += 1
    @cost = cost
  end

  def destroy!
    @from_vertex.out_edges.delete(self)
    @to_vertex.in_edges.delete(self)
    @to_vertex.in_degree -= 1
    @from_vertex = nil
    @to_vertex = nil
  end

  def inspect
    "From #{@from_vertex.value} To #{@to_vertex.value} \n"
  end
end
