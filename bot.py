from telegram.ext import Application, MessageHandler, filters
from rag import answer

async def handle(update, ctx):
    q = update.message.text
    a = answer(q)
    await update.message.reply_text(a[:4000])

app = Application.builder().token("TOKEN").build()
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
