#include <iostream>

using namespace std;

// Define the Node structure for the linked list
struct Node {
    int data;
    Node* next;
};

// Function to print the linked list
void printList(Node* n) {
    while (n != nullptr) {
        cout << n->data << " -> ";
        n = n->next;
    }
    cout << "nullptr" << endl;
}

int main() {
    // Create nodes
    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();

    // Assign data and link nodes
    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = nullptr;

    // Print the linked list
    cout << "Linked List: ";
    printList(head);

    return 0;
}