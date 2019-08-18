from connectors.mongodb import mongodb_client
from pymongo import DESCENDING, ASCENDING
from datetime import datetime
import timeago

_ONE_HOUR = 3600
_CHECK_TRESHOLD = _ONE_HOUR * 2


def houses_find_all():
    db = mongodb_client.houses_scraper
    collection = db.estates
    estates_found = list(collection.find({}).sort([("is_stale", ASCENDING), ("created_at", DESCENDING)]))
    now_utc = datetime.utcnow()

    for estate in estates_found:
        last_checked_at_diff_seconds = 0

        if estate['last_checked_at']:
            last_checked_at_diff_seconds = (now_utc - estate['last_checked_at']).total_seconds()

        if last_checked_at_diff_seconds > _CHECK_TRESHOLD:
            collection.update_one({
                '_id': estate['_id']
            }, {
                '$set': {
                    'is_stale': True
                }
            })

        estate['created_ago'] = timeago.format(estate['created_at'], now_utc)

        if estate['last_checked_at']:
            estate['last_checked_ago'] = timeago.format(estate['last_checked_at'], now_utc)
        else:
            estate['last_checked_ago'] = estate['created_ago']

    return estates_found


def houses_empty():
    db = mongodb_client.houses_scraper
    db.estates.drop()
