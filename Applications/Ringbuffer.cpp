//
// Created by dingding on 24-6-20.
// Ringbuffer Implementation
//
#include <iostream>
#include <vector>
using namespace std;

#define MAX_SIZE 5

typedef struct {
    int items[MAX_SIZE];
    int front;
    int rear;
} QUEUE;

void initialize(QUEUE *q) {
    q->front = -1;
    q->rear = -1;
}

bool isFull(QUEUE *q) {
    if ((q->rear + 1) % MAX_SIZE == q->front) {
        cout << "Queue Full" << endl;
        return true;
    }
    return false;
}

bool isEmpty(QUEUE *q) {
    if (q->front == -1 && q->rear == -1) {
        cout << "Queue Empty" << endl;
        return true;
    }
    return false;
}

void enqueue(QUEUE *q, int val) {
    if (isFull(q)) {
        return;
    }
    if (isEmpty(q)) {
        q->front = 0;
        q->rear = 0;
    }else {
        q->rear = (q->rear + 1) % MAX_SIZE;
    }
    q->items[q->rear] = val;
}

void dequeue(QUEUE *q) {
    if (isEmpty(q)) {
        return;
    }
    int val = q->items[q->front];
    cout << "Dequeue Val: " << val << endl;
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    }else {
        q->front = (q->front + 1) % MAX_SIZE;
    }
}

int main() {
    QUEUE* q;
    q = (QUEUE *) malloc(sizeof(QUEUE));
    initialize(q);
    enqueue(q, 10);
    dequeue(q);
    dequeue(q);
    dequeue(q);
    return 0;
}


