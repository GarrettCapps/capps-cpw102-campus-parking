#Define hourly rate
hourly_rate = 2.0
def main():
    hours_parked = 0.0
    cost = 0.0
    #Prompt user for hours parked
    hours_parked = float(input("How may hours will you be parked? "))
    #Calculate price
    cost = estimate_cost(hours_parked)
    #Return price to user
    print("Your parking will cost $", cost, sep="")
def estimate_cost(hours_parked):
    cost = hourly_rate * hours_parked
    return cost

# call main
main()