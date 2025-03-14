from app import app
from app.scheduler import run_scheduler
import threading

if __name__ == "__main__":
    # Run Flask API
    threading.Thread(target=run_scheduler, daemon=True).start()
    app.run(debug=True, port=5000)
