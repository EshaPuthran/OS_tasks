# Producer–Consumer Problem using Threads in Java

## Overview

This project implements the classic Producer–Consumer problem using threads and synchronization in Java.

The Producer–Consumer problem demonstrates how multiple threads can safely communicate through a shared resource. In this implementation, a bounded buffer is shared between a Producer thread and a Consumer thread.

The Producer generates items and places them into the buffer, while the Consumer removes and consumes the items from the buffer.

## Objective

To implement the Producer–Consumer problem using Java threads and demonstrate:

- Thread creation and execution
- Shared resource management
- Synchronization between threads
- Inter-thread communication using `wait()` and `notifyAll()`
- Handling of a bounded buffer

## Technologies Used

- Java
- Java Threads
- Queue
- LinkedList
- `synchronized`
- `wait()`
- `notifyAll()`

## Approach

A shared buffer is implemented using a `Queue<Integer>` with a fixed capacity of 5 elements.

Two threads are created:

### Producer Thread

The Producer generates integer values from 1 to 10 and inserts them into the shared buffer.

If the buffer is full, the Producer waits until space becomes available.

```java
while (queue.size() == capacity) {
    wait();
}
```java

After adding an item, the Producer calls:

```java
notifyAll();

to notify waiting threads that the buffer state has changed.

### Consumer Thread


