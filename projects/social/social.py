import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()
    
    def fisher_yates(self, arr):
        copy_arr = list(arr)
        # iterate over the array 
        for idx in range(len(copy_arr)):
        # choose a random index
            rand_index = random.randint(0, len(copy_arr) - 1)
        # swap the current item with that random index
            copy_arr[idx], copy_arr[rand_index] = copy_arr[rand_index], copy_arr[idx]

        return copy_arr
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)

        # Create friendships
        # you could create a list with all possible friendship combinations
        all_friend_combos = []
        for person in range(1, num_users):
            for friend in range(person + 1, num_users + 1): # start 1 higher so we don't get reverse combo
                all_friend_combos.append((person, friend))
        
        # shuffle the list
        shuffled_combos = self.fisher_yates(all_friend_combos)

       # the grab the first N elements from the list.
        total_friendships = num_users * avg_friendships
        elements_needed =total_friendships // 2
        combos_to_make = shuffled_combos[:elements_needed]

        # the loop over the list and cal add_friendship
        for friendship in combos_to_make:
            self.add_friendship(friendship[0], friendship[1])



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set

        q.enqueue([user_id])

        while q.size() > 0:
            current_path = q.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:
                visited[current_user] = current_path

                friends =  self.friendships[current_user]

                for friend in friends:
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
