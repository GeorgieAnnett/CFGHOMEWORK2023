## (Section 1: Theory Questions [31 marks])

### 1.1    What does SDLC stand for?	1 mark

- Software Development Life Cycle

### 1.2   What exception is thrown when you divide a number by 0?	1 mark

- ‘ZeroDivisionError’

### 1.3   What is the git command that moves code from the local repository to the remote repository? 	1 mark

- Git Push

### 1.4   What does NULL represent in a database? 	   1 mark


- The absence of a value. NULL can also indicate an unknown value.

### 1.5   Name 2 responsibilities of the Scrum Master 	2 marks

-	Helps to facilitate rituals i.e., Daily Scrum, Sprint Review 
-	Leading the SCRUM team, providing guidance on how to complete tasks laid out in sprints or daily sprints.

### 1.6   Name 2 debugging methods, and when you would use them.	  4 marks

-	Version control: this includes using version control systems such as Git to see when a problem was introduced.
-	Unit tests: automated tests that are written to test individual components of the code. It imports the use of the unittest module. 


### 1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. 

```def can_pay(price, cash_given):
   if cash_given >= price:
       return True
   else:
       return False
 ```
	  

-	This would throw an error if a numeric value – either an integer or a float – was not given. 
-	For example, if a string or a Boolean value was given instead it would throw an error. 
-	This means we would have to use exception handling in our code. For example, you could print an error message and add on a return false to show that the payment cannot be made.
-	We could also convert the if/else statements inside a try block which would raise an error if there is not a numeric value 
-	For example:

```def can_pay(price, cash_given):
try:
   if cash_given >= price:
       return True
   else:
       return False
except TypeError:
print(“Error: invalid input”)
return False 
```

### 1.8    What is git branching? Explain how it is used in Git. 	  6 marks


-	Git branching is effectively when you diverge from your main branch in git. This is useful because it means that you can continue to work on a programme without messing up the main branch.
-	One way that git branching can be used in git is by allowing for collaboration between multiple developers. Like I mentioned above multiple developers can work on the same repository by creating separate branches for each developer. These changes can be merged back into the main branch. 
-	A second way it can be used in git is for debugging a programme. Developers can create a new branch from the main repository specifically for fixing an individual bug. This allows developers to fix a programme without disrupting ongoing work to the main branch. 

### 1.9 Design a restaurant ordering system. You do not need to write code, but describe a high-level approach: 
a.	Draw a list of key requirements.
b.	What are your main considerations and problems?
c.	What components or tools would you potentially use? 	  10 marks

-	A. 
- - Ask if customer has made a reservation?
- - Ask if you want anything to eat or drink?
- - A menu that can be shown to customers with different options both food and drink
- - Different menus that cover breakfast, lunch, dinner
- - Ability to take orders and pass them to the chef to prepare. 
- - Assign a table/order number and the customer details to a specific order. 
-	B. 
- - Making sure you have enough stock for the chef to make the required number of dishes, not over/under ordering food prep.
- - Orders must be processed in the order that it is taken to ensure that there is no long wait/ an order isn’t forgotten about. 
- - Make sure reservations are not overlooked, as to ensure that you can seat everyone in your restaurant and are not overbooked.
-	C. 
- - A web app that allows customers to look at the menu, it can be regularly updated to show specials and display anything that might be out of stock.
- - APIs for custom credit or debit card payment services
- - Software where customers can leave tips for staff as a % of their bill, the same software also divides the sum of tips equally amongst all staff. 

