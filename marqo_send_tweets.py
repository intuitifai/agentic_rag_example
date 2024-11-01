import marqo

mq = marqo.Client(url="http://localhost:8882")

# Below are the synthetic tweets
tweets = [
    {"tweet": "After all the delays, finally seeing some progress. Not sure if I should be happy or cautious."},
    {"tweet": "Amazing effort by the team! But let's not get complacent now."},
    {"tweet": "Another day, another issue resolved. Slowly but surely, we’re getting there."},
    {"tweet": "Product launch went better than expected, though some bugs need addressing."},
    {"tweet": "Surprised to see such a quick response from customer support. Hope it lasts."},
    {"tweet": "Team managed a last-minute save, but can we keep up this pace?"},
    {"tweet": "The update was okay, but I’m still facing some glitches. Hope for more fixes soon."},
    {"tweet": "Sales are up, but I worry it’s just a seasonal spike."},
    {"tweet": "The new feature is interesting, though a bit difficult to use."},
    {"tweet": "Nice to see improvements, but why did it take so long?"},
    {"tweet": "The system seems faster now, though I wonder if it’ll stay stable."},
    {"tweet": "Impressed with the changes, but let’s see how it holds up under pressure."},
    {"tweet": "Finally, some progress! Just hope it’s not too little, too late."},
    {"tweet": "Loving the new UI, but performance is still an issue."},
    {"tweet": "Great initiative, though execution could have been better."},
    {"tweet": "The team did well, but deadlines are still slipping."},
    {"tweet": "Satisfied with the purchase, although delivery was delayed."},
    {"tweet": "Customer service has improved, but some training is still needed."},
    {"tweet": "App works fine, but still a bit laggy at times."},
    {"tweet": "Glad they listened to feedback, though improvements are minimal."}
]

mq.create_index("tweets-index")
mq.index("tweets-index").add_documents(tweets, tensor_fields=["tweet"])