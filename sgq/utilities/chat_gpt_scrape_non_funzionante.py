"key: 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"
# Questo è un progetto in bozza in quanto non è permesso effettuare lo scraping delle conversazioni in chatgpt

import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Define the function to save conversations from chat.openai.com
def save_conversations():
    url = url_entry.get()
    output_file = file_entry.get()
    output_path = f"/home/mauro/Scrivania/django_general_template2/sgq/utilities/storage/{output_file}"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the conversation elements
        conversation_elements = soup.find_all('div', class_='assistant-response')
        
        # Open the output file for writing
        with open(output_path, 'a', encoding='utf-8') as file:
            # Iterate over the conversation elements and save the content
            for conversation in conversation_elements:
                content = conversation.text.strip()
                file.write(content + '\n')
        
        status_label.configure(text=f"Saved conversations to '{output_path}'")
    else:
        status_label.configure(text="Failed to retrieve conversations.")

# Create the Tkinter window
window = tk.Tk()
window.title("Conversation Saver")
window.geometry("500x400")  # Set the size of the window (width x height)
window.configure(bg="#002300")  # Set the background color of the window
# To remember Hexadecimal color codes: "#FF0000" (red), "#00FF00" (green), 
# # "#0000FF" (blue), "#FFFF00" (yellow), "#800080" (purple), etc.

# Create URL input field
url_label = tk.Label(window, text="Conversation URL:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Create output file name input field
file_label = tk.Label(window, text="Output File Name:")
file_label.pack()
file_entry = tk.Entry(window)
file_entry.pack()

# Create save button
save_button = tk.Button(window, text="Save Conversations", command=save_conversations)
save_button.pack()

# Create status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the Tkinter event loop
window.mainloop()