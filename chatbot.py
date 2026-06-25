from groq import Groq

client = Groq(api_key="YOUR_GROQ_API_KEY")

print("===== Automated Copywriting & Tone Transformer =====")

product = input("Enter Product Name: ")
platform = input("Enter Platform (LinkedIn/Instagram/Email): ")
tone = input("Enter Tone (Professional/Friendly/Creative): ")

prompt = f"""
Create a marketing copy.

Product: {product}
Platform: {platform}
Tone: {tone}

Generate engaging promotional content.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nGenerated Content:\n")
print(response.choices[0].message.content)