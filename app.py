from logger import *

from config import *
from parser import *
from archive import *
from email_service import *
from api import *

def main():

    logger.info("Fetching announcements...")

    data = fetch_announcements(OPSYD_API_POSTS_URI)

    archive = load_archive(ARCHIVE_FILE)

    updated_archive = set(archive)

    new_items = []

    for item in data:

        post_date = sanitize_date(item["AnnouncementStringDate"])
        post_description = sanitize_html(item["Description"])
        uid = generate_hash(post_date,post_description)

        if uid not in updated_archive:

            new_items.append({"date": post_date, "description": post_description})
            updated_archive.add(uid)

    update_archive(ARCHIVE_FILE, updated_archive)

    if new_items:

        send_email(subject="Νέες Ανακοινώσεις ΟΠΣΥΔ", items=new_items)
        logger.info(f"Found {len(new_items)} new announcements, e-mail was sent")

    else:
        logger.info("No new announcements found")

if __name__ == "__main__":
    main()