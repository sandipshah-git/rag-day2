
import os
from google import genai

# Step 1: Check API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing!")

# Step 2: Connect to Gemini
client = genai.Client(api_key=api_key)

# Step 3: Send a simple request
response = client.interactions.create(
    model="gemini-4-hydrogen",
    input="Introduce yourself in two simple sentences."
)

# Step 4: Display Gemini's response
print("\n===== GEMINI RESPONSE =====")
print(response.output_text)
