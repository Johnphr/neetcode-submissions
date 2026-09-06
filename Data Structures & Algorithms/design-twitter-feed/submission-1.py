class Twitter:

    def __init__(self):
        self.follows = {}
        self.posts = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows:
            self.follows[userId] = set()
            self.follows[userId].add(userId)
        self.posts.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        count = 0
        i = len(self.posts) - 1
        res = []
        while i > -1 and count < 10:
            user, tweet = self.posts[i]
            if user in self.follows[userId]:
                count += 1
                res.append(tweet)
            i -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
            self.follows[followerId].add(followerId)
        self.follows[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
