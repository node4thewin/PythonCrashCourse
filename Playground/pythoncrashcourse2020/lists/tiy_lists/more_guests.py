# 3-6 MORE GUESTS

# You just found a bigger dinner table, so now more space is available. Think of three more
# guests to invite to dinner.

# Start with your program from Exercise 3-4. Add a print() call at the end of your program
# stating the name of the guest who can't make it.

guest_list = ['michael jordan', 'tiger woods', 'kobe bryant', 'mudge', 'callie barron']
print(guest_list)
print("\nHey everyone! I just found a bigger dinner table so I have room for three more!\n")

# Use insert() to add one new guest to the beginning of your list.
guest_list.insert(0, 'michael buble')
print(guest_list)

# Use insert() to add one new guest to the middle of the list.
guest_list.insert(3, 'otis barron')
print(guest_list)

# Use append() to add one new guest to the end of your list.
guest_list.append('mike barron sr.')
print(guest_list)

# Print a new set of invitation messages, one for each person in your list.

print(f'UPDATED INVITE: Hello {guest_list[0].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[1].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[2].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[3].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[4].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[5].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[6].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
print(f'UPDATED INVITE: Hello {guest_list[7].title()}! You are cordially invited to the bigger and better dinner with Andrew Harvey and the gang!')
