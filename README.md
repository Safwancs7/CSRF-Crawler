# CSRF Vulnerability Scanner and Proof of Concept

## 1. Overview

This project demonstrates a **Cross-Site Request Forgery (CSRF)** vulnerability along with a custom-built **Python crawler** that scans a web application for missing CSRF protection.

CSRF attacks occur when a user’s authenticated browser is tricked into sending an unwanted request to a trusted website. This happens because the browser **automatically includes session cookies**, and the server does not verify the request using a CSRF token.

This project demonstrates:

- How CSRF attacks work
- How vulnerable applications behave
- How missing CSRF tokens can be detected
- How attackers can exploit this weakness

---

## 2. How CSRF Protection Works

Modern frameworks prevent CSRF using **CSRF tokens**.

1. Server generates a unique, random token
2. Token is inserted into a form as a **hidden input**
3. When the form is submitted, the server verifies the token
4. If the token is missing or invalid → the request is rejected

Examples:

| Framework | Protection |
|----------|-----------|
| Django | `CsrfViewMiddleware` + `{% csrf_token %}` |
| Express.js | `csurf` middleware |
| ASP.NET Core | Anti-forgery tokens |
| Laravel | `@csrf` directive |

Other protections include:

- SameSite cookies
- Re-authentication for sensitive actions
- Confirmation dialogs

---

## 3. CSRF Vulnerability Crawler (Python)

This repository contains a Python script that crawls a target website and detects **forms that are missing CSRF tokens**.

### Files in this repository
## 🔗 Live CSRF Demo (Web Version)

The vulnerable banking application and the attacker page are live here:

https://safwancs7.github.io/CSRF_Demo/

A fake transaction will be triggered automatically.  
This demonstrates a successful **CSRF attack**.

---

## 📁 CSRF Demo Repository (HTML Source Code)

The HTML files for the demo are stored in this GitHub repository:

https://github.com/Safwancs7/CSRF_Demo.git

This repository contains:

- `index.html` → Vulnerable banking page (NO CSRF protection) + Auto-submitting CSRF attack page

---

## ✅ Final Notes

- Python Crawler → This repository ✅
- CSRF Demo → Linked above ✅
- Live Demo → Linked above ✅

This completes the CSRF research + crawler + PoC requirements.

---

## Disclaimer

This project is for **educational and authorized testing only**.  
Do NOT use this on systems that you do not own or have permission to test.

## 🚀 How to Run the CSRF Crawler

1. Clone this repository:

```bash
git clone https://github.com/Safwancs7/CSRF_Crawler.git
```

Install the required libraries:
```bash
pip install -r requirements.txt
```

Run the crawler:
```bash
python csrf_crawler.py
```



