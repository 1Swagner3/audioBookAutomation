import openai
import os
from dotenv import load_dotenv

def get_improved_text(query, context_data):
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    # Ensure the API key is set
    if not openai_api_key:
        raise ValueError("OpenAI API key is not set in environment variables.")

    openai.api_key = openai_api_key

    prompt = f"""
    {context_data}
    {query}
    """

    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        temperature=0.4,
        top_p=1,
        n=1,
        stop=None,  # You can set stopping tokens if necessary
        frequency_penalty=0,
        presence_penalty=0
    )

    result = response.choices[0].text.strip()
    return result

# Example usage
context_data = "Your context data here"
query = "Your query here"
improved_text = get_improved_text(query, context_data)
print(improved_text)
