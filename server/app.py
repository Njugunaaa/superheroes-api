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
    return "<h1>Welcome To My Hero API</h1>", 200

##GET METHODS

@app.route('/heroes', methods=["GET"])
def get_heroes():
  heroes=[]

  for hero in Hero.query.all():
      heroes.append(hero.to_dict())

  return make_response(heroes, 200)


@app.route('/powers', methods=["GET"])
def get_powers():
    powers=[]

    for power in Power.query.all():
        powers.append(power.to_dict()) 

    return make_response(powers, 200)


@app.route('/heroes/<int:id>', methods=["GET"])
def get_hero(id):

    hero = Hero.query.get(id)
    if hero:
        return make_response(hero.to_dict(), 200)
    
    return make_response({"error": "Hero has  not found"}, 404)


@app.route('/powers/<int:id>', methods=["GET"])
def get_power(id):

    power = Power.query.get(id)

    if power:
        return make_response(power.to_dict(), 200)
    
    return make_response({"error": "Power was not found"}, 404)


##PATCH-- UPDATE METHODS


@app.route('/powers/<int:id>', methods=["PATCH"])
def update_power(id):
    power = Power.query.get(id)
    #validation if power exists
    if not power:
        return {"error": "Power was not found"}, 404

    data = request.get_json()

    description = data.get("description")

    #validation check to confirm the appropriate length

    if not description or len(description) < 20:
        return {"errors": ["MAke the description have at least 20 characters long"]}, 400

    power.description = description
    db.session.commit()

    return {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }, 200


##POST-- CREATE NEW METHODS


@app.route('/hero_powers', methods=["POST"])
def add_hero_power():

    data = request.get_json()

    
    strength=data.get("strength")
    hero_id=data.get("hero_id")
    power_id=data.get("power_id")
    

    #validation check to confirm the level of strength

    strengths=["Strong", "Weak", "Average"]
    if strength not in strengths:
        return { "errors": ["Strength must be 'Strong', 'Weak', or 'Average'"] }, 400

    new_hero_power = HeroPower(
        strength=strength,
        hero_id=hero_id,
        power_id=power_id
    )
    db.session.add(new_hero_power)
    db.session.commit()
    
    new_hero_dict=new_hero_power.to_dict()
    return make_response(new_hero_dict, 201)



if __name__ == '__main__':
    app.run(port=5555, debug=True)


