# Test Cases

## Test Case 1: Valid Input

**Input / Action:**  
Enter [a valid input]

**Expected Result:**  
The program calculates and displays the correct [output]

**Actual Result:**  
The program performed as expected and returned the correct value

**Result:**  
Pass

---

## Test Case 2: Boundary Input

**Input / Action:**  
Enter the minimum or maximum allowed [input]

**Expected Result:**  
The program handles the boundary value correctly.

**Actual Result:**  
The program handles all numbers as expected, with a 0 returnign $0, though sufficiently large numbers result in a number expressed in scientific notation.
Negative numbers return negative results as one would expect

**Result:**  
Pass

---

## Test Case 3: Invalid Input

**Input / Action:**  
Enter an invalid value (such as text when a number is expected)

**Expected Result:**  
The program handles the invalid input without crashing.

**Actual Result:**  
The program throws an exception, expecting a float value to be input, meaning it is incapable of handling a string being input by the user

**Result:**  
Fail
