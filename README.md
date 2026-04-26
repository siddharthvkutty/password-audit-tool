# 🔐 Password Audit Tool

A CLI-based password strength analyzer that goes beyond simple rules by simulating real-world attack strategies.

---

## 🚀 Overview

This project evaluates password strength using a combination of:

* Entropy estimation
* Pattern detection (sequences, keyboard patterns, etc.)
* Dictionary matching
* Leet (l33t) substitution detection
* Common suffix/prefix recognition
* Attack simulation via guess estimation

Instead of only checking complexity, the tool answers a more realistic question:

> **"How long would it take an attacker to crack this password?"**

---

## ⚙️ Features

* 🔢 **Entropy-based scoring**
* 🧠 **Pattern-aware analysis**
* 📚 **Dictionary and common password detection**
* 🔁 **Leet substitution recognition** (e.g., `@ → a`, `0 → o`)
* 🔚 **Common suffix detection** (`123`, `@123`, etc.)
* ⚔️ **Attack simulation**

  * Online attacks (rate-limited)
  * CPU-based attacks
  * GPU attacks
  * Advanced cluster attacks
* ⏱️ **Crack time estimation**
* 💬 **Human-readable feedback**

---

## 🏗️ Project Structure

```
password-audit-tool/
│
├── main.py
├── analyzer/
│   ├── entropy.py
│   ├── patterns.py
│   ├── scorer.py
│   └── feedback.py
│
├── data/
│   ├── common_passwords.txt
│   └── common_suffixes.txt
│
├── utils/
│   └── helpers.py
```

---

## ▶️ Usage

```bash
python -m main "your_password_here"
```

### Example

```bash
python -m main "Password123!"
```

Output:

```
=== Password Audit ===
Password: Password123!
Score: 6/10

Issues:
- Contains sequence
- Common suffix pattern
- Weak numeric pattern

Estimated Crack Time:
- GPU: instant
- Advanced cluster: instant
```

---

## 🧠 How It Works

The tool uses a hybrid model:

### 1. Entropy Estimation

Calculates theoretical randomness based on length and character set.

### 2. Pattern Detection

Identifies predictable structures such as:

* Sequences (`1234`)
* Dictionary words
* Leet substitutions
* Common suffixes

### 3. Guess Estimation

Instead of brute-force assumptions, the tool estimates how attackers actually operate:

* Wordlists + mutation rules
* Common transformations
* Early vs late guess ordering

---

## ⚠️ Limitations

* Uses simplified models (not as advanced as tools like zxcvbn)
* Dataset size is limited (for performance)
* Does not account for all real-world attack optimizations

---

## 🔮 Future Improvements

* Prefix + suffix chaining detection
* Smarter dictionary segmentation
* Frequency-based word ranking
* Rule-based attack simulation engine
* Web UI / dashboard

---

## 🛠️ Tech Stack

* Python 3
* Standard library (no heavy dependencies)

---

## 📌 Why This Project?

Most password checkers rely on simplistic rules. This tool aims to model **real attacker behavior**, making its analysis more practical and educational.

---

## 📜 License

MIT (or choose your preferred license)

---

## 👤 Author

Siddharth
Computer Science Student

---

