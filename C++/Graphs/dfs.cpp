#include "Node.hpp"

#include <iostream>
#include <unordered_map>
#include <stack>

using namespace std;
/**
 * Performs DFS using stack on a root node
 * returns the pointer to the node with the desired value
 */
Node<int> * dfs(Node<int>* root, int target) {
  stack<Node<int>*> stk = stack<Node<int>*>();
  stk.push(root);
  Node<int> * current;
  while (!stk.empty()) {
    current = stk.top();
    stk.pop();
    if (current->getVal() == target) {
      return current;
    }
    for (Node<int> *child: current->getChildren()) {
      stk.push(child);
    }
  }
  return nullptr;
}

int main() {
  auto graph = unordered_map<int,Node<int>*>();
  Node<int>* root = new Node<int>(10);
  graph[10] = root;
  for(int i = 8; i < 10; i++) {
    graph[i] = new Node<int>(i);
    root->insert(graph[i]);
  }
  for(int i = 11; i < 13; i++) {
    graph[i] = new Node<int>(i);
    root->insert(graph[i]);
  }
  auto found = dfs(root,20);
  if (found) {
    cout << found->getVal() << endl;;
  }
  else {
    cout << "20 not found" << endl;
  }
  return 0;
}