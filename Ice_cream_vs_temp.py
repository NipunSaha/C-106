import csv
import plotly.express as px
import numpy as np

def plot_fig(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Temperature",y="Ice-cream Sales")
        fig.show()

def get_data_source(data_path):
    temp = []
    ice_cream_sales = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            temp.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
    return {
        "x": temp,
        "y": ice_cream_sales
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Temperature and Ice cream sales are ",correlation)

def main():
    file_name = "temperatureVsIce-cream.csv"
    plot_fig(file_name)
    data_source = get_data_source(file_name)
    find_correlation(data_source)

main()