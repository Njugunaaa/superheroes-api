## Superheroes API
Author Gichuhi Joshua Njuguna Phase 3 - Moringa School 
****Flask PRoject****
Incase of any ISsues  contact 
joshuangich2@gmail.com
## Description
Superheroes API is a flask based app that manages superheroes and their respective powers and you can be able to acces the secific endpoints individually on their own

It allows users to:

Viewing all superheroes and powers

Assigning powers to heroes with different strength levels

Editing power descriptions

Validating data before saving

The project uses Flask , Sqlalchemy among other services enjoyyyy......

## Folder Structure 
superheroes-api/
├── app.py
├── models.py
├── config.py
├── seed.py
├── server/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── migrations/
├── requirements.txt
└── README.md


yaml Copy Edit

## Technologies Used
Python 3.8.13

Flask

Flask-SQLAlchemy

Flask-Migrate (Alembic)

Marshmallow (optional, for serialization/validation)

SQLite (or PostgreSQL if upgraded)


## How to Run the App
Clone the repository:

bash
Copy
Edit
git clone https://github.com/superheroes-api/superheroes-api.git
cd superheroes-api
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
On Windows: venv\Scripts\activate

***Install dependencies:***

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
flask db upgrade
Seed the database (optional mine was provided for ):

bash
Copy
Edit
python seed.py
Start the development server:

bash
Copy
Edit
flask run

## Features
 Features
=> View all heroes and their powers

=> Assign powers to heroes via POST /hero_powers

=> Validate power strength: only "Strong", "Weak", or "Average" accepted

=> Edit a power's description with validation (PATCH /powers/<id>)

=> Handle errors gracefully (e.g., missing fields, invalid strength)

## API Endpoints available
Method	Endpoint	Description
GET	/heroes	List all heroes
GET	/powers	List all powers
GET	/heroes/<id>	Get hero with powers
POST	/hero_powers	Assign power to hero
PATCH	/powers/<id>	Update power description



## License
This application is released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
