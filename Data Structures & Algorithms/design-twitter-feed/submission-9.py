import heapq
class Twitter:

    def __init__(self):
        self.posts = {}
        self.following = {}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        if userId in self.posts:
            self.posts[userId].append([self.count,tweetId])
        else:
            self.posts[userId] = [[self.count,tweetId]]
            self.following[userId] = set()
            self.following[userId].add(userId)

        self.count = self.count - 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.following.get(userId)
        all_posts = []
   
        for followee in followers:
            if followee in self.posts:
                if len(self.posts[followee]) > 10:
                    cur_user = []
                    for i in range(-1,-11,-1):
                        cur_user.append(self.posts[followee][i])
                        all_posts.append(self.posts[followee][i])
                    self.posts[followee] = cur_user
                else:
                    for post in self.posts[followee]:
                        all_posts.append(post)
        heapq.heapify(all_posts)
        res = []

        while all_posts and len(res) < 10:
            res.append(heapq.heappop(all_posts)[1])
        
        return res
                
        

        

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId in self.following:
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set()
            self.following[followerId].add(followerId)
            self.following[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
         if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
        
