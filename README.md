# Day 01: Python Socket Programming & Calculator 🚀

## 📝 Overview

This practical introduces basic socket programming in Python and implements a simple calculator class.

---

## 🧮 Calculator (`calculator.py`)

A simple calculator class demonstrating static methods and basic arithmetic operations.

### Features:

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division (with zero-check)

### How to Run:

```powershell
python calculator.py
```

### Code Summary:

- `Calculator` class with 4 static methods for basic operations
- Takes two integer inputs from user
- Displays all four operation results
- Includes error handling for division by zero

### Quick Code Reference:

```python
# Create calculator class with static methods
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    # subtract, multiply, divide...

# Use it
calculator = Calculator()
result = calculator.add(10, 5)  # 15
```

---

## 💬 Client-Server Chat Application

A simple TCP-based chat application using Python sockets.

### 🖥️ Server (`server.py`)

The server-side application that listens for incoming connections.

#### How to Run:

```powershell
python server.py
```

#### Code Summary:

- Creates a socket and binds to hostname and port 8080
- Listens for one client connection
- Server sends messages first, then receives client responses
- Messages alternate between server and client

#### Quick Code Reference:

```python
import socket

# Create and bind socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))

# Listen and accept connection
s.listen(1)
conn, addr = s.accept()

# Send and receive messages
message = input().encode()
conn.send(message)
incoming = conn.recv(1024).decode()
```

---

### 👤 Client (`client.py`)

The client-side application that connects to the server.

#### How to Run:

```powershell
python client.py
```

#### Code Summary:

- Prompts user for server hostname
- Connects to server on port 8080
- Client receives messages first, then sends responses
- Messages alternate between client and server

#### Quick Code Reference:

```python
import socket

# Create and connect socket
s = socket.socket()
host = input("Enter server hostname: ")
port = 8080
s.connect((host, port))

# Receive and send messages
incoming = s.recv(1024).decode()
message = input(">> ").encode()
s.send(message)
```

---

## 🎯 Key Concepts Learned

1. **Socket Programming**: Creating TCP connections using Python's `socket` module
2. **Client-Server Architecture**: Understanding the communication flow
3. **Object-Oriented Programming**: Using static methods in classes
4. **Error Handling**: Division by zero validation
5. **Encoding/Decoding**: Converting strings to bytes for network transmission

---

## 📌 Important Notes

⚠️ **For Chat Application:**

- Run `server.py` FIRST before starting the client
- Both terminals must remain open during the chat session
- Server and client must be on the same network (or use localhost)
- Default port: **8080**

---

## 🔧 Technologies Used

- Python 3.x
- Socket Library
- Standard I/O Operations
