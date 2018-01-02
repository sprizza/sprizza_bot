web: python mio_bot.py --port=$ PORT
mio_bot.py:
import os
from intro_to_flask import app

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)
