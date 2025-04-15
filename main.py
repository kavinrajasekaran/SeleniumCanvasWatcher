import time
import os
import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from plyer import notification

# === CONFIG ===
CANVAS_URL = "https://yourcanvas.instructure.com/courses/123456/quizzes"  # <-- Change this
CHECK_INTERVAL = 20  # Check every 20 seconds
DATA_FILE = "known_quizzes.pkl"

# === HEADLESS SELENIUM SETUP ===
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

def login_to_canvas():
    driver.get(CANVAS_URL)
    print("Please log in manually if needed...")
    input("Press Enter after logging in and the quizzes page has fully loaded...")

def get_current_quiz_titles():
    driver.get(CANVAS_URL)
    time.sleep(2)
    quiz_elements = driver.find_elements(By.CSS_SELECTOR, ".ig-title a")
    titles = [el.text.strip() for el in quiz_elements if el.text.strip()]
    return titles

def load_known_quizzes():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "rb") as f:
            return pickle.load(f)
    return []

def save_known_quizzes(titles):
    with open(DATA_FILE, "wb") as f:
        pickle.dump(titles, f)

def notify_new_quiz(title):
    print(f"[ALERT] New quiz posted: {title}")
    notification.notify(
        title="📚 New Canvas Quiz Posted!",
        message=f"{title}",
        timeout=10
    )

# === MAIN LOOP ===
login_to_canvas()
known_quizzes = load_known_quizzes()

while True:
    print("🔄 Checking for new quizzes...")
    try:
        current_quizzes = get_current_quiz_titles()
        new_quizzes = [q for q in current_quizzes if q not in known_quizzes]

        if new_quizzes:
            for quiz in new_quizzes:
                notify_new_quiz(quiz)
            known_quizzes = current_quizzes
            save_known_quizzes(known_quizzes)
        else:
            print("✅ No new quizzes.")
    except Exception as e:
        print(f"⚠️ Error during check: {e}")

    time.sleep(CHECK_INTERVAL)
