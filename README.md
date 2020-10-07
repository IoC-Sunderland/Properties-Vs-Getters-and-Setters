# Public, "Private" and "Protected" instance attributes
Other OO languages such as Java have the concept of Public, Private and Protected instance attributes.

In Java these are known as Access level modifiers.

Access level modifiers determine whether other classes can use a particular field or invoke a particular method (https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html).

We can mimic these access modifiers in Python classes but they are not strictly enforced. 

See class example: <strong>Underscores_in_Python</strong>

# Java Style Vs Python Style Classes
Here we create a Java Style class in Python i.e. a class with Public, "Private" and "Protected" instance attributes.

We then show how we can write the same class in Python without access modifiers.

# Properties
The use of the @property decorator allows getter and setter methods to be invoked automatically when an instance attribute is accessed.

@property decorator can be added after code has already been written if we need to add getters and setters for some reason i.e. change of implementation. 

See example: <strong>Properties</strong>

# Getters and Setters
In other OOP languages such as Java, getter and setter methods are used to enable access to private instnace variables.

In Python we don't enforce this and instance variables can be public. However, we can mimic this pattern by implementing Python Properties if required (see above).


