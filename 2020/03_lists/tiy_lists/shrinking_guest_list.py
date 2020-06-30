# 3-7 Shrinking Guest List
# You just found out that your new dinner table won't arrive in time for the dinner, and you
# have space for only two guests.

# Start with your program from 3-6. Add a new line that prints a message saying that you can
# invite only two people for dinner.

guest_list = ['michael buble', 'michael jordan', 'tiger woods', 'otis barron', 'kobe bryant', 'mudge', 'callie barron', 'mike barron sr.']
message = "Unfortunately I have just received word that I can only invite two people to dinner this evening. Please accept my apology. The following people will still be invited..."
print(message)

# Use pop() to remove guests from your list one at a time until only two names remain
# in your list. Each time you pop a name from your list, print a message to that person letting
# them know you're sorry you can't invite them to dinner.

uninvited_guest = guest_list.pop(0)
print(f"My apologies {uninvited_guest.title()} but I have to rescind your invitation to dinner because of limited seating. Please excuse this aggregious resignation. Thank you and until next time, Andrew.")

uninvited_guest = guest_list.pop(0)
print(f"My apologies {uninvited_guest.title()} but I have to rescind your invitation to dinner because of limited seating. Please excuse this aggregious resignation. Thank you and until next time, Andrew.")

uninvited_guest = guest_list.pop(0)
print(f"My apologies {uninvited_guest.title()} but I have to rescind your invitation to dinner because of limited seating. Please excuse this aggregious resignation. Thank you and until next time, Andrew.")

uninvited_guest = guest_list.pop(1)
print(f"My apologies {uninvited_guest.title()} but I have to rescind your invitation to dinner because of limited seating. Please excuse this aggregious resignation. Thank you and until next time, Andrew.")

uninvited_guest = guest_list.pop(1)
print(f"My apologies {uninvited_guest.title()} but I have to rescind your invitation to dinner because of limited seating. Please excuse this aggregious resignation. Thank you and until next time, Andrew.")

uninvited_guest = guest_list.pop(2)
print(f"My apologies {uninvited_guest.title()} but I have to rescind your invitation to dinner because of limited seating. Please excuse this aggregious resignation. Thank you and until next time, Andrew.")

print(guest_list)

# Print a message to each of the two people still on your list, letting them knwo you're
# still invited.

print(f"Not to worry {guest_list[0].title()}. You are one of the two most important people in the world to me...and for that reason you are cordially invited to dinner with me!")
print(f"Not to worry {guest_list[1].title()}. You are one of the two most important people in the world to me...and for that reason you are cordially invited to dinner with me!")

# Use del to remove the last two name from your list, so you have an empty list. Print your list
# to make sure you actually have an empty list at the end of your program.

del guest_list[0]
del guest_list[0]
print(guest_list)
