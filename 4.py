loader = 25 #parcels
parcel = 5 #kilograms
car = 150 #kilograms was in car from start
already_transfered = loader * parcel
left_in_car = car - already_transfered #kilograms
parcels_left_in_car = left_in_car / parcel
print("parcels left in car:" ,parcels_left_in_car)
