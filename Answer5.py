# A transport company charge the fare according to folling table:
# distance    charges
# 1-50         8 Rs./Km
# 51-100       10 Rs./Km
# >100         12 Rs./Km


def cal_fare(distance):

    if distance <= 50:
        return distance * 8
    elif distance <= 100:
        return 50 * 8 + (distance - 50) * 10
    else:
        return 50 * 8 + 50 * 10 + (distance - 100) * 12
    
distance = int(input("Enter the distance traveld (in km):"))

fare = cal_fare(distance)

print("The total fare is Rs. ", fare)