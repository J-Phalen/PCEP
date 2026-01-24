import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(message)s")


def get_int_input(prompt: str) -> int:
    """
    Function to validate user input is a digit.
    """
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        else:
            logger.error("Please enter a digit as experience, not a word.")


def get_user_input() -> dict:
    """
    Function to capture user's data that will be saved to a dictionary.
    """
    userData = {}
    logger.info("Welcome to the PCEP course, please answer the following questions to tell us about yourself.")
    userData["name"] = input("1. What is your name?\n")
    userData["job"] = input("2. What kind of work do you do (or want to do)?\n")
    userData["goal"] = input("3. Why are you learning Python?\n")
    userData["company"] = input("4. Where are you working right now?\n")
    userData["experience"] = get_int_input("5. How many years of tech experience do you have?\n")
    userData["pyexperience"] = get_int_input("6. How many years, if any, of Python Programming do you have?\n")

    return userData


def create_badge() -> dict:
    """
    Function to create a badge for a user with data returned by the getUserinput function.
    """
    userData = get_user_input()

    logger.info("Python Learner Badge")
    logger.info("-" * 30)
    logger.info(f"Name: {userData.get('name')}")
    logger.info(f"Job: {userData.get('job')}")
    logger.info(f"Goal: {userData.get('goal')}")
    logger.info(f"Technical Experience: {userData.get('experience')} years")
    logger.info(f"Programming Experience: {userData.get('pyexperience')} years")

    # text is a variable declared as a multiline strings
    # comprised of f strings to stay under the 141 character per line limit needed for pep8 compliance.
    text = (
        f"{userData.get('name')} - {userData.get('job')}\n"
        f"Goal: {userData.get('goal')}\n"
        f"Experience: {userData.get('experience')} years\n"
        f"Programming Experience: {userData.get('pyexperience')} years\n"
    )

    badgeFile = Path("badge.txt")
    if not badgeFile.exists():
        Path(badgeFile).write_text(text)
        logger.info("Badge saved to badge.txt")
    else:
        logger.warning("Warning: A badge file already exists")
        while True:
            overwrite = input("Would you like to overwrite the existing file? (Y/n)\n")
            if str(overwrite).lower() in ["y", "yes"]:
                badgeFile.write_text(text)  # This will overwrite any existing data in the file.
                break
            elif str(overwrite).lower() in ["n", "no"]:
                logger.info("The program will now exit as the badge already exists.")
                raise SystemExit
            else:
                logger.info("Please answer only yes or no.")

    return userData


# Main program execution starts here.
badge = create_badge()
pyexp = badge.get("pyexperience")

# Since 0 is falsey pyexp needs to be check if not None as opposed to just "if pyexp:"
if pyexp is not None:
    if pyexp == 0:
        logger.info("Welcome! You're starting fresh.")
    elif pyexp < 3:
        logger.info("You're off to a great start.")
    elif pyexp < 20:
        logger.info("You deserve a pat on the back for your hard work!")
    else:
        logger.info("Great! You bring experience to the table.")

badgeFile = Path("./badge.txt")

if badgeFile.exists():
    with open(badgeFile, "r") as file:
        content = file.read()
        logger.info("Here is what you saved:")
        logger.info(content)
