#!/usr/bin/python3
from argparse import ArgumentParser, Action
import google.generativeai as genai
from IPython.display import Markdown
from textwrap import indent
from json import load
from os import path
from re import sub


CONFIG_PATH = "./askgem.config"

try:
    CONFIG = dict(load(open(CONFIG_PATH)))
except FileNotFoundError:
    pass

args, chat = [None for _ in range(2)]


def main():
    global chat, args

    args = parse_args()
    
    if not args.action == "config":
        setup_model()
        
    actions = {
        None: askgem, 
        "list": list_models, 
        "config": config
    }
        
    return actions[args.action]()


def askgem():
    you = CONFIG.get("you", ">>> ")
    gemeni = CONFIG.get("gemeni", "")

    if args.save_file:
        youInFile = CONFIG.get("youInFile", CONFIG.get("you", ">>> "))
        gemeniInFile = CONFIG.get("gemeniInFile", CONFIG.get("gemeni", "<<< "))
    while True:
        if args.question:
            text = " ".join(args.question)
            args.question = None
        else:
            text = input(you)
            print()
        if text.lower().strip() == CONFIG.get("exit", "exit"):
            return
        response = to_markdown(chat.send_message(text).text).data
        print(gemeni, response)
        if args.save_file:
            with open(args.save_file, "a") as f:
                f.write(f"{youInFile} {text}\n\n{gemeniInFile} {response}\n\n")
        print("")

        if args.non_interactive:
            return


def list_models():
    for model in genai.list_models():
        print(model.name)


def config():
    file = path.abspath(__file__)
    with open(file, "r") as f:
        new = sub('\nCONFIG_PATH = ".+"\n', f'\nCONFIG_PATH = "{args.config_path}"\n', f.read(), 1)
        
    with open(file, 'w') as f:
        f.write(new)


def setup_model():
    global chat
    genai.configure(api_key=CONFIG["key"])
    
    model = genai.GenerativeModel(CONFIG.get("model", "gemini-1.0-pro-latest"))

    chat = model.start_chat(history=[])

def parse_args():
    parser = ArgumentParser(description="Ask gemeni from the command line")
    parser.add_argument(
        "-q",
        "--question",
        help="Ask gemeni one question from command line directly",
        type=str,
        nargs="+",
        metavar="",
    )
    parser.add_argument(
        "-n",
        "--non-interactive",
        action="store_true",
        help="Don't initiate an interactive chat session and close after the first request",
    )
    parser.add_argument(
        "-s", "--save-file", metavar="", help="Save the chat history to a file"
    )
    parser.add_argument(
        "-l",
        "--list-models",
        help="List gemeni models there",
        const="list",
        action="store_const",
        dest="action",
    )
    parser.add_argument(
        "-c",
        "--config-path",
        metavar="",
        help="set the path for the config file",
        dest="action",
        action=ConfigAction,
    )
    parser.add_argument(
        "-qn",
        "--question-non-interactive",
        help="-questoin and --non-interactive at the same time",
        metavar='',
        action=qnAction,
        nargs='+'
    )

    return parser.parse_args()


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(indent(text, "", predicate=lambda _: True))


class ConfigAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, "config")
        namespace.config_path = values

class qnAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        namespace.question = str(values)
        namespace.non_interactive = True


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("\n")