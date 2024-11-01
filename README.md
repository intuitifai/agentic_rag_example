# Agentic RAG first example.

# Steps to Install Marqo

Marqo is an open-source vector search engine, and you can easily set it up using Docker. Here are the steps to install and run Marqo locally:

## Prerequisites

- **Docker**: Make sure Docker is installed on your machine. You can download Docker from [Docker's official website](https://www.docker.com/get-started).

## Step-by-Step Installation

1. **Pull the Marqo Docker Image**

   First, pull the latest Marqo Docker image by running:

```bash
   docker pull marqoai/marqo:latest
```

2. **Run the Marqo Docker Container**
```bash
    docker run --name marqo -it -p 8882:8882 marqoai/marqo:latest
```

# Output
```bash
> Entering new AgentExecutor chain...
Thought: The question is asking for the output of a Python code snippet. I need to execute the code to get the result.

Action: REPL
Action Input: sum(i for i in range(10))
Observation: 45
Thought:Thought: The code snippet provided is a Python expression that calculates the sum of numbers from 0 to 9. The result should be a numerical value.

Action: REPL
Action Input: sum(i for i in range(10))
Observation: 45
Thought:Here's the answer:

Question: What would be the output of the code: sum(i for i in range(10))
Thought: The question is asking for the output of a Python code snippet. I need to execute the code to get the result.

Action: REPL
Action Input: sum(i for i in range(10))
Observation: 45
Thought:Here's the answer:

Final Answer: The output of the code: sum(i for i in range(10)) is 45.

> Finished chain.
The output of the code: sum(i for i in range(10)) is 45.


> Entering new AgentExecutor chain...
Thought: To find the value of the multiplication, I'll use the Calculator tool.

Action: Calculator
Action Input: 108*1203
Observation: The result of 108*1203 is 129924.
Thought:Thought: I now know the value of the multiplication.

Final Answer: 129924

> Finished chain.
129924


> Entering new AgentExecutor chain...
Thought: I'm looking for a tweet that mentions a last-minute save, and it's likely to be a sports-related tweet.

Action: Text Classification
Action Input: "last-minute save"
Observation: I would classify this tweet as Positive. The word "save" implies a successful outcome, which is a positive event.
Thought:Thought: Since the tweet is likely to be Positive and sports-related, I should look for a tweet that is classified as Positive and contains sports-related keywords.

Action: Text Similarity
Action Input: "sports last-minute save"
Observation: ['Team managed a last-minute save, but can we keep up this pace?', "Amazing effort by the team! But let's not get complacent now.", 'Finally, some progress! Just hope it’s not too little, too late.', 'The team did well, but deadlines are still slipping.', 'Another day, another issue resolved. Slowly but surely, we’re getting there.', 'Surprised to see such a quick response from customer support. Hope it lasts.', 'Satisfied with the purchase, although delivery was delayed.', 'After all the delays, finally seeing some progress. Not sure if I should be happy or cautious.', 'The update was okay, but I’m still facing some glitches. Hope for more fixes soon.', 'Great initiative, though execution could have been better.']
Thought:Thought: The Text Similarity action returned a list of tweets that are similar to the input query "sports last-minute save". I should now look for a tweet in this list that mentions "team managed" to confirm if it's a tweet where a team managed a last-minute save.

Action: Text Classification
Action Input: "Team managed a last-minute save, but can we keep up this pace?"
Observation: I would classify this tweet as Neutral. The tone is neither overwhelmingly positive nor negative, but rather a mix of relief and caution. The use of "last-minute save" implies a sense of accomplishment, but the question "can we keep up this pace?" suggests uncertainty and a desire for continued improvement.
Thought:Here's the continuation:

Thought: Since the tweet is classified as Neutral, it's possible that it's a tweet where a team managed a last-minute save, but it's not necessarily a positive or celebratory tweet. I should still look for a tweet in the list that mentions "team managed" to confirm if it's the one I'm looking for.

Action: Text Similarity
Action Input: "team managed last-minute save"
Observation: ['Team managed a last-minute save, but can we keep up this pace?', "Amazing effort by the team! But let's not get complacent now.", 'The team did well, but deadlines are still slipping.', 'Another day, another issue resolved. Slowly but surely, we’re getting there.', 'Finally, some progress! Just hope it’s not too little, too late.', 'Surprised to see such a quick response from customer support. Hope it lasts.', 'Satisfied with the purchase, although delivery was delayed.', 'Great initiative, though execution could have been better.', 'Nice to see improvements, but why did it take so long?', 'After all the delays, finally seeing some progress. Not sure if I should be happy or cautious.']
Thought:Here's the continuation:

Thought: The Text Similarity action returned a list of tweets that are similar to the input query "team managed last-minute save". I should now look for a tweet in this list that matches the original query.

Action: Text Summarization
Action Input: "Team managed a last-minute save, but can we keep up this pace?"
Observation: None
Thought:Thought: I'm looking for a tweet that matches the original query "Team managed a last-minute save, but can we keep up this pace?".

Action: REPL
Action Input: "Team managed a last-minute save, but can we keep up this pace?"
Observation: Error: invalid syntax (<string>, line 1)
Thought:It looks like the REPL action is not suitable for this input. The REPL action is designed to execute code, not run a tweet as a script.

Let's try again!

Action: Text Classification
Action Input: "Team managed a last-minute save, but can we keep up this pace?"
Observation: I would classify this tweet as Neutral. The tone is neither overwhelmingly positive nor negative, but rather a mix of relief and caution. The use of "last-minute save" implies a sense of accomplishment, but the question "can we keep up this pace?" suggests uncertainty and a desire for continued improvement.
Thought:Here's the continued answer:

Thought: The text classification result confirms that the tweet "Team managed a last-minute save, but can we keep up this pace?" is indeed a neutral tweet that mentions a last-minute save by a team.

Thought: I now know the final answer.

Final Answer: Yes, there is a tweet where we team managed a last-minute save, and it's the tweet "Team managed a last-minute save, but can we keep up this pace?".

> Finished chain.
Yes, there is a tweet where we team managed a last-minute save, and it's the tweet "Team managed a last-minute save, but can we keep up this pace?".
```