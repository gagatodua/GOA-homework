def remove_char_replace(s, char_to_remove):
    return s.replace(char_to_remove, "")

my_string = "hello world"
new_string = remove_char_replace(my_string, "o")
print(new_string)
# Output: hell 


def square_sum(numbers):
  """Calculates the sum of squares for a list of numbers."""
  return sum(i * i for i in numbers)

# Example usage:
my_list = [1, 2, 2]
result = square_sum(my_list)
print(f"The sum of squares for {my_list} is: {result}") 
# Output: The sum of squares for [1, 2, 2] is: 9 (because 1*1 + 2*2 + 2*2 = 9)