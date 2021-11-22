# Python Files and Function Name
from .aloha import say_hi
from .adios import say_goodbye


"""System Thinking in Python: Building a System of Code
In Python, we can organize our code into discrete—but related—units. And as our codebase grows, we'll begin thinking about our code more and more as a system of such interconnected components.

Classes are one of these fundamental units. As we've discussed previously, a class can have data (in the form of instance variables) and behaviors or actions (in the form of instance methods).

As we build more functionality, we may find that many of our classes are related—and that they share some of the same data and behaviors. For example, Cats and Dogs are both Animals, so they may have some of the same variables and methods. In these cases, it would be ideal if we were able to share code between these related types of objects. This would ensure our code follows the Don't Repeat Yourself (DRY) principle. It would also give us a simple shared interface so we can work with similar types of objects in a more organized way. For example, we would be able to specify (in one place) that all animals have a speak method, and avoid having to write this method in multiple classes.

Let's see how we can use inheritance to accomplish these goals."""
