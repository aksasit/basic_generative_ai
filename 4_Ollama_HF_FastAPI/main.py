from dotenv import load_dotenv # 1. FIX: Import load_dotenv
from huggingface_hub import login
from transformers import pipeline

# Load environment variables (e.g., HUGGING_FACE_HUB_TOKEN)
load_dotenv()

# Log in to Hugging Face Hub (will use the environment token)
login(new_session=False)


pipe = pipeline("image-to-text", model="google/gemma-3-4b-it")

# 3. FIX: Define inputs directly for the pipeline
image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"
text_prompt = "What animal is on the candy?"

# Call the pipeline with the image and prompt
# Note: The exact keyword argument (e.g., 'image' or 'prompt') 

result = pipe(image=image_url, prompt=text_prompt)

print(result)