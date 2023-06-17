import argparse
import json
from .Loader import Loader
import openai

class FinGen:
    @staticmethod
    def get_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(usage="FinGen --api-key \"<OpenAI_Api_Key>\" --title \"<Finding Title>\"", description="FinGen CLI", prog="python -m FinGen")
        parser.add_argument(
            "-t",
            "--title",
            required=True,
            action='append',
            help="Finding Title",
        )
        parser.add_argument(
            "-k",
            "--api-key",
            type=str,
            required=True,
            help="OpenAI API key",
        )
        parser.add_argument(
            "-c",
            "--company",
            type=str,
            default=None,
            help="Perspective to write finding from",
        )
        return parser

    @staticmethod
    def CreateFinding(api_key, titles, company):
        openai.api_key = api_key
        systemPrompt = "You are a penetration tester writing report findings"

        # Write it from the company perspective
        if company != None:
            systemPrompt += " for " + company

        # Set up the bot
        for title in titles:
            loader = Loader("Thinking...", "Thinking... Done!").start()
            prompt = (
                # Preamble
                "Write a finding for \"" + title + "\".\n"

                # Description Spec
                "The description section should contain enough detail to understand the finding and the risk posed to the business.\n"
                
                # implication spec
                "The implication should contain a paragraph outlining the implication of not implementing the finding and how it may impact an organisation"

                # Remediation Spec
                "The remediation should contain a paragraph outlining how to remediate the finding."

                # Risk Rating Spec
                "The risk rating is based on the likelihood and impact of exploitation following on the OWASP Risk Rating Methodology." 
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613", # or gpt-4-0613
                messages=[
                    {"role": "system", "content" : systemPrompt},
                    {"role": "user", "content": prompt}
                ],
                functions=[
                    {
                        "name": "generate_finding",
                        "description": "Compiles raw finding sections into a report",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Title for the finding"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "Description of the finding"
                                },
                                "remediation": {
                                    "type": "string",
                                    "description": "How to fix the finding"
                                },
                                "implication": {
                                    "type": "string",
                                    "description": "The business implication if the finding isn't fixed"
                                },
                                "overall_risk": {
                                    "type": "string",
                                    "enum": ["Informational", "Low", "Medium", "High", "Critical"]
                                },
                                "impact": {
                                    "type": "string",
                                    "enum": ["Insignificant", "Minor", "Moderate", "Major", "Very High"]
                                },
                                "likelihood": {
                                    "type": "string",
                                    "enum": ["Rare", "Unlikely", "Possible", "Likely", "Almost Certain"]
                                }
                            },
                            "required": ["title", "description", "remediation", "implication", "overall_risk", "impact", "likelihood"]
                        }
                    }
                ],
                function_call={"name": "generate_finding"}
            )
            output = json.loads(response.choices[0]["message"]["function_call"]["arguments"])
            loader.stop()

            print("----- Title -----")
            print(output["title"])

            print("\n----- Description -----")
            print(output["description"])

            print("\n----- Remediation -----")
            print(output["remediation"])
            
            print("\n----- Implication -----")
            print(output["implication"])

            print("\n----- Risk Rating -----")
            print(output["overall_risk"])

            print("\n----- Impact -----")
            print(output["impact"])

            print("\n----- Likelihood -----")
            print(output["likelihood"])

            print("")