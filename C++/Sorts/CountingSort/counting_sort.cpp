#include <vector>
#include <iostream>

std::pair << std::vector<int> *, int > counting_sort(std::vector<int> &list)
{
  // initial fill of counts O(n)
  std::vector<int> *counts = new std::vector<int>(1);
  int median = 0;
  for (int num : list)
  {
    if (num >= counts->size())
    {
      std::vector<int> extended = std::vector<int>(num);
      counts->reserve(counts->size() + distance(extended.begin(), extended.end()));
      counts->insert(counts->end(), extended.begin(), extended.end());
    }
    (*counts)[num] = (*counts)[num] + 1;
  }

  // go through the list again summing with previous counts
  int current_sum = 0;
  for (int i = 0; i < counts->size(); i++)
  {
    (*counts)[i] += current_sum;
    current_sum += (*counts)[i];
    std::cout << (*counts)[i];
  }
  std::cout << std::endl;
  return counts;
}