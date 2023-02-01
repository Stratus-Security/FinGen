import argparse
import os
from .Loader import Loader
from revChatGPT.Official import Chatbot

class FinGen:
    @staticmethod
    def get_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(usage="FinGen --api_key \"<OpenAI_Api_Key>\" --title \"<Finding Title>\"", description="FinGen CLI", prog="python -m FinGen")
        parser.add_argument(
            "-t",
            "--title",
            required=True,
            action='append',
            help="Finding Title",
        )
        parser.add_argument(
            "-k",
            "--api_key",
            type=str,
            required=True,
            help="OpenAI API key",
        )
        return parser

    @staticmethod
    def CreateFinding(api_key, titles):
        # Set base prompt - will only give very short responses otherwise
        os.environ["CUSTOM_BASE_PROMPT"] = "You are ChatGPT, a large language model trained by OpenAI.\n"

        # Set up the bot
        chatbot = Chatbot(api_key=api_key)

        for title in titles:
            loader = Loader("Thinking...", "Thinking... Done!").start()
            prompt = (
                # Preamble
                "Write me a penetration testing finding titled \"" + title + "\".\n"
                "It should contain a description, remediation, and overall risk rating.\n"

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

                # Final thoughts
                "Nicely format the sections for me."
            )
            message = chatbot.ask(prompt)
            loader.stop()
            print(message["choices"][0]["text"])
            print("")