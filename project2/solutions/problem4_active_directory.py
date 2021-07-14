class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    # We need to check if the user is a member of the group
    if user in group.get_users():
        return True
    else:
        # Check if the the group is not empty, if it is, return False
        if not group.get_groups():
            return False
        else:
            '''Search user in group by first search for the group and then for 
            the user
            '''
            for gp in group.get_groups():
                return is_user_in_group(user, gp)

# Create group and users

parent = Group("parentrgoup")
child = Group("user")
child1 = Group("")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
child.add_group(sub_child)
parent.add_group(child)

# User or group exists
print(is_user_in_group(sub_child_user, child)) # This should return True
print(is_user_in_group(sub_child_user, parent))  # This also will return True

# Test case user does not exist or it has no parent/group
print(is_user_in_group("Another one", sub_child))  # And this returns False

# Test case empty user
print(is_user_in_group(child1, parent))  # And this returns False
