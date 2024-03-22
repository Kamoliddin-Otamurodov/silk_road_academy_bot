from telegram import Update , Contact , KeyboardButton
from telegram.ext import CallbackContext
from messages import WELCOME_MESSAGE , COURSE_MESSAGE , ENGLISH_MESSAGE , KOREAN_MESSAGE , JAPANESE_MESSAGE , ENGLISH_INFO_MESSAGE , KOREAN_INFO_MESSAGE , JAPANESE_INFO_MESSAGE
from keyboards import WELCOME_KEYBOARD , COURSE_KEYBOARD , ENGLISH_KEYBOARD , KOREAN_KEYBOARD , JAPANESE_KEYBOARD , ReplyKeyboardMarkup , CLEAR_USERS_KEYBOARD
from db import UserDB
userdb = UserDB('users.json')

# create a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboards = WELCOME_KEYBOARD

    if userdb.is_user(user.id):
        update.message.reply_html(
            text="""Assalomu alaykum yana bir bor! qaytganingizdan xursandmiz.""",
            reply_markup=keyboards
        )
        return 

    userdb.add_user(chat_id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)

    update.message.reply_html(
        text=f"""Assalomu alaykum <b>{user.full_name}</b>! 😍SILK ROAD ACADEMY😍 botiga xush kelibsiz.""",
        reply_markup=keyboards
    )

def course(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=COURSE_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=COURSE_KEYBOARD,
    )

def english(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=ENGLISH_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=ENGLISH_KEYBOARD,
    )

def japanese(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=JAPANESE_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=JAPANESE_KEYBOARD,
    )

def korean(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=KOREAN_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=KOREAN_KEYBOARD,
    )
def korean_info(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=KOREAN_INFO_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=KOREAN_KEYBOARD,
    )

def japanese_info(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=JAPANESE_INFO_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=JAPANESE_KEYBOARD,
    )

def english_info(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=ENGLISH_INFO_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=ENGLISH_KEYBOARD,
    )

def korean_write(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=KOREAN_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=KOREAN_KEYBOARD,
    )

def japanase_write(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=KOREAN_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=KOREAN_KEYBOARD,
    )

def english_write(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=KOREAN_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=KOREAN_KEYBOARD,
    )

# Define a function to handle the /get_contact command
def get_contact(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [KeyboardButton("Send Contact", request_contact=True)],
        [KeyboardButton("⬅️Qaytish")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True , resize_keyboard=True)


    update.message.reply_text(
        text='Please share your contact information by using the contact button below the chat input field.',
        parse_mode="HTML",
        reply_markup=reply_markup,
    )

# Define a function to handle contact messages
def handle_contact(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    # Get the contact information from the message
    contact_info: Contact = update.message.contact

    # Access the properties of the Contact object
    contact_name = contact_info.first_name
    contact_phone = contact_info.phone_number

    # Add the contact information to the TinyDB database
    userdb.add_contact(chat_id=user.id , first_name=contact_name , phone_number=contact_phone)

    update.message.reply_text(f'Contact received!\nName: {contact_name}\nPhone Number: {contact_phone}')

def users(update: Update, context: CallbackContext) -> None:
    """This function will be called when the user sends /users command

    Args:
        update (Update): Updater object that contains the update info.
        context (CallbackContext): Context object that contains the bot info.
    """
    # Get the first name of the user
    first_name = update.effective_user.first_name
    
    # Assuming userdb is an instance of TinyDB and contains user information
    users = userdb.get_contact()

    # Create a string template for each user
    user_template = '''name: {},
    phone_number: {}'''

    # Iterate through the users and format the string for each user
    formatted_users = []
    for user in users:
        formatted_user = user_template.format(user["first_name"], user["phone_number"])
        formatted_users.append(formatted_user)

    # Join the formatted user strings with newlines
    users_text = '\n'.join(formatted_users)

    update.message.reply_text(
        text=users_text,
        parse_mode="HTML",
        reply_markup=CLEAR_USERS_KEYBOARD,
    )

def clear_users(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name
    users = userdb.clear_contact()

    # send a message to the user
    update.message.reply_text(
        text="Toza",
        parse_mode="HTML",
        reply_markup=CLEAR_USERS_KEYBOARD,
    )