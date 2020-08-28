# 8-13 USER PROFILE

# Start with a copy of 'user_profile.py' from page 149. Build a profile of yourself by calling 'build_profile()', using your first and last names and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
  """Build a User Profile"""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('andrew', 'harvey',
                            age=32,
                            height=68)

print(user_profile)