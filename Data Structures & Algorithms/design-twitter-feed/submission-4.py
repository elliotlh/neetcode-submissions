from dataclasses import dataclass
from typing import Tuple

@dataclass
class Tweet:
    tweet_id: int
    timestamp: int


class Twitter:
    def __init__(self):
        self.followers: Dict[int, Set[int]] = collections.defaultdict(set)
        self.tweets: Dict[int, deque[Tweet]] = collections.defaultdict(deque[Tweet])
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append(Tweet(tweetId, self.timestamp))
        
    def extendNewsFeed(self, tweets: deque[Tweet], feed: List[Tuple[int, Tweet]]) -> None:
        for tweet in tweets:
            heapq.heappush(feed, (tweet.timestamp, tweet))
            while len(feed) > 10:
                heapq.heappop(feed)


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        self.extendNewsFeed(self.tweets[userId], feed)
        for following in self.followers[userId]:
            self.extendNewsFeed(self.tweets[following], feed)
        feed.sort(reverse=True, key=lambda x: x[0])
        return [tweet.tweet_id for _, tweet in feed]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
