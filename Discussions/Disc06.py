# https://inst.eecs.berkeley.edu/~cs61a/fa19/disc/disc06.pdf

"""
1.2 Write a function that takes in no arguments and returns two functions, prepend and get,
which represent the “add to front of list” and “get the ith item” operations, respectively.
Do not use any python built-in data structures like lists or dictionaries.
"""

def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """

    get = lambda x: "Index out of range!"
    def prepend(value):
        nonlocal get
        f = get
        def get(i):
            if i == 0:
                return value
            return f(i - 1)
    return prepend, lambda x: get(x)


# 2.2 Write three different classes, Server, Client, and Email to simulate email.

class Email:
    """Every email object has 3 instance attributes: the message, the sender name, and the recipient name."""
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
    
    class Server:
        """Each Server has an instance attribute clients, which is a dictionary that associates client names with client objects."""
        def __init__(self):
            self.clients = {}

        def send(self, email):
            """Take an email and put it in the inbox of the client it is addressed to."""
            self.clients[email.recipient_name].inbox.append(email)

        def register_client(self, client, client_name):
            """Takes a client object and client_name and adds it to the clients instance attribute."""
            if client_name not in self.clients:
                self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which isused for addressing emails to the client),
    server (which is used to send emails out to other clients),
    and inbox (a list of all emails the client has received)."""
    def __init__(self, server, name):
        self.inbox = []
        self.server = server
        self.name = name

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        self.server.send(Email(msg, self.name, recipient_name))


    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)

# 3.1 Complete the implementation for the Cat class by overriding __init__ and talk methods of Pet class, and addi a new lose_life method.

class Pet():
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
        
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
        
    def talk(self):
        print(self.name)
        
class Dog(Pet):
    def talk(self):
        print(self.name +'says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives = 9):
        self.is_alive = True
        self.name = name
        self.owner = owner
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas','Tammy').talk()
        Thomas says meow!
        """
        print(self.name + " says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reach zero, 'is_alive' becomes False."""
        if self.is_alive:
            self.lives -= 1
            if self.lives == 0:
                self.is_alive = False

# 3.2 NoisyCat is just like a normal Cat. However, it talks twice as much as a normal Cat!

class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic','James').talk()
        Magic says meow!
        Magic says meow!
        """
        Cat.talk(self)
        Cat.talk(self)


# 3.4 Implement the Foo class so that the following interpreter session works as expected.


class Foo:
    def __init__(self, bar):
        self.bar = bar

    def g(self, y):
        """
        >>> x = Foo(1)
        >>> x.g(3)
        4
        >>> x.g(5)
        6
        >>> x.bar = 5
        >>> x.g(5)
        10
        """
        return y + self.x