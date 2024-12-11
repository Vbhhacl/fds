#include <iostream>
using namespace std;

class Deque {
    int arr[10];
    int front, rear, size;

public:
    Deque() {
        front = -1;
        rear = -1;
        size = 10;
    }

    bool isFull() {
        return (front == 0 && rear == size - 1) || (rear + 1 == front);
    }

    bool isEmpty() {
        return front == -1;
    }

    void addFront(int value) {
        if (isFull()) {
            cout << "Deque is full!" << endl;
            return;
        }
        if (front == -1) {
            front = rear = 0;
        } else if (front == 0) {
            front = size - 1;
        } else {
            front--;
        }
        arr[front] = value;
    }

    void addRear(int value) {
        if (isFull()) {
            cout << "Deque is full!" << endl;
            return;
        }
        if (front == -1) {
            front = rear = 0;
        } else if (rear == size - 1) {
            rear = 0;
        } else {
            rear++;
        }
        arr[rear] = value;
    }

    void deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty!" << endl;
            return;
        }
        if (front == rear) {
            front = rear = -1;
        } else if (front == size - 1) {
            front = 0;
        } else {
            front++;
        }
    }

    void deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty!" << endl;
            return;
        }
        if (front == rear) {
            front = rear = -1;
        } else if (rear == 0) {
            rear = size - 1;
        } else {
            rear--;
        }
    }

    void display() {
        if (isEmpty()) {
            cout << "Deque is empty!" << endl;
            return;
        }
        int i = front;
        while (true) {
            cout << arr[i] << " ";
            if (i == rear) break;
            i = (i + 1) % size;
        }
        cout << endl;
    }
};

int main() {
    Deque dq;

    dq.addRear(10);
    dq.addRear(20);
    dq.addFront(5);
    dq.display();

    dq.deleteFront();
    dq.display();

    dq.deleteRear();
    dq.display();

    return 0;
}
