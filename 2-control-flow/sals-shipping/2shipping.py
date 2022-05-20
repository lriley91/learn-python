weight = 1.5

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

# Ground Shipping Premium
premium_ground = 125

# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Ground Shipping Cost:")
print(cost_ground)
print(" ")
print("Ground Shipping Premium Cost:")
print(premium_ground)
print(" ")
print("Drone Shipping Cost")
print(cost_drone)
print(" ")

if cost_ground < premium_ground and cost_ground < cost_drone:
  print("Cheapest Option: Ground Shipping for", cost_ground)
if premium_ground < cost_ground and premium_ground < cost_drone:
  print("Cheapest Option: Ground Shipping Premium for ", premium_ground)
if cost_drone < cost_ground and cost_drone < premium_ground:
  print("Cheapest Option: Drone Shipping for ", cost_drone)
