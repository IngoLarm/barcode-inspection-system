import cv2
import time
import threading
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
from pyzbar.pyzbar import decode, ZBarSymbol

STREAM_URL = "tcp://172.18.36.75:8888"

# Zielbereich fuer den Barcode (x1, y1, x2, y2) im 1280x800-Kamerabild
ROI = (390, 310, 890, 490)

cap = cv2.VideoCapture(STREAM_URL)
latest_frame = None
scan_text = "Barcode ins Feld halten..."
scan_ok = False
lock = threading.Lock()


def grab_loop():
    global latest_frame
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            with lock:
                latest_frame = frame


def scan_loop():
    global scan_text, scan_ok
    x1, y1, x2, y2 = ROI
    while True:
        with lock:
            frame = latest_frame
        if frame is not None:
            roi = cv2.cvtColor(frame[y1:y2, x1:x2], cv2.COLOR_RGB2GRAY)
            results = decode(roi, symbols=[ZBarSymbol.I25, ZBarSymbol.EAN13])
            with lock:
                if results:
                    scan_text = " | ".join(f"{r.type}: {r.data.decode(errors='replace')}" for r in results)
                    scan_ok = True
                else:
                    scan_text = "Barcode ins Feld halten..."
                    scan_ok = False
        time.sleep(0.2)


threading.Thread(target=grab_loop, daemon=True).start()
threading.Thread(target=scan_loop, daemon=True).start()

root = tk.Tk()
root.title("Kamera Live-Ansicht - cm5-node2")
label = tk.Label(root)
label.pack()
status = tk.Label(root, text="", font=("Segoe UI", 14, "bold"))
status.pack(pady=5)


def update():
    with lock:
        frame = latest_frame
        text = scan_text
        ok = scan_ok
    if frame is not None:
        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)
        draw.rectangle(ROI, outline=(0, 255, 0) if ok else (255, 0, 0), width=4)
        tkimg = ImageTk.PhotoImage(img)
        label.imgtk = tkimg
        label.configure(image=tkimg)
    status.configure(text=text, fg="green" if ok else "red")
    root.after(15, update)


update()
root.mainloop()
cap.release()
