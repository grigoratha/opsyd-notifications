# OPSYD Notifications

Lightweight service to fetch the latest announcements from OPSYD and notify the specified mailing list

Python-based automation service that runs scheduled tasks via GitHub Actions
designed to process data and send e-mail notifications based on the logic defined in the application.
This implementation probes OPSYD.gr for announcements, archives them generating unique hashes
and triggers e-mail notifications to an e-mail list if new announcements are discovered

---

# CD/CI

This project is designed to run both locally and in CI (GitHub Actions). 
Is is a lightweight backend automation runner that executes periodic notification tasks without requiring a dedicated server.
It can be used to automate notifications, email processing, or other scheduled tasks defined in the application logic.

---

# Requirements

* Windows
* Python 3.10+

---

# Installation

## Clone repository

```bash
git clone <repository_url>
cd OPSYD
```

## Install dependencies

```bash
pip install -r requirements.txt
```

---

# License

MIT License

