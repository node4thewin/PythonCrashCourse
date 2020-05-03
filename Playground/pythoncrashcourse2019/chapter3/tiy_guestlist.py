# Guest List
# 3-4

guests = ['Bob Marley', 'Ryan Giggs', 'Ronaldinho', 'Ronaldo', 'Paul Scholes']
print(guests)
#Example of how to insert and delete guests from list

guests.insert(5, 'Jose Antonio Reyes')

#invite1
print(f"\nI would like to cordially invite you, {guests[0]}, to dinner on March 1st, 2019 at 7:00PM.")
#invite2
print(f"\nI would like to cordially invite you, {guests[1]}, to dinner on March 1st, 2019 at 7:00PM.")
#invite3
print(f"\nI would like to cordially invite you, {guests[2]}, to dinner on March 1st, 2019 at 7:00PM.")
#invite4
print(f"\nI would like to cordially invite you, {guests[3]}, to dinner on March 1st, 2019 at 7:00PM.")
#invite5
print(f"\nI would like to cordially invite you, {guests[4]}, to dinner on March 1st, 2019 at 7:00PM.")
#invite6
print(f"\nI would like to cordially invite you, {guests[5]}, to dinner on March 1st, 2019 at 7:00PM.")

# 3-5 - Changing Guest List

missing_guest = guests.pop(5)

print(f"\nUnfortunately {missing_guest.title()} has been pronouned dead after a terrible car accident. I will update the guest list shorly. Thank you and RIP Reyes.")

guests.insert(5, 'Will Ferrell')

#invite1
print(f"\nI would like to cordially invite you, {guests[0]}, to dinner on March 1st, 2019 at 7:00PM. Sir {guests[5]} will be joining us instead of {missing_guest}. Sending condolences to the {missing_guest} family.")
#invite2
print(f"\nI would like to cordially invite you, {guests[1]}, to dinner on March 1st, 2019 at 7:00PM. Sir {guests[5]} will be joining us instead of {missing_guest}. Sending condolences to the {missing_guest} family.")
#invite3
print(f"\nI would like to cordially invite you, {guests[2]}, to dinner on March 1st, 2019 at 7:00PM. Sir {guests[5]} will be joining us instead of {missing_guest}. Sending condolences to the {missing_guest} family.")
#invite4
print(f"\nI would like to cordially invite you, {guests[3]}, to dinner on March 1st, 2019 at 7:00PM. Sir {guests[5]} will be joining us instead of {missing_guest}. Sending condolences to the {missing_guest} family.")
#invite5
print(f"\nI would like to cordially invite you, {guests[4]}, to dinner on March 1st, 2019 at 7:00PM. Sir {guests[5]} will be joining us instead of {missing_guest}. Sending condolences to the {missing_guest} family.")
#invite6
print(f"\nI would like to cordially invite you, {guests[5]}, to dinner on March 1st, 2019 at 7:00PM. You will be joining us instead of {missing_guest}. Sending condolences to the {missing_guest} family.")

# 3-6 New Table and Space for Additional Guests

guests.insert(0, 'George Clooney')
guests.insert(3, 'Mo Salah')
guests.append('Leo Messi')

print(f"\n{guests}")

print(f"\nAs an update, we have been able to procure a new table and thus will have three spots opening for our 7:00PM dinner on March 1st, 2019. The additional guests will be {guests[0]}, {guests[3]}, and {guests[8]}. Looking forward to a great night! Thank you.")

# 3-7 Shrinking Guest List
# I decided to use guests.pop(0) over and over again but 
# redefined the value after each print() call. 

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

rejection = guests.pop(0)
print(f"\nUnfortunately we will not have a large enough table in time for our Celebrity Dinner. We ask that you, {rejection}, accept this apology and consider us next time. Thank you.")

print(f"\n Congratulations {guests[0]} you are still invited! You were one of the last two selected for my Celebrity Dinner. while we wish everyone could have made it, we are especially happy to have you.")

print(f"\n Congratulations {guests[1]} you are still invited! You were one of the last two selected for my Celebrity Dinner. while we wish everyone could have made it, we are especially happy to have you.")


