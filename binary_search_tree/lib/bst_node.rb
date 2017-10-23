class BSTNode
  attr_reader :value
  attr_accessor :left, :right, :parent

  def initialize(value, parent = nil)
    @value = value
    @parent = parent
  end

  def children
    [@left, @right].reject(&:nil?)
  end

  def descendents
    return [] if children.empty?
    result = children + children.map(&:descendents)
    result.flatten.reject(&:nil?)
  end
end
