import os import sqlite3 import threading import time import uuid import logging from datetime import datetime from flask import Flask, request, jsonify, render_template_string from apscheduler.schedulers.background import BackgroundScheduler

Interactive account setup

SENDER_NAME = input("Enter sender name: ").strip() or "MessageTesterBot" ADMIN_SECRET = input("Enter admin secret: ").strip() or "change_this_secret" DRY_RUN = True RATE_LIMIT_PER_MIN = 10 DATABASE = "messagetester.db"

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def init_db(): conn = sqlite3.connect(DATABASE) c = conn.cursor() c.execute('''CREATE TABLE IF NOT EXISTS consent (id TEXT PRIMARY KEY, recipient TEXT UNIQUE, name TEXT, opted_in_at TEXT)''') c.execute('''CREATE TABLE IF NOT EXISTS queue (id TEXT PRIMARY KEY, recipient TEXT, message TEXT, scheduled_at TEXT, enqueued_at TEXT)''') c.execute('''CREATE TABLE IF NOT EXISTS logs (id TEXT PRIMARY KEY, timestamp TEXT, sender TEXT, recipient TEXT, message_snippet TEXT, status TEXT, error TEXT)''') conn.commit() conn.close()

def db_execute(query, params=(), fetch=False): conn = sqlite3.connect(DATABASE) c = conn.cursor() c.execute(query, params) result = None if fetch: result = c.fetchall() conn.commit() conn.close() return result

class RateLimitedSender(threading.Thread): def init(self, per_minute=10): super().init(daemon=True) self.per_minute = per_minute self.interval = 60.0 / per_minute self._stop = threading.Event()

def stop(self):
    self._stop.set()

def run(self):
    logging.info(f"RateLimitedSender started at {self.per_minute} msgs/min")
    while not self._stop.is_set():
        rows = db_execute("SELECT id, recipient, message, scheduled_at FROM queue ORDER BY scheduled_at ASC LIMIT 1", fetch=True)
        if not rows: time.sleep(0.5); continue
        qid, recipient, message, scheduled_at = rows[0]
        scheduled_dt = datetime.fromisoformat(scheduled_at)
        if scheduled_dt > datetime.utcnow():
            time.sleep(min(1.0, (scheduled_dt - datetime.utcnow()).total_seconds())); continue
        db_execute("DELETE FROM queue WHERE id=?", (qid,))
        logging.info(f"[DRY-RUN] Would send to {recipient}: {message[:80]}")
        db_execute("INSERT INTO logs (id, timestamp, sender, recipient, message_snippet, status, error) VALUES (?, ?, ?, ?, ?, ?, ?)"
                   ,(str(uuid.uuid4()), datetime.utcnow().isoformat(), SENDER_NAME, recipient, message[:200], "sent", None))
        time.sleep(self.interval)

app = Flask(name) TEMPLATE_INDEX = """<h2>MessageTester</h2>

<p>DRY_RUN: {{ dry_run }} RateLimit: {{ rate }}</p>
<form action='/optin' method='post'>Recipient:<input name='recipient'><br>Name:<input name='name'><button type='submit'>Opt-in</button></form>
<form action='/optout' method='post'>Recipient:<input name='recipient'><button type='submit'>Opt-out</button></form>
<form action='/admin/enqueue' method='post'>
<input type='hidden' name='secret' value='{{ admin_secret }}'>Recipient:<input name='recipient'><br>Message:<textarea name='message'></textarea><br>Time ISO:<input name='scheduled_at'><button type='submit'>Enqueue</button></form>"""@app.route("/", methods=["GET"]) def index(): consented = db_execute("SELECT recipient,name,opted_in_at FROM consent ORDER BY opted_in_at DESC LIMIT 50", fetch=True) return render_template_string(TEMPLATE_INDEX, dry_run=DRY_RUN, rate=RATE_LIMIT_PER_MIN, admin_secret=ADMIN_SECRET, consented=consented)

@app.route("/optin", methods=["POST"]) def optin(): r = request.form.get("recipient","".strip()); n=request.form.get("name","".strip()) or None db_execute("INSERT OR REPLACE INTO consent (id,recipient,name,opted_in_at) VALUES (?,?,?,?)",(str(uuid.uuid4()),r,n,datetime.utcnow().isoformat())) return f"Opted in: {r}",200

@app.route("/optout", methods=["POST"]) def optout(): r = request.form.get("recipient","".strip()) db_execute("DELETE FROM consent WHERE recipient=?",(r,)) return f"Opted out: {r}",200

@app.route("/admin/enqueue", methods=["POST"]) def enqueue(): if request.form.get("secret") != ADMIN_SECRET: return "forbidden",403 r=request.form.get("recipient").strip(); m=request.form.get("message").strip(); t=request.form.get("scheduled_at","".strip()) if not db_execute("SELECT recipient FROM consent WHERE recipient=?",(r,),fetch=True): return "not opted-in",400 if not t: t=datetime.utcnow().isoformat() db_execute("INSERT INTO queue (id,recipient,message,scheduled_at,enqueued_at) VALUES (?,?,?,?,?)",(str(uuid.uuid4()),r,m,t,datetime.utcnow().isoformat())) return jsonify({"status":"enqueued"}),200

def main(): init_db() sender = RateLimitedSender(RATE_LIMIT_PER_MIN); sender.start() sched=BackgroundScheduler(); sched.start() try: app.run(host="0.0.0.0", port=5000) finally: sender.stop(); sched.shutdown()

if name=="main": main()

GitHub: K-z89

