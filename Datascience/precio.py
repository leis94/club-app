def cost_of_the_trip():
    inflation  = {'2016':5.75, '2017': 4.09, '2018':3.18, '2019':3.80}
    inflation_values = inflation.values()
    car_annual_cost_2015 = [5589600, 4444500, 4734250]
    current_annual_cost = []
    total = 0
    for cost in car_annual_cost_2015:
        for value in inflation_values:
            percentage = cost/100
            multiplier = percentage * value
            cost = cost + multiplier 
        current_annual_cost.append(cost)
    for value in current_annual_cost:
        total = total + value
        average = total/3
    monthly_cost = average / 12
    weekly_cost = monthly_cost / 4
    daily_cost = weekly_cost / 6
    cost_per_trip = daily_cost / 20

    cost_per_liter_of_gasoline = 2106
    range_of_kilometers_traveled_per_liter = range(9,29)
    sum_of_the_range = sum(range_of_kilometers_traveled_per_liter)
    range_length = len(range_of_kilometers_traveled_per_liter)
    average_kilometer_per_liter = sum_of_the_range / range_length
    cost_per_kilometer = 1/average_kilometer_per_liter * cost_per_liter_of_gasoline

    monthly_cost_of_living = 2018417
    weekly_cost_of_living = monthly_cost_of_living / 4 
    cost_of_living_per_day = weekly_cost_of_living / 6
    cost_of_living_per_trip = cost_of_living_per_day / 20
    total = cost_per_trip + cost_of_living_per_trip + cost_per_kilometer
    return total

def TrafficCalculation(trafic_color, total):
    if trafic_color == 'green':
        return total
    elif trafic_color == 'orange':
        percentage = total/100
        multiplier = percentage * 5
        total = total + multiplier
        return total
    elif trafic_color == 'red':
        percentage = total/100
        multiplier = percentage * 10
        total = total + multiplier
        return total
    elif trafic_color == 'deep red':
        percentage = total/100
        multiplier = percentage * 20
        total = total + multiplier
        return total
    else:
        return total


def Total_per_kilometer(trafic_color, kilometers):
    subtotal = cost_of_the_trip()
    total_cost_per_kilometer = subtotal * kilometers
    total = TrafficCalculation(trafic_color,total_cost_per_kilometer)
    return total


