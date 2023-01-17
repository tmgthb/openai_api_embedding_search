# Podcast search with OpenAI API
This repository code performs effective text search on audio transcriptions following four steps:

## Audio-file search:
1. Code for converting podcast (an mp3 file) into transcription using OpenAI's Whisper model.
2. Text embeddings are generated for each sentence in the transcription & the user query using OpenAI's "Embedding"-endpoint.
3. The query is correlated against the sentence text embeddings by retrieving the most correlated information.
4. The most relevant information is summarized with prompt-engineering to user query with "Text completion"-endpoint

## API costs:
- The total token consumption is approximately 0.025 USD per audio using "text-embedding-ada-002" (0.0004 USD/1k tokens) and "text-davinci-003" (0.02USD/1k tokens), which are the best ones available.
- The total consumption of Embedding endpoint depends mainly on audio file length. The sample 1h audio podcast is 8k tokens and the search query only 9 tokens / query.
- The total consumption of "Text completion"-endpoint depends upon number of searches. Single search is ~1.1k tokens (prompt: ~800 tokens, completion: ~300 tokens) per each search.


## How to reduce cost?
- I found the performance of "text-davinci-003" and "text-curie-001" very similar on most queries, while dropping cost per query: from ~0.025USD/query, down to ~0.002USD/query.
- The "prompt engineering" is important, but it can be used as a source of saving costs. 

## What costs are not counted?
- The code uses local vector database stored as csv, but alternative solutions (Weavite, Pinecone etc) typically price products based on vector dimensions, rather than per search query. Limited sized text strings may not even require vector database due to short text strings consuming only few tokens. Then it is better to query the text embeddings from scratch each time.
