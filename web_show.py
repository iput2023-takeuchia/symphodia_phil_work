from flask import Flask, render_template
import function_pkg.data_csv as csv
import function_pkg.ambient_read as amb

app = Flask(__name__)

@app.route("/", methods=["GET"])
def display_csvdata():
    print("Hello! (to Terminal)")
    amb.get_ambient_data()
    data_csv_list = csv.csv_read_iterator()
    print("data_csv_list: ", data_csv_list)
    
    return render_template("data_show.html",  input_ambient_data=data_csv_list) 

@app.route("/update", methods=["POST"])
def reload_ambient_data():
    data_csv_list = csv.csv_read_iterator()
    print("data_csv_list: ", data_csv_list)
    
if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    app.run(host='0.0.0.0', port=5001, debug=True)