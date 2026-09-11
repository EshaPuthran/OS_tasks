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
```

After adding an item, the Producer calls:

```java
notifyAll();
```

to notify waiting threads that the buffer state has changed.

### Consumer Thread

The Consumer removes values from the shared buffer.

If the buffer is empty, the Consumer waits until an item is produced.

```java
while (queue.isEmpty()) {
    wait();
}
```

After removing an item, the Consumer calls:
```java
notifyAll();
```
to notify waiting threads that the buffer state has changed.

### Synchronization

The produce() and consume() methods are declared as synchronized:

```java
public synchronized void produce(int item)
```
```java
public synchronized void consume()
```
The synchronized keyword ensures that only one thread at a time can access the critical section of the shared buffer. This prevents multiple threads from modifying the shared queue at the same time.

### Program Flow 
![Program Flow Diagram](<img width="1267" height="1460" alt="producer_flow" src="https://github.com/user-attachments/assets/3692911a-4d19-4202-b31a-fb7673bb16c8" />
)

## Project Structure

```text
ProducerConsumer/
│
└── src/
    └── producerConsumer/
        └── ProducerConsumer.java
```

## Source Code

The program consists of the following classes:

### Buffer

The `Buffer` class represents the shared bounded buffer. It contains the `produce()` and `consume()` methods and controls access to the shared queue.

### Producer

The `Producer` class extends the Java `Thread` class and generates values from 1 to 10.

### Consumer

The `Consumer` class extends the Java `Thread` class and consumes the values produced by the Producer.

### ProducerConsumer

The `ProducerConsumer` class contains the `main()` method. It creates the shared buffer, Producer thread, and Consumer thread, and starts their execution.

## How to Run

### Using Eclipse

1. Open Eclipse.

2. Create a new Java Project.

3. Create a package named:

```text
producerConsumer
```

4. Create a Java class named:

```text
ProducerConsumer
```

5. Add the complete source code.

6. Save the project.

7. Right-click `ProducerConsumer.java`.

8. Select:

**Run As → Java Application**

9. The output will be displayed in the Eclipse Console.



## Sample Output

```text
Produced: 1
Consumed: 1
Produced: 2
Produced: 3
Consumed: 2
Produced: 4
Consumed: 3
Produced: 5
Produced: 6
Consumed: 4
Produced: 7
Consumed: 5
Produced: 8
Produced: 9
Consumed: 6
Produced: 10
Consumed: 7
Consumed: 8
Consumed: 9
Consumed: 10
```

> **Note:** The exact order of the output may vary because the Producer and Consumer execute concurrently.

## Important Concepts

| Concept | Purpose |
|---|---|
| `Thread` | Creates concurrent execution |
| `synchronized` | Provides mutual exclusion |
| `wait()` | Makes a thread wait for a condition |
| `notifyAll()` | Wakes waiting threads |
| `Queue` | Stores produced items |
| `LinkedList` | Implements the queue |
| `sleep()` | Adds a delay between operations |

## Buffer Capacity

The buffer capacity is set to **5**:

```java
private final int capacity = 5;
```

Therefore:

- When the buffer contains 5 items, the **Producer waits**.
- When the buffer is empty, the **Consumer waits**.
- When an item is produced or consumed, `notifyAll()` is used to notify waiting threads.
