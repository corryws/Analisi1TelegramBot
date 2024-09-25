import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, CallbackQueryHandler
from telegram.ext import filters

from GeneratoreNumeriComplessi import ReturnComplexImage
from GeneratoreFunzioniIRRazionali import ReturnRationalIrrationalFunctionImage

# Imposta il logging per tracciare eventuali errori
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Funzione che risponde al comando /start con il messaggio di benvenuto
async def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    logger.info(f"Utente {user.full_name} (username: {user.username}, id: {user.id}) ha avviato il bot con /start alle {update.message.date}")
    
    welcome_message = (
        "Benvenuto su Analisi 1 Bot by CorryWestSide[STILL IN DEVELOPMENT].\n"
        "Lo scopo è quello di aiutare lo studio di Analisi 1 mediante la fornitura Teorica e di Esercizi generati randomicamente sulla base degli argomenti richiesti.\n"
        "Comandi disponibili:\n"
        "/Esercizi - Accedi agli esercizi\n"
        "/Teoria - Accedi alla teoria\n"
    )

    if update.message:  # Assicurati che il messaggio sia presente
        await update.message.reply_text(welcome_message)
    elif update.callback_query:  # Caso callback
        await update.callback_query.message.edit_text(welcome_message)

# Funzione che crea il pannello di controllo con pulsanti degli argomenti
def create_panel(tipo: str) -> InlineKeyboardMarkup:
    keyboard = [
        [InlineKeyboardButton("Insiemistica", callback_data=f"{tipo}_Insiemistica")],
        [InlineKeyboardButton("Numeri Complessi", callback_data=f"{tipo}_NumeriComplessi")],
        [InlineKeyboardButton("Successioni", callback_data=f"{tipo}_Successioni")],
        [InlineKeyboardButton("Funzioni", callback_data=f"{tipo}_Funzioni")],
        [InlineKeyboardButton("🔙 Torna al Menu", callback_data="menu_start")]  # Aggiunto pulsante per tornare al menu
    ]
    return InlineKeyboardMarkup(keyboard)

# Funzione che risponde al comando /Esercizi con il pannello di argomenti
async def esercizi(update: Update, context: CallbackContext) -> None:
    message = (
        "Seleziona uno degli Argomenti per avere un Esercizio generato randomicamente da risolvere.\n"
        "Suggerimento: Puoi sempre tornare al menu principale cliccando su 'Torna al Menu'."
    )
    keyboard = create_panel("Esercizi")
    await update.message.reply_text(message, reply_markup=keyboard)

# Funzione che risponde al comando /Teoria con il pannello di argomenti
async def teoria(update: Update, context: CallbackContext) -> None:
    message = (
        "Seleziona uno degli Argomenti per ottenere la teoria dell'argomento richiesto.\n"
        "Suggerimento: Puoi sempre tornare al menu principale cliccando su 'Torna al Menu'."
    )
    keyboard = create_panel("Teoria")
    await update.message.reply_text(message, reply_markup=keyboard)

# Funzione che gestisce la selezione del pulsante
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()  # Risponde per evitare che il bot rimanga "in attesa"

    # Gestisce il pulsante "Torna al Menu"
    if query.data == "menu_start":
        await start(update, context)  # Torna al menu principale
        return

    # Estrae il tipo e l'argomento dal callback_data
    data = query.data.split("_")
    tipo = data[0]  # Esercizi o Teoria
    argomento = data[1]  # L'argomento selezionato

    if tipo == "Esercizi":
        if argomento == "NumeriComplessi":
            # Genera l'immagine dell'esercizio sui numeri complessi
            image_path = ReturnComplexImage()  # Supponendo che ritorni il percorso del file
            # Invia l'immagine all'utente
            await query.message.reply_photo(photo=open(image_path, 'rb'))
        if argomento == "Funzioni":
            # Genera l'immagine dell'esercizio sui numeri complessi
            image_path = ReturnRationalIrrationalFunctionImage()  # Supponendo che ritorni il percorso del file
            # Invia l'immagine all'utente
            await query.message.reply_photo(photo=open(image_path, 'rb'))
        else:
            response = f"Generazione esercizio sull'argomento: {argomento}."
            await query.edit_message_text(text=response)

    elif tipo == "Teoria":
        response = f"Teoria sull'argomento: {argomento}."
        await query.edit_message_text(text=response)

# Funzione che gestisce i messaggi non riconosciuti
async def echo(update: Update, context: CallbackContext) -> None:
    # Cancella il messaggio ricevuto
    await update.message.delete()

# Funzione per gestire gli errori
async def error(update: Update, context: CallbackContext) -> None:
    logger.error(f"Errore: {context.error}")

async def set_bot_commands(application: Application) -> None:
    commands = [
        BotCommand("start", "Mostra il menu principale"),
        BotCommand("Esercizi", "Accedi agli esercizi"),
        BotCommand("Teoria", "Accedi alla teoria"),
    ]
    try:
        await application.bot.set_my_commands(commands)
    except Exception as e:
        logger.error(f"Impossibile impostare i comandi: {e}")

def main() -> None:
    # Inserisci qui il token del bot
    TOKEN = 'inserttokenhere'

    # Crea l'application e passa il token del bot
    application = Application.builder().token(TOKEN).build()

    # Definisci i comandi disponibili
    application.add_handler(CommandHandler("start", start))

    # Comandi per esercizi e teoria
    application.add_handler(CommandHandler("Esercizi", esercizi))
    application.add_handler(CommandHandler("Teoria", teoria))

    # Gestore per il pannello dei pulsanti
    application.add_handler(CallbackQueryHandler(button))

    # Risposta a tutti i messaggi di testo non riconosciuti
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Gestore di errori
    application.add_error_handler(error)

    # Imposta i comandi al momento dell'avvio
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_bot_commands(application))

    # Avvia il bot
    application.run_polling()

if __name__ == '__main__':
    main()
