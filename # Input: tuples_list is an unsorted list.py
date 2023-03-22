# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples (tuples_list):

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval


def sort_by_interval_size (tuples_list):

# Input: no input
# Output: a string denoting all test cases have passed


def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main()
  # open file intervals.in and read the data and create a list of tuples
  in_file = open('intervals.in.txt', 'r')

  # merge the list of tuples
  merged_list = merge_tuples()

  # sort the list of tuples according to the size of the interval
  sort_by_interval_size()

  # run your test cases
  '''
  print (test_cases())
  '''

  # open file intervals.out and write the output list of tuples
  # from the two functions

if __name__ == "__main__":
  main()