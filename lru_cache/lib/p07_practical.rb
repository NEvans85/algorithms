require_relative 'p05_hash_map'

def can_string_be_palindrome?(string)
  char_count = HashMap.new
  string.each_char do |chr|
    char_count.include?(chr) ? char_count[chr] += 1 : char_count[chr] = 1
  end
  odd_counts = 0
  char_count.each {|_key, val| odd_counts += 1 if val.odd? }
  odd_counts > 1 ? false : true
end
