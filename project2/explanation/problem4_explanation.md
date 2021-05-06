# Active Directory solution explanation

We create an object called group holding the name, groups, and users.
Groups can hold sub-groups, and users.
Recursively check if a user is a member of a group.
The time complexity is O(n^2) while the space complexity is O(n).