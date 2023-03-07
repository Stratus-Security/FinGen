import argparse
import os
from .Loader import Loader
import os
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
        systemPrompt = "You are a penetration tester writing a report"

        # Write it from the company perspective
        if company != None:
            systemPrompt += " for " + company

        # Set up the bot
        for title in titles:
            loader = Loader("Thinking...", "Thinking... Done!").start()
            prompt = (
                # Preamble
                "Write a finding for \"" + title + "\".\n"
                "It should contain a description, remediation, and overall risk rating. Nothing else.\n"

                # Description Spec
                "The description section should contain enough detail to understand the finding and the risk posed to the business.\n"

                # Remediation Spec
                "The remediation should contain a paragraph outlining how to remediate the finding."
                "If multiple steps are required, they can be listed too.\n"

                # Risk Rating Spec
                "The risk rating is based on the likelihood and impact of exploitation following on the OWASP Risk Rating Methodology.\n" 
                "Risk rating section should be displayed in the format: ```Risk: <insert overall risk>\nImpact: <insert impact>\nLikelihood: <insert likelihood of exploitation>```\n"
                "The overall risk can be \"Informational\", \"Low\", \"Medium\", \"High\", or \"Critical\".\n"
                "The impact can be \"Insignificant\", \"Minor\", \"Moderate\", \"Major\", or \"Very High\".\n"
                "The likelihood can be \"Rare\", \"Unlikely\", \"Possible\", \"Likely\", or \"Almost Certain\".\n"
            )

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content" : systemPrompt},
                    {"role": "user", "content": prompt}
                ]
            )
            message = completion.choices[0].message.content
            loader.stop()
            print(message)
            print("")