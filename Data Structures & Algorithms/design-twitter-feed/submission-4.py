class Twitter:

    def __init__(self):
        self.g_id=0
        self.tweetsByUserId={}
        self.users={}
        self.followedUsersById={}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.g_id+=1
        if userId not in self.tweetsByUserId:
            self.tweetsByUserId[userId]=[]
        self.tweetsByUserId[userId].append(([self.g_id,tweetId]))

    def getNewsFeed(self, userId: int) -> List[int]:
        users=set()
        if userId in self.followedUsersById:
            users = self.followedUsersById[userId]
        users.add(userId)
        t=[]
        for user in users:
            if user in self.tweetsByUserId:
                t+=self.tweetsByUserId[user]
        t.sort()
        t.reverse()
        for i,x in enumerate(t):
            t[i]=x[1]
        return t[:min(len(t),10)]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followedUsersById:
            self.followedUsersById[followerId]=set()
        self.followedUsersById[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followedUsersById and followeeId in self.followedUsersById[followerId]:
            self.followedUsersById[followerId].remove(followeeId)
        
        
