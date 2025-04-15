# SeleniumCanvasWatcher

SeleniumCanvasWatcher is a lightweight Python web scraper that monitors your Canvas course's Quizzes page and alerts you when a new quiz drops — so you can skip class without missing pop quizzes.

---

## Features

- Headless scraping with Selenium
- Desktop notifications for new quizzes
- Remembers previously seen quizzes (local .pkl file)
- Auto-checks every 20 seconds (configurable)
- Works on any Canvas course with manual login once

---

## Setup

1. Clone the Repository

    git clone https://github.com/yourusername/SeleniumCanvasWatcher.git
    cd SeleniumCanvasWatcher

2. Set Up Virtual Environment (optional but recommended)

    python3 -m venv venv
    source venv/bin/activate      # macOS/Linux
    venv\Scripts\activate         # Windows

3. Install Requirements

    pip3 install selenium plyer

    You must also download ChromeDriver from https://chromedriver.chromium.org/downloads that matches your installed Chrome version and put it in your PATH or the project folder.

---

## Usage

1. Edit the Canvas URL

    In `canvas_quizwatcher.py`, change the following line:

    CANVAS_URL = "https://yourcanvas.instructure.com/courses/123456/quizzes"

    Replace it with your course’s actual Quizzes page URL.

2. Run the Script

    python3 canvas_quizwatcher.py

    On first run, you'll be prompted to log in manually in the browser window. The script will then check for new quizzes every 20 seconds and notify you.

---

## Notes

- Canvas login session is preserved across runs
- Quiz titles are stored in known_quizzes.pkl
- Check interval is configurable by editing CHECK_INTERVAL

---

## Example Output

    🔄 Checking for new quizzes...
    ✅ No new quizzes.
    [ALERT] New quiz posted: Midterm Review Quiz

---

## Future Improvements

- Email/SMS/Discord webhook support
- Background system tray app
- Auto-login using cookies (experimental)

---

## License

MIT License. Use at your own risk — your professor doesn’t need to know 😎

---

## Credits

Created by [Your Name]  
Built with Selenium and Plyer
