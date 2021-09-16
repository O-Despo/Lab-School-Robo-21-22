import random

def role_n_sides_n_times(sides, roles):
    """Role a n sided die n times"""
    roles_list = []

    for roles in range(roles):
        role = random.randint(1, sides)
        roles_list.append(role)
    
    return roles_list

def role_one(sides = 6):
    return random.randint(1, sides)

def role_w_mod(sides = 20, mod = 1):
    role = random.randint(1, sides) + mod
    return role

def role_n_sides_dif(sides):
    ops = list(range(1, sides + 1))
    roles_list = []

    while(len(ops) != 0):
        role = random.choice(ops)
        roles_list.append(role)
        ops.remove(role)

    return roles_list

roles = role_one(4) 
print(roles)
