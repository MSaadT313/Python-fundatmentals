import random

total_users = 10
min_friends = 1
max_friends = 6  # some users have many connections

with open("social_graph1.txt", "w") as f:
    for user in range(1, total_users + 1):
        num_friends = random.randint(min_friends, max_friends)
        # choose random friends, excluding self
        friends = random.sample([u for u in range(1, total_users + 1) if u != user], num_friends)
        f.write(f"{user}: {' '.join(map(str, friends))}\n")
