# A RouteTrie will store our routes and their associated handlers

class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
    def insert(self, path):
        paths = split_path(path)
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        c_node = self.root

        for p in paths:
            if p not in c_node.items:
                c_node.insert(p)
            c_node = c_node.items[p]
        
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        paths = split_path(path)
        c_node = self.root

        for p in paths:
            if p not in c_node.items:
                return None
            c_node = c_node.items[p]
        
        return c_node.utility
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.utility = None
        self.items = {}
    def insert(self, p):
        # Insert the node as before
        self.items[p] = RouteTrieNode()
        
"""
Next we need to implement the actual Router. The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.
Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.
"""
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_utility, not_found_utility):
        
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        
        self.root = RouteTrieNode()
        self.utility = root_utility
        self.not_found_utility = not_found_utility

    def add_handler(self, path, data):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        paths = self.split_path(path)
        c_node =  self.root

        for p in paths:
            if p not in c_node.items:
                c_node.insert(p)
            
            c_node = c_node.items[p]
        # Set the data 
        c_node.utility = data
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        # Check for path
        if path == "/":
            return "root_handler"
        
        paths = self.split_path(path)

        c_node = self.root

        for p in paths:
            # Check if p exists otherwise throw a 404 exception
            try:
                if c_node.items[p]:
                    c_node = c_node.items[p]
            except:
                return "404 page not found"
        if not c_node.utility:
                return "404 not found"
        return c_node.utility


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        if path[0] == "/":
            path = path[1:]
        if path[-1] == "/":
            path = path[:-1]

        paths = path.split("/")
        # Return all the paths
        return paths

# Test Cases
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
