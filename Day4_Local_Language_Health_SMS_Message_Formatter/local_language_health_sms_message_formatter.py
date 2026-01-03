# Accept Raw Inputs
recipient_name = input("Name: ")
raw_message = input("Message: ")

# Clean the Message 
clean_message = raw_message.strip()

# Nigeria-Friendly Tone Adjustment (replace before formatting)
pidgin_body = clean_message.lower().replace(
    "remember to take your malaria drugs every day",
    "no forget to take your malaria drugs every day"
)

# Personalize with f-Strings
final_message = f"Hello {recipient_name}, {pidgin_body}"

# Enforce SMS Length
if len(final_message) > 160:
    final_message = final_message[:157] + "..."

# Display Final Message
print("\n----- Local Language Health SMS Message Formatter -----\n")
print("Final SMS:")
print(final_message)
print(f"Message Length: {len(final_message)} characters")
print("\n")