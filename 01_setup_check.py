import os
from dotenv import load_dotenv
from google import genai

def main() -> None:
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY was not found. Create a .env file and add your key first."
        )
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Reply with exactly these two words: environment ready",
    )

    print("Model reply:")
    print(response.text)

    usage = getattr(response, "usage_metadata", None)
    if usage:
        prompt_tokens = getattr(usage, "prompt_token_count", "n/a")
        response_tokens = getattr(usage, "candidates_token_count", "n/a")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

if __name__ == "__main__":
    main()