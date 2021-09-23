# "l" at the end of variable name means love cuz couldn't repeat

print("Welcome to the Love Calculator!")
name1 = input("What is your name? ")
name2 = input("What is their name? ")
#Lower case names
lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
#Counting "TRUE" letters
lower_case_name1_t = lower_case_name1.count("t")
lower_case_name1_r = lower_case_name1.count("r")
lower_case_name1_u = lower_case_name1.count("u")
lower_case_name1_e = lower_case_name1.count("e")
lower_case_name2_t = lower_case_name2.count("t")
lower_case_name2_r = lower_case_name2.count("r")
lower_case_name2_u = lower_case_name2.count("u")
lower_case_name2_e = lower_case_name2.count("e")
#Counting "LOVE" letters
lower_case_name1_l = lower_case_name1.count("l")
lower_case_name1_o = lower_case_name1.count("o")
lower_case_name1_v = lower_case_name1.count("v")
lower_case_name1_el = lower_case_name1.count("e")
lower_case_name2_l = lower_case_name2.count("l")
lower_case_name2_o = lower_case_name2.count("o")
lower_case_name2_v = lower_case_name2.count("v")
lower_case_name2_el = lower_case_name2.count("e")
#Adding "TRUE" names
name_t_added = lower_case_name1_t + lower_case_name2_t
name_r_added = lower_case_name1_r + lower_case_name2_r
name_u_added = lower_case_name1_u + lower_case_name2_u
name_e_added = lower_case_name1_e + lower_case_name2_e
#Adding "LOVE" name
name_l_added = lower_case_name1_l + lower_case_name2_l
name_o_added = lower_case_name1_o + lower_case_name2_o
name_v_added = lower_case_name1_v + lower_case_name2_v
name_el_added = lower_case_name1_el + lower_case_name2_el
#Adding all variables
true_added = name_t_added + name_r_added +name_u_added + name_e_added
love_added = name_l_added + name_o_added + name_v_added + name_el_added
love_score = str(true_added) + str(love_added)
#Interpretor
if int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos. ;)")
elif int(love_score) < 10:
    print(f"Your love score is {love_score}, You should stay away from each other.")
elif int(love_score) > 45 and int(love_score) < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
