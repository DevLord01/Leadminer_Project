import os
os.system("python scraper.py")
os.system("python clean.py")
os.system("python load_db.py")
print("Pipeline completed")
