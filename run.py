from app import my_app
my_app.run(debug=True)
my_app.config["CACHE_TYPE"] = "null"