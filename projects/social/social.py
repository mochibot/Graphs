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

    def populate_graph(self, numUsers, avgFriendships):
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
        # (using code from lecture)
        # Add users
        for i in range(numUsers):
            self.add_user(f'user {i + 1}')
        # Create friendships
        possibilities = []
        for key in self.users:
            for i in range(key + 1, self.last_id + 1):
                possibilities.append((key, i))

        random.shuffle(possibilities)
        for i in range(numUsers * avgFriendships // 2):
            friendship = possibilities[i]
            self.add_friendship(friendship[0], friendship[1])

        # totalFriends = numUsers * avgFriendships
        # flag = True
        # possibilities = []
        # while flag:
        #     possibilities = [random.randint(0, 4) for i in range(numUsers)]
        #     if sum(possibilities) == totalFriends:
        #         flag = False

        # friends = possibilities.copy()
        # for i in range(numUsers):
        #     num = friends[i]
        #     while num > 0:
        #         friend = random.randint(i + 1, numUsers - 1)
        #         if friend != i + 1 and friend not in self.friendships[i + 1] and friends[friend] > 0:
        #             self.add_friendship(i + 1, friend)
        #             friends[friend] -= 1
        #             num -= 1
        # print(friends)
        # return 
    

    
    def bfs(self, starting_vertex, destination_vertex):
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue( [starting_vertex] )
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            v = path[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.friendships[v]:
                    # COPY THE PATH
                    path_copy = path.copy()
                    # APPEND THE NEIGHOR TO THE BACK
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        # version 1 (aka lazy approach) - using bfs algo from lecture (see above)
        # q = Queue()
        # q.enqueue(user_id)
        # path = []
        # while q.size() > 0:
        #     node = q.dequeue()
        #     if node not in visited:
        #         path = self.bfs(user_id, node)
        #         visited[node] = path
        #         for friend in self.friendships[node]:
        #             q.enqueue(friend)            
        # return visited

        #version 2 - modified BFS algorithm
        q = Queue()
        q.enqueue([user_id])
        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]
            if node not in visited:
                visited[node] = path
                for friend in self.friendships[node]:
                    new_path = path.copy()
                    new_path.append(friend)
                    q.enqueue(new_path)            
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
