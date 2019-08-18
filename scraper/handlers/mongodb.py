from datetime import datetime
from scraper.helpers import log
from connectors import mongodb_client
import re

db = mongodb_client.houses_scraper
estates = db.estates


def _estate_name_normalize(name):
    return re.sub(r'^prodej', 'Prodej', name)


def handle_mongodb(estate, on_new_estate=None):
    log("Processing: {}, {}, {}".format(estate.name, estate.locality, estate.price))

    record = estates.find_one({"link": {"$eq": estate.link}})

    if record is None:
        data = {
            "name": _estate_name_normalize(estate.name),
            "link": estate.link,
            "locality": estate.locality,
            "price": estate.price,
            "images": estate.images,
            "created_at": datetime.utcnow(),
            "last_checked_at": None,
            "is_stale": False,
            "is_user_hidden": False,
            "history": []
        }
        estates.insert_one(data)

        if on_new_estate:
            on_new_estate(data)

    else:
        new_history = {}
        changed = {}

        # has price changed
        if record['price'] != estate.price:
            new_history['price'] = {"old": record['price'], "new": estate.price}
            changed['price'] = estate.price

        # has anything been added to new_history
        if len(new_history):
            new_history['updated_at'] = datetime.utcnow()
            changed['history'] = record['history']
            changed['history'].append(new_history)

        estates.update_one({
            '_id': record['_id']
        }, {
            '$set': {
                'last_checked_at': datetime.utcnow(),
                **changed
            }
        })
