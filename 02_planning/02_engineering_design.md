# Engineering Design

**Project:** Campus Parking Helper  
**Team members:**  Garrett Capps
**Date:** 30 September 2026

## Problem Summary
CPTC parking's pricing is not automated, and must be estimated manually by drivers

## Proposed solution
The writing of a program which will tell a driver their estimated parking cost after getting the duration of parking from the user


## Technical design

### Inputs
_What data and information will go into the program? What data types will the program use to represent that data?_

**hours parked** (float): the anticipated number of hours parked

### Processing
_What will the program do with the data? What calculations will it perform?_ 
Determine the cost; Multiply the hours parked by 2.0 (dollars)
```
estimated cost = hours_parked * 2.0
```

### Output
_What will the program return or print to the user?_
The estimated parking fee based off the given parking time
### Functions
_What function(s) could this program use to modularize the logic? What actions belong together?_
estimate_cost, which multiples the user's specified parking time, in hours, by the hourly fee
## Example interaction

```text
User input: 2.5

Program output: Your parking will cost $5.0
```

## Implementation plan

1. 
2. 
3. 

