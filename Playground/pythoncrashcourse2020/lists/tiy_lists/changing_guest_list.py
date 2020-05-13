#3-5 CHANGING GUEST LIST

# You just heard that one of your guests can't make the dinner, so you need to send out a
# new set of invitations. You'll have to think of someone else to invite.

# Start with your program from 3-4. Add a print() call at the end of your program stating
# the name of the guest who can't make it.

guest_list = ['michael jordan', 'tiger woods', 'kobe bryant', 'mudge', 'callie barron']

remove_guest = guest_list.pop(4)
print(f"Unfortunately, we have just received word that {remove_guest.title()} has rescinded their invitation. Andrew fucked up.")

# Modify your list, replacing the name of the guest who can't make it with the name of the
# new person you're inviting.

guest_list.insert(4, 'susan barron')
print(f"{guest_list[4].title()} has decided to take the place of {remove_guest.title()}.")
print(guest_list)

# Print a second set of invitation messages, one for each person who is still in your list.

print(f"Hello! This is a confirmation for {guest_list[0].title()}. Please bring a copy of this message to dinner on the eve of May 16th, 2020.")
print(f"Hello! This is a confirmation for {guest_list[1].title()}. Please bring a copy of this message to dinner on the eve of May 16th, 2020.")
print(f"Hello! This is a confirmation for {guest_list[2].title()}. Please bring a copy of this message to dinner on the eve of May 16th, 2020.")
print(f"Hello! This is a confirmation for {guest_list[3].title()}. Please bring a copy of this message to dinner on the eve of May 16th, 2020.")
print(f"Hello! This is a confirmation for {guest_list[4].title()}. Please bring a copy of this message to dinner on the eve of May 16th, 2020.")

