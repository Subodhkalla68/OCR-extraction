client = OpenAI(api_key="OPENAI API KEY")
import pytesseract
from PIL import Image


# 1. Perform OCR on your image
image = Image.open("/Users/subodhkalla/Desktop/PDF_Text_Extractor/pdf_images/page_6.png")
extracted_text = pytesseract.image_to_string(image)

# 2. Construct a detailed prompt for GPT-4 Turbo
messages = [
    {
        "role": "system",
        "content": "You are an assistant that formats text extracted from images."
    },
    {
        "role": "user",
        "content": (
            "Here is the text extracted via Tesseract OCR:\n\n"
            f"{extracted_text}\n\n"
            "Please **format** this text into a neat table (or any structure) if possible, "
            "and make it more readable. For any sections that don't fit a table, "
            "summarize them in a clean paragraph."
        )
    }
]

# 3. Send to GPT-4 Turbo
response = client.chat.completions.create(model="gpt-4-turbo",
messages=messages,
max_tokens=500)

# 4. Print the formatted output
formatted_output = response.choices[0].message.content
print(formatted_output)