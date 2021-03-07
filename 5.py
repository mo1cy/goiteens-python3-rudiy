first_day = 500 #accounts deleted
pair_user = 50 #hrn
odd_user = 40 #hrn
profit = 500 #hrn
pair_users = 250 * pair_user #hrn
odd_users = 250 * odd_user #hrn
total_loss_of_deleted_users = pair_users + odd_users
total_loss = profit - total_loss_of_deleted_users
print("total loss:" ,total_loss)
