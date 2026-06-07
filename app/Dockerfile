# בחירת תמונת הבסיס - פייתון
FROM python:3.9-slim

# הגדרת תיקיית העבודה בתוך הקונטיינר
WORKDIR /app

# העתקת קובץ הדרישות והתקנת הספריות
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# העתקת שאר הקוד
COPY . .

# הגדרת הפורט שהאפליקציה מאזינה לו
EXPOSE 5000

# הפקודה שמריצה את האפליקציה
CMD ["python", "app.py"]