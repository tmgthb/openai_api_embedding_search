!pip install git+https://github.com/openai/whisper.git
import whisper
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import os
import numpy as np
import torch
from transformers import GPT2TokenizerFast
from openai.embeddings_utils import get_embedding, cosine_similarity
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
