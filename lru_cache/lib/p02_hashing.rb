class Fixnum
  # Fixnum#hash already implemented for you
end

class Array
  def hash
    return "empty array".hash if empty?
    hashed = map.with_index {|el, idx| el.hash * (idx + 1) }
    hashed.reduce(:+)
  end
end

class String
  def hash
    chars.map.with_index {|char, idx| (char.ord * (idx + 1)).hash }.reduce(:+)
  end
end

class Hash
  # This returns 0 because rspec will break if it returns nil
  # Make sure to implement an actual Hash#hash method
  def hash
    to_a.sort.hash
  end
end
