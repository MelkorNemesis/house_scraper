from quart import Quart, jsonify, render_template
from services.houses import houses_find_all, houses_empty

import scraper

app = Quart(__name__)


@app.route('/')
def index():
    return jsonify('Hello world')


@app.route('/houses')
def houses_get_html():
    houses = list(houses_find_all())
    return render_template('houses.html', houses=houses)


@app.route('/api/houses', methods=["GET"])
def houses_get():
    houses = houses_find_all()

    for house in houses:
        if '_id' in house:
            del house['_id']

    return jsonify({"data": houses, "status": "OK"})


@app.route('/api/houses', methods=['DELETE'])
def houses_delete():
    houses_empty()
    return jsonify({"status": "OK"})


@app.route('/api/houses/scrape', methods=["POST"])
async def scrape():
    await scraper.scrape()
    return jsonify({"status": "OK"})


app.run(debug=True, use_reloader=True)
