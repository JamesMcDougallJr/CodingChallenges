#include "counting_sort.cpp"
int main()
{
  int list[] = {1, 4, 1, 2, 7, 5, 2};
  std::vector<int> test = std::vector<int>();
  for (int el : list)
  {
    test.push_back(el);
  }
  std::pair<std::vector<int>, int> ret = counting_sort(test);
  return 0;
}