# SkillBond APK
### Personal Skill-Based Friend Finder — Android App
Built with **Kivy 2.3.0 + KivyMD 2.0.1** | Python 3.10.11 | Pillow latest | Local SQLite

---

## 📱 What's in this App

| Feature | Detail |
|---|---|
| Multi-user | Login & Sign Up — each user's data is private |
| Add Friends | Name, Phone, Location, Skills, Notes |
| Live Search | Type to filter by name — results appear instantly |
| Autocomplete | Skill & Location fields show live suggestions while typing |
| Quick Skills | Tap chips to add common skills in one click |
| View Details | Tap any friend card to see full info |
| Edit / Delete | Manage friends easily |
| Offline | All data stored on-device using SQLite — no internet needed |
| Dark Modern UI | Cyan accent, dark cards, matching the website design |

---

## 🚀 Option A — Run on PC First (Test Before Building APK)

### Step 1 — Install Python 3.10+
https://www.python.org/downloads/

### Step 2 — Install dependencies
```bash
pip install kivy==2.3.0 kivymd==2.0.1 pillow
```

### Step 3 — Run the app
```bash
python main.py
```

This opens the app in a desktop window so you can test everything.

---

## 📦 Option B — Build the APK (on Linux / WSL / GitHub Actions)

### Prerequisites (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
pip install buildozer cython
```

### Build the APK
```bash
cd skillbond_apk/
buildozer android debug
```

First build takes ~15–30 minutes (downloads Android SDK/NDK).

After build, find your APK at:
```
bin/skillbond-1.0-arm64-v8a_armeabi-v7a-debug.apk
```

Transfer to your phone and install!

---

## 🌐 Option C — Build Online for Free (No Linux Needed)

Use **GitHub Actions** to build the APK in the cloud:

1. Create a GitHub repo
2. Upload all files in this folder
3. Create `.github/workflows/build.yml`:

```yaml
name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: buildozer android debug
      - uses: actions/upload-artifact@v3
        with:
          name: skillbond-apk
          path: bin/*.apk
```

4. Push → GitHub builds the APK → Download from the Actions tab.

---

## 📁 File Structure
```
skillbond_apk/
├── main.py          ← Full app (screens, logic, autocomplete)
├── db.py            ← SQLite database layer
├── buildozer.spec   ← APK build configuration
└── README.md        ← This file
```

---

## 🔤 Bengali Font (Optional)
To show Bengali text properly in the app:
1. Download **Hind Siliguri** or **Noto Sans Bengali** font (.ttf)
2. Place the .ttf file in the project folder
3. In main.py, add this after `Builder.load_string(KV)`:
```python
from kivy.core.text import LabelBase
LabelBase.register(name='HindSiliguri', fn_regular='HindSiliguri-Regular.ttf')
```
4. Use `font_name: 'HindSiliguri'` in KV where you want Bengali text.

---

## 🔑 Notes
- Database is stored at: `/data/data/com.skillbond/files/skillbond.db` on Android
- Passwords are hashed with SHA-256 + random salt (secure, not reversible)
- No internet connection needed — 100% offline
- To reset the app data on Android: Settings → Apps → SkillBond → Clear Data
