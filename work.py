# Maria Juliana Saavedra
# Thomas Gomez
# Alejandro Orozco
# Felipe Espinilla

# Practice Iterators and Generators 

sensor_readings = [
    22.5, 22.7, 22.6, 22.9,
    23.1, 23.4, 23.8, 24.0,
    24.3, 24.8
]

# Part 1 — Baseline: for Loop (Hidden Control)
for value in sensor_readings:
    print (value)

# Part 2 — Iterator: Explicit Control with next()

it = iter(sensor_readings)

next(it)
next(it)
next(it)

# Part 3 — Generator: Lazy Data Production


def sensor_stream(data):
    for value in data:
        print("Producing:", value)
        yield value

stream = sensor_stream(sensor_readings)

next(stream)
next(stream)
next(stream)

# Part 4 — yield vs return

def normal_func():
    print("Start")
    return 1
    print("End")

normal_func()

def gen_func():
    print("Start")
    yield 1
    print("Middle")
    yield 2
    print("End")
    
g = gen_func()
next(g)
next(g)
next(g)

# Part 5 — Generator State Is Preserved

def counter():
    x = 0
    while True:
        yield x
        x += 1

c = counter()
next(c)
next(c)
next(c)

# Part 6 — Generator Pipeline (Controlled Flow)

def high_temp_filter(stream, threshold):
    for value in stream:
        print("Filtering:", value)
        if value > threshold:
            yield value

stream = sensor_stream(sensor_readings)
filtered = high_temp_filter(stream, 23.0)

next(filtered)
next(filtered)

# Part 7 — Dunder (Magic) Methods
# 7.1 Object Creation and Display
# __init__ , __str__ , __repr__

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, age {self.age}"
    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age})"
    
u = User("Alice", 21)
print(u)
u

# 7.2 Truth and Size
# __len__ , __bool__

class Cart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    
    def __bool__(self):
        return len(self.items) > 0
    
cart = Cart(["apple", "banana"])
empty_cart = Cart([])

len(cart)
bool(cart)

if cart:
    print("Cart has items")

# 7.3 Indexing and Iteration
# __get__, __iter__, __next__

class Log:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]
    
log = Log([10, 20, 30, 40])

log[0]
log[2]

for x in log:
    print(x)

# 7.4 Comparison and Operators
# __eq__, __lt__, __ad__

class Score:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __add__(self, other):
        return Score(self.value + other.value)
    
a = Score(10)
b = Score(20)

a == b
a < b

c = a + b
c.value

# Part 8 — Dunder Methods and Generators

gen = sensor_stream(sensor_readings)

iter(gen) is gen
next(gen)


# Closures and Decorators 
# PART 1 - CLOSURES

# Lab 1.1 — Simple Closure (Data Persists)

def outer():
    x = 10
    def inner():
        print("x =", x)
    return inner

f = outer()
f()
f()

#Lab 1.2 — Closure with Changing State

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        print ("Count: = ", count)
    return inc

c = counter()
c()
c()
c()

# Lab 1.3 — Prove Where the Data Lives

print(c.__closure__)
print(c.__closure__[0].cell_contents)

# PART 2 - DECORATORS

# Lab 2.1 — Basic Decorator (Wrapper in Action)

def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()

# Lab 2.2 — Decorator vs Wrapper (IMPORTANT)

def demo_decorator(func):
    print("DECORETOR runs (definition time)")
    def wrapper():
        print("WRAPPER start")
        func()
        print("WRAPPER end")
    return wrapper

@demo_decorator
def say_hi():
    print("HI")

# Lab 2.3 — Inspect the Decorated Function

print (say_hi)
print(say_hi.__closure__)

# PART 3 - DECORATOR WITH ARGUMENTS 

def log_calls(func):
    def wrapper(*args):
        print("Calling with args: ", args)
        return func(*args)
    return wrapper 

@log_calls
def add(a, b):
    return a + b 

print(add(3, 4))
print(add(10, 20))

# PART 4 - CLOSURE VS DECORATOR 

# Lab 4.1 — Closure = Data Memory

def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

# Lab 4.2 — Decorator = Behavior Wrapping

def loud(func):
    def wrapper():
        print("LOUD MODE")
        func()
    return wrapper

@loud
def speak():
    print("hello")

speak()