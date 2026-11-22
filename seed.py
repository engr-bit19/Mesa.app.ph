"""Creates the MySQL database 'mesa', its tables, and sample recipes.
Needs XAMPP's MySQL running. Run once: python seed.py"""
import pymysql

HOST, USER, PASSWORD = "localhost", "root", ""   # XAMPP defaults

CATEGORY = {
    "Chicken thighs": "Meat", "Pork belly": "Meat", "Pork blood": "Meat",
    "Pork liver": "Meat", "Beef chuck": "Meat", "Beef brisket": "Meat",
    "Beef sirloin": "Meat", "Beef shank": "Meat",
    "Shrimp": "Seafood", "Milkfish": "Seafood", "Squid": "Seafood",
    "Egg": "Dairy & eggs", "Condensed milk": "Dairy & eggs",
    "Evaporated milk": "Dairy & eggs", "Coconut milk": "Dairy & eggs",
    "Soy sauce": "Pantry", "Vinegar": "Pantry", "Tamarind mix": "Pantry",
    "Cooking oil": "Pantry", "Rice": "Pantry", "Canton noodles": "Pantry",
    "Bihon noodles": "Pantry", "Miki noodles": "Pantry", "Sotanghon noodles": "Pantry",
    "Bay leaves": "Pantry", "Fish sauce": "Pantry", "Peppercorns": "Pantry",
    "Tomato sauce": "Pantry", "Liver spread": "Pantry", "Sugar": "Pantry",
    "Brown sugar": "Pantry", "Star anise": "Pantry", "Annatto oil": "Pantry",
    "Glutinous rice flour": "Pantry", "Tapioca pearls": "Pantry",
    "Lumpia wrapper": "Pantry", "Shaved ice": "Pantry", "Sweet beans": "Pantry",
    "Ube halaya": "Pantry"
}

RECIPES = [
 ("Chicken adobo", "#8a4b2d", 55, 4, ["chicken", "rice meal"],
  [("Chicken thighs", 800, "g"), ("Soy sauce", 60, "ml"), ("Vinegar", 60, "ml"), ("Garlic", 6, "cloves"), ("Bay leaves", 3, "pcs")]),
 ("Sinigang na baboy", "#4d7a3a", 70, 4, ["pork", "soup"],
  [("Pork belly", 600, "g"), ("Tamarind mix", 1, "pack"), ("Kangkong", 1, "bunch"), ("Tomato", 2, "pcs"), ("Onion", 1, "pcs")]),
 ("Tortang talong", "#6b4c8a", 20, 2, ["vegetarian", "under 30 min"],
  [("Eggplant", 3, "pcs"), ("Egg", 3, "pcs"), ("Onion", 1, "pcs"), ("Cooking oil", 30, "ml")]),
 ("Arroz caldo", "#b5832a", 45, 4, ["chicken", "soup"],
  [("Chicken thighs", 500, "g"), ("Rice", 200, "g"), ("Garlic", 5, "cloves"), ("Ginger", 30, "g"), ("Egg", 2, "pcs")]),
 ("Garlic rice & egg", "#2f6f86", 15, 2, ["vegetarian", "under 30 min", "rice meal"],
  [("Rice", 300, "g"), ("Garlic", 4, "cloves"), ("Egg", 2, "pcs"), ("Cooking oil", 20, "ml")]),
 ("Pancit canton", "#a8453a", 30, 4, ["pork", "noodles"],
  [("Canton noodles", 250, "g"), ("Pork belly", 200, "g"), ("Carrot", 1, "pcs"), ("Onion", 1, "pcs"), ("Soy sauce", 30, "ml")]),
 ("Dinuguan", "#3d2b35", 60, 4, ["pork", "rice meal"],
  [("Pork belly", 600, "g"), ("Pork blood", 250, "ml"), ("Vinegar", 80, "ml"), ("Garlic", 5, "cloves"), ("Onion", 1, "pcs"), ("Green chili", 3, "pcs"), ("Bay leaves", 2, "pcs")]),
 ("Nilagang baboy", "#3a6b5c", 75, 4, ["pork", "soup"],
  [("Pork belly", 700, "g"), ("Potato", 2, "pcs"), ("Cabbage", 1, "head"), ("Pechay", 1, "bunch"), ("Onion", 1, "pcs"), ("Fish sauce", 30, "ml"), ("Peppercorns", 1, "tsp")]),
 ("Beef caldereta", "#9e3b24", 80, 4, ["beef", "rice meal"],
  [("Beef chuck", 700, "g"), ("Tomato sauce", 200, "ml"), ("Liver spread", 85, "g"), ("Potato", 2, "pcs"), ("Carrot", 1, "pcs"), ("Bell pepper", 1, "pcs"), ("Garlic", 4, "cloves")]),
 ("Sinigang na hipon", "#2b7a78", 35, 4, ["seafood", "soup"],
  [("Shrimp", 500, "g"), ("Tamarind mix", 1, "pack"), ("Kangkong", 1, "bunch"), ("Radish", 1, "pcs"), ("Tomato", 2, "pcs"), ("Onion", 1, "pcs")]),
 ("Leche flan", "#c98a2c", 45, 6, ["dessert"],
  [("Egg", 10, "pcs"), ("Condensed milk", 300, "ml"), ("Evaporated milk", 370, "ml"), ("Sugar", 100, "g")]),

 # --- More Noodles ---
 ("Pancit bihon", "#b86b35", 30, 4, ["chicken", "noodles"],
  [("Bihon noodles", 250, "g"), ("Chicken thighs", 250, "g"), ("Cabbage", 1, "head"), ("Carrot", 1, "pcs"), ("Soy sauce", 45, "ml"), ("Garlic", 4, "cloves")]),
 ("La Paz batchoy", "#7a442a", 60, 4, ["pork", "noodles", "soup"],
  [("Miki noodles", 300, "g"), ("Pork belly", 300, "g"), ("Pork liver", 150, "g"), ("Egg", 2, "pcs"), ("Garlic", 5, "cloves"), ("Spring onion", 2, "stalks")]),
 ("Sotanghon guisado", "#c47d3b", 35, 4, ["chicken", "noodles"],
  [("Sotanghon noodles", 200, "g"), ("Chicken thighs", 250, "g"), ("Carrot", 1, "pcs"), ("Annatto oil", 30, "ml"), ("Garlic", 4, "cloves"), ("Fish sauce", 15, "ml")]),

 # --- More Seafood ---
 ("Ginataang hipon", "#c96d2d", 25, 4, ["seafood", "under 30 min", "rice meal"],
  [("Shrimp", 500, "g"), ("Coconut milk", 400, "ml"), ("Squash", 200, "g"), ("String beans", 100, "g"), ("Ginger", 20, "g"), ("Garlic", 4, "cloves")]),
 ("Daing na bangus", "#35687a", 25, 4, ["seafood", "under 30 min", "rice meal"],
  [("Milkfish", 600, "g"), ("Vinegar", 80, "ml"), ("Garlic", 6, "cloves"), ("Peppercorns", 1, "tsp"), ("Cooking oil", 60, "ml")]),
 ("Adobong pusit", "#3a2e47", 30, 4, ["seafood", "rice meal"],
  [("Squid", 600, "g"), ("Soy sauce", 45, "ml"), ("Vinegar", 45, "ml"), ("Tomato", 2, "pcs"), ("Onion", 1, "pcs"), ("Garlic", 5, "cloves")]),

 # --- More Beef ---
 ("Beef pares", "#6e3226", 90, 4, ["beef", "rice meal"],
  [("Beef brisket", 750, "g"), ("Soy sauce", 60, "ml"), ("Brown sugar", 45, "g"), ("Star anise", 3, "pcs"), ("Ginger", 25, "g"), ("Garlic", 5, "cloves")]),
 ("Bistek tagalog", "#7d3c28", 35, 4, ["beef", "rice meal"],
  [("Beef sirloin", 600, "g"), ("Soy sauce", 60, "ml"), ("Calamansi", 6, "pcs"), ("Onion", 2, "pcs"), ("Garlic", 4, "cloves"), ("Cooking oil", 30, "ml")]),
 ("Bulalo", "#4a6b53", 120, 6, ["beef", "soup"],
  [("Beef shank", 1000, "g"), ("Corn", 2, "pcs"), ("Cabbage", 1, "head"), ("Pechay", 1, "bunch"), ("Onion", 1, "pcs"), ("Fish sauce", 30, "ml"), ("Peppercorns", 1, "tsp")]),

 # --- More Dessert ---
 ("Halo-halo", "#8a4b7d", 15, 2, ["dessert", "under 30 min"],
  [("Shaved ice", 400, "g"), ("Evaporated milk", 120, "ml"), ("Sweet beans", 100, "g"), ("Ube halaya", 60, "g"), ("Sugar", 30, "g")]),
 ("Ginataang bilo-bilo", "#9e6b43", 40, 4, ["dessert"],
  [("Glutinous rice flour", 200, "g"), ("Coconut milk", 400, "ml"), ("Sweet potato", 1, "pcs"), ("Saba banana", 3, "pcs"), ("Tapioca pearls", 80, "g"), ("Sugar", 100, "g")]),
 ("Turon", "#b87a28", 20, 4, ["dessert", "under 30 min"],
  [("Saba banana", 4, "pcs"), ("Lumpia wrapper", 8, "pcs"), ("Brown sugar", 80, "g"), ("Jackfruit", 60, "g"), ("Cooking oil", 100, "ml")]),
]

SCHEMA = [
 "DROP TABLE IF EXISTS plan_entries",
 "DROP TABLE IF EXISTS recipe_tags",
 "DROP TABLE IF EXISTS recipe_ingredients",
 "DROP TABLE IF EXISTS tags",
 "DROP TABLE IF EXISTS ingredients",
 "DROP TABLE IF EXISTS recipes",
 """CREATE TABLE recipes (
      id INT AUTO_INCREMENT PRIMARY KEY,
      title VARCHAR(100) NOT NULL,
      color VARCHAR(7) NOT NULL DEFAULT '#1f4d43',
      minutes INT NOT NULL,
      servings INT NOT NULL)""",
 """CREATE TABLE ingredients (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100) NOT NULL UNIQUE,
      category VARCHAR(50) NOT NULL DEFAULT 'Produce')""",
 """CREATE TABLE recipe_ingredients (
      recipe_id INT NOT NULL,
      ingredient_id INT NOT NULL,
      quantity DOUBLE NOT NULL,
      unit VARCHAR(20) NOT NULL,
      PRIMARY KEY (recipe_id, ingredient_id),
      FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
      FOREIGN KEY (ingredient_id) REFERENCES ingredients(id))""",
 """CREATE TABLE tags (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(50) NOT NULL UNIQUE)""",
 """CREATE TABLE recipe_tags (
      recipe_id INT NOT NULL,
      tag_id INT NOT NULL,
      PRIMARY KEY (recipe_id, tag_id),
      FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE,
      FOREIGN KEY (tag_id) REFERENCES tags(id))""",
 """CREATE TABLE plan_entries (
      day ENUM('Mon','Tue','Wed','Thu','Fri','Sat','Sun') NOT NULL,
      meal ENUM('Breakfast','Lunch','Dinner') NOT NULL,
      recipe_id INT NOT NULL,
      PRIMARY KEY (day, meal),
      FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE)""",
]

con = pymysql.connect(host=HOST, user=USER, password=PASSWORD)
cur = con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS mesa CHARACTER SET utf8mb4")
cur.execute("USE mesa")
for stmt in SCHEMA:
    cur.execute(stmt)

for title, color, mins, serv, tags, ings in RECIPES:
    cur.execute("INSERT INTO recipes(title,color,minutes,servings) VALUES (%s,%s,%s,%s)",
                (title, color, mins, serv))
    rid = cur.lastrowid
    for t in tags:
        cur.execute("INSERT IGNORE INTO tags(name) VALUES (%s)", (t,))
        cur.execute("SELECT id FROM tags WHERE name=%s", (t,))
        cur.execute("INSERT INTO recipe_tags VALUES (%s,%s)", (rid, cur.fetchone()[0]))
    for name, qty, unit in ings:
        cur.execute("INSERT IGNORE INTO ingredients(name,category) VALUES (%s,%s)",
                    (name, CATEGORY.get(name, "Produce")))
        cur.execute("SELECT id FROM ingredients WHERE name=%s", (name,))
        cur.execute("INSERT INTO recipe_ingredients VALUES (%s,%s,%s,%s)",
                    (rid, cur.fetchone()[0], qty, unit))

con.commit()
con.close()
print("Created MySQL database 'mesa' with", len(RECIPES), "recipes")