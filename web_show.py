from flask import Flask, render_template
import function_pkg.data_csv as data_csv

app = Flask(__name__)

@app.route("/", methods=["GET"])
def display_csvdata():
    print("Hello! (to Terminal)")

    data_csv_list = data_csv.csv_read_iterator()
    print("data_csv_list: ", data_csv_list)
    
    return render_template("data_show.html",  input_ambient_data=data_csv_list) 

@app.route("/update", methods=["POST"])
def display_csvdata():
    

    data_csv_list = data_csv.csv_read_iterator()
    print("data_csv_list: ", data_csv_list)
    
    return 
if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    app.run(host='0.0.0.0', port=5001, debug=True)