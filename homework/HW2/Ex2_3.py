# 3. В гравця є 100 одиниць HP (health points). 
# В грі є 3 монстра: скелет, зомбі, павук.k 
# Кожен з них наносить певний damage (урон) гравцю. 
# Перевірити чи помре гравець після 5 ударів зомбі, 
# 1 удару скелету та 2 укусів павука, якщо урон скелета = 15, 
# зомбі = 5, павука = 40. Вивести повідомлення “You die!” 
# якщо гравець помер, або “You have only {HP}” якщо він вижив, де HP - залишок здоров’я.
print("After five zombie damages, one skeleton damage and 2 spider damages ...")
health_points =100
skeleton_damage=15
zombie_damage=5
spider_damage=40
if health_points>(5*zombie_damage+skeleton_damage+2*spider_damage):
    print ("You have only ",health_points-(5*zombie_damage+skeleton_damage+2*spider_damage), "{HP}")
else:    
    print ("You die!")

