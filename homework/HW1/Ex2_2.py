doctor_hto_copecs = 5 # copecs per 1 view
doctor_hto_hrn = doctor_hto_copecs / 100 # hryvnyas per 1 view
channel_views = 1000
profit = channel_views * doctor_hto_hrn
print("Total profit: ", profit, "hrn")