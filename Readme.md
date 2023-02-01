# FinGen - Penetration Testing Findings Generator
FinGen is a ChatGPT based findings generator to help save penetration testers time and provide more readable findings.

It generates findings with the following properties:
- Description
- Remediation
- Risk Rating (With Likelihood + Impact)
- _Sometimes_ extra helpful info like a risk rating justification
> **_NOTE:_**  It generally gives accurate findings but make sure to verify and add context in a real report.

## Quick Start
You just need 2 things to run it:
- An API key from OpenAI (https://platform.openai.com/account/api-keys)
- A finding title

```
git clone https://github.com/Stratus-Security/FinGen
cd FinGen
pip3 install revChatGPT
python3 FindingsGenerator.py --api_key "<api_key>" --title "Auto Complete Not Disabled"
```

## Usage
Generate a single finding
```
python3 FindingsGenerator.py --api_key "<api_key>" --title "Auto Complete Not Disabled" 
```

We can also generate multiple findings at once
```
python3 FindingsGenerator.py --api_key "<api_key>" --title "Auto Complete Not Disabled" --title "Blind SQL Injection" --title "Reflected Cross-Site Scripting" 
```

## Demo
![Demo GIF](demo.gif)

## Requests
If you want any features added feel free to open an issue or PR!