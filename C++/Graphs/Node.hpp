#include <vector>
using std::vector;

template <typename T>
class Node {
  protected:
    T val;

    vector<Node*> children;
  public:
    Node(T value) : val(value) {
      children = vector<Node*>();
    }

    T getVal() {
      return val;
    }

    vector<Node<T>*> getChildren() {
      return children;
    }

    void insert(Node<T>*child) {
      children.push_back(child);
    }
};