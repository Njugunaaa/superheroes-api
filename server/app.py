from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "<h1>Hero API</h1>", 200

@app.route('/heroes', methods=["GET"])
def get_heroes():
  heroes=[]

  for hero in Hero.query.all():
      heroes.append(hero.to_dict())
  return make_response(heroes, 200)

@app.route('/heroes/<int:id>', methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return make_response(hero.to_dict(), 200)
    return make_response({"error": "Hero not found"}, 404)

@app.route('/powers', methods=["GET"])
def get_powers():
    powers = [power.to_dict() for power in Power.query.all()]
    return make_response(powers, 200)

@app.route('/powers/<int:id>', methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return make_response(power.to_dict(), 200)
    return make_response({"error": "Power not found"}, 404)

@app.route('/powers/<int:id>', methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    
    if not power:
        return {"error": "Power not found"}, 404

    data = request.get_json()
    description = data.get("description")

    if not description or len(description) < 10:
        return {"errors": ["validation errors"]}, 400

    power.description = description
    db.session.commit()

    return {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }, 200


@app.route('/hero_powers', methods=["POST"])
def add_hero_power():
    data = request.get_json()
    new_hero_power = HeroPower(
        strength=data.get("strength"),
        hero_id=data.get("hero_id"),
        power_id=data.get("power_id")
    )
    db.session.add(new_hero_power)
    db.session.commit()
    new_hero_dict=new_hero_power.to_dict()
    return make_response(new_hero_dict, 201)



if __name__ == '__main__':
    app.run(port=5555, debug=True)
