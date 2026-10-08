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
        res = []
   
        for follower in followers:
            if follower in self.posts:
                index = len(self.posts[follower]) - 1
                count,tweet_id = self.posts[follower][index]
                heapq.heappush(all_posts,[count,tweet_id,follower,index - 1])
        
        while all_posts and len(res) < 10:
            count,tweet_id,followee_id,index = heapq.heappop(all_posts)
            res.append(tweet_id)
            if index >= 0:
                count,tweet_id = self.posts[followee_id][index]
                heapq.heappush(all_posts,[count ,tweet_id,followee_id,index - 1])
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
        
        
