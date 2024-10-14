import spacy

# Load the trained NER model
model_path = "D:/(NER) model for the identification of mountain names/output_model"  # Update this if your model is saved in a different path

nlp = spacy.load(model_path)

# Read the text from the file
with open("D:/(NER) model for the identification of mountain names/mountain_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text with the loaded NER model
doc = nlp(text)

# Output the detected entities
print(f"{'Entity Text':<30} | {'Start':<6} | {'End':<6} | {'Label':<10}")
print("-" * 60)
for ent in doc.ents:
    print(f"{ent.text:<30} | {ent.start_char:<6} | {ent.end_char:<6} | {ent.label_:<10}")

# Save the results to a file
with open("D:/(NER) model for the identification of mountain names/entities_output.txt", "w", encoding="utf-8") as out_file:
    for ent in doc.ents:
        out_file.write(f"Text: {ent.text}, Start: {ent.start_char}, End: {ent.end_char}, Label: {ent.label_}\n")

# Format the text with entities in bold (**entity**)
formatted_text = text
offset = 0  # This compensates for index shifting due to adding '**'

for ent in doc.ents:
    start = ent.start_char + offset
    end = ent.end_char + offset
    formatted_text = formatted_text[:start] + '**' + formatted_text[start:end] + '**' + formatted_text[end:]
    offset += 4  # Adding 4 characters because '**' is added before and after the entity

# Print the formatted text with entities in bold
print("\nFormatted text with entities highlighted:")
print(formatted_text)