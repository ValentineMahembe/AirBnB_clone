This is my first attempt at the AirBnB clone project in partial fulfilment of the ALXSE course

The ALX is a complete web application, integrating database storage, a back-end API, and front-end interface in a clone of AirBnB.

This team project is part of the (Alx) Holberton School Software Engineering program.
It represents the first step towards building a full web application.

This first step consists of:

	1)a custom command-line interface for data management,
	2)and the base classes for the storage of this data.

Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

Command	Example
Run the console						./console.py
Quit the console					(hbnb) quit
Display the help for a command				(hbnb) help <command>
Create an object (prints its id)			(hbnb) create <class>
Show an object						(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object					(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances of a class		(hbnb) all or (hbnb) all <class>
Update an attribute of an object			(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")

