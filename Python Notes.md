
#### What is a Variable?
A variable is like a container used to store data in a Python program.
You assign a value to it using the = operator.

name = "Ajit"         # Stores a string
age = 36              # Stores an integer
is_active = True      # Stores a boolean


#### What are Data Types?

**Data types** define the kind of data a variable can hold.

### 🔹 1. **Numeric Types**

| Type      | Description     | Example      |
| --------- | --------------- | ------------ |
| `int`     | Whole numbers   | `age = 36`   |
| `float`   | Decimal numbers | `pi = 3.14`  |
| `complex` | Complex numbers | `z = 2 + 3j` |

---

### 🔹 2. **Text Type**

| Type  | Description | Example         |
| ----- | ----------- | --------------- |
| `str` | Text string | `name = "Ajit"` |

---

### 🔹 3. **Boolean Type**

| Type   | Description   | Example            |
| ------ | ------------- | ------------------ |
| `bool` | True or False | `is_active = True` |

---

### 🔹 4. **Sequence Types**

| Type    | Description              | Example                       |
| ------- | ------------------------ | ----------------------------- |
| `list`  | Ordered, changeable list | `fruits = ["apple", "mango"]` |
| `tuple` | Ordered, unchangeable    | `colors = ("red", "blue")`    |
| `range` | Sequence of numbers      | `r = range(5)`                |

---

### 🔹 5. **Set Types**

| Type        | Description              | Example                     |
| ----------- | ------------------------ | --------------------------- |
| `set`       | Unordered, no duplicates | `nums = {1, 2, 3}`          |
| `frozenset` | Immutable set            | `fs = frozenset([1, 2, 3])` |

---

### 🔹 6. **Mapping Type**

| Type   | Description     | Example                                |
| ------ | --------------- | -------------------------------------- |
| `dict` | Key-value pairs | `person = {"name": "Ajit", "age": 36}` |

---

### 🔹 7. **None Type**

| Type   | Description      | Example    |
| ------ | ---------------- | ---------- |
| `None` | No value / empty | `x = None` |

---

## 🔍 Example Code:

```python
# Variable declarations with different data types
name = "Ajit"           # str
age = 36                # int
pi = 3.14               # float
is_logged_in = True     # bool
colors = ["red", "blue"]  # list
user = {"id": 1, "name": "Ajit"}  # dict
nothing = None          # NoneType
```
---

#### global Keyword in Python
The global keyword is used to modify a global variable from inside a function.

####  Without global

x = 10

def my_func():
    x = 5  # Local variable, doesn't change the global 'x'

my_func()
print(x)   # Output: 10


#### With global

x = 10

def my_func():
    global x
    x = 5  # Changes the global 'x'

my_func()
print(x)   # Output: 5

#### When to Use global
When you need to update a global variable inside a function.

Avoid overusing it – too many global variables make code hard to debug.

counter = 0

def increment():
    global counter
    counter += 1

increment()
increment()
print(counter)  # Output: 2


#### 🚫 Don't Confuse With: globals()
global (keyword) is used to modify a global variable.

globals() (built-in function) returns a dictionary of all global variables.

x = 42
print(globals()['x'])  # Output: 42

---