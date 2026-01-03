# Day 4 — Local Language Health SMS Message Formatter (Nigeria & Africa)

## Overview
- **Goal:** Format raw health messages into clear, respectful, SMS-ready text tailored for Nigerian/African audiences.
- **Audience:** Community health workers, clinics/NGOs, public health educators, telemedicine startups, government campaigns.
- **Why it matters:** SMS remains the most reliable channel; better wording increases compliance, trust, and can save lives.

## Context
- Many citizens use feature phones and have limited data.
- Health messages are often poorly phrased, not localized, and exceed 160 characters.
- This tool helps clean, personalize, adapt tone (English → simple Nigerian Pidgin rules), and enforce SMS limits.

## Core Features (Pure Python)
- **Clean input:** Trim whitespace using `strip()`.
- **Tone adaptation:** Simple rule-based Pidgin substitution via `replace()`.
- **Personalization:** Add recipient name with f-strings.
- **Length enforcement:** Truncate to 160 characters (adds `...` when needed).

## File
- Main script: [Day4_Local_Language_Health_SMS_Message_Formatter/local_language_health_sms_message_formatter.py](Day4_Local_Language_Health_SMS_Message_Formatter/local_language_health_sms_message_formatter.py)

## Usage
1. Run the script and provide inputs when prompted.
2. Example (PowerShell):
   ```powershell
   cd C:\Project\30DaysOfPythonProjects\Day4_Local_Language_Health_SMS_Message_Formatter
   python .\local_language_health_sms_message_formatter.py
   ```
3. Input:
   - Name: `Aisha`
   - Message: `remember to take your malaria drugs every day`

### Expected Output
```
Final SMS:
Hello Aisha, no forget to take your malaria drugs every day
Message Length: 62 characters
```

## How It Works (Logic Flow)
- Read inputs: `Name` and `Message`.
- Clean: `clean_message = raw_message.strip()`.
- Tone change before formatting:
  - Convert to lowercase and apply exact phrase replacement: 
    - `pidgin_body = clean_message.lower().replace("remember to take your malaria drugs every day", "no forget to take your malaria drugs every day")`
- Personalize: `final_message = f"Hello {recipient_name}, {pidgin_body}"`.
- Enforce SMS length: if `len(final_message) > 160`, keep first 157 chars and append `...`.

## Debugging Notes (What Went Wrong and Fixes)
- **Issue: `replace()` didnt trigger**
  - Cause: The original code used `.capitalize()` which changed `remember` → `Remember`, so the lowercase match failed.
  - Fix: Remove `.capitalize()`; use `.lower()` before `.replace()` to ensure consistent matching.

- **Issue: Replacing the entire message**
  - Cause: Attempted `personalized_message.replace(clean_message, ...)` after greeting was added, which risks replacing the wrong substring or too broadly.
  - Fix: Perform replacement on the **body** first (before adding greeting), then compose the final message.

- **Issue: Off-by-one in length expectation**
  - Observation: `Hello Aisha, no forget to take your malaria drugs every day` is 59 characters, not 60.
  - Tip: If you need exactly 60 for a demo, append a period (`.`).

## Lessons Learned
- **Exact-match behavior:** `str.replace()` requires exact substring matches.
- **Case sensitivity matters:** Normalize case with `.lower()` when matching phrases.
- **Order of operations:** Apply transformations to the body before adding greetings.
- **String hygiene:** Use `.strip()` to avoid accidental leading/trailing spaces.
- **Length control:** Always measure `len()` and enforce your SMS cap.
- **Clarity first:** Small, respectful wording changes can significantly improve comprehension.

## Future Improvements
- Case-insensitive matching without `.lower()` (e.g., regex) while preserving original casing.
- Support additional health prompts (antenatal reminders, immunization, water hygiene).
- Multi-language rules: Hausa-influenced English or other local variants.
- Configurable templates and tone settings.
- Basic tests for common phrases and SMS limit behavior.

## Try It Quickly
- Run the script, then input the sample phrase to see the Pidgin transformation.
- Adjust the message to exceed 160 chars to verify truncation.
