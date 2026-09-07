import heapq
class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)
        if userId not in self.posts:
            self.posts[userId] = []
        self.posts[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        followeePosts = []
        res = []
        for followee in self.follows[userId]:
            if followee in self.posts:
                time, tweet = self.posts[followee][-1]
                followeePosts.append((-time, tweet, followee, len(self.posts[followee]) - 2))
        heapq.heapify(followeePosts)
        while followeePosts and len(res) < 10:
            time, tweet, followee, idx = heapq.heappop(followeePosts)
            res.append(tweet)

            if idx >= 0:
                time, tweet = self.posts[followee][idx]
                heapq.heappush(followeePosts, (-time, tweet, followee, idx - 1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
            self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)