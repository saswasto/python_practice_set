import pyperclip

# Define the text you want to copy
text_to_copy = "This is a test text for pyperclip."

# Copy the text to the clipboard
pyperclip.copy(text_to_copy)

# Retrieve the text from the clipboard
pasted_text = pyperclip.paste()

# Check if the copied text matches the pasted text
if text_to_copy == pasted_text:
    print("Test Passed: The text was copied successfully!")
else:
    print("Test Failed: The copied text does not match the original.")

print("Copied text:", pasted_text)
