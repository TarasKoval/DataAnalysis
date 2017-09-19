from spyre import server
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

indexes_list = [{"label": 'SMN', "value": 'SMN'},
                {"label": 'SMT', "value": 'SMT'},
                {"label": 'VCI', "value": 'VCI'},
                {"label": 'TCI', "value": 'TCI'},
                {"label": 'VHI', "value": 'VHI'}]
area_list = []
year_list = []

for counter in range(1, 28):
    area_list.append({"label": counter, "value": counter})

for counter in range(1981, 2018):
    year_list.append({"label": counter, "value": counter})


class StockExample(server.App):
    title = "Data"

    inputs = [{"input_type": 'dropdown',
               "label": 'Year',
               "options": year_list,
               "variable_name": 'year_number',
               "action_id": "update_data"},
              {"input_type": 'dropdown',
               "label": 'Area',
               "options": area_list,
               "variable_name": 'area_number',
               "action_id": "update_data"},
              {"type": 'dropdown',
               "label": 'Check index to show',
               "options": indexes_list,
               "variable_name": 'index_names',
               "action_id": "update_data"},
              ]

    controls = [{"control_type": "hidden",
                 "label": "get data for area",
                 "control_id": "update_data"}]

    tabs = ["Plot", "Table"]

    outputs = [{"output_type": "plot",
                "output_id": "plot",
                "control_id": "update_data",
                "tab": "Plot",
                "on_page_load": True},
               {"output_type": "table",
                "output_id": "table_id",
                "control_id": "update_data",
                "tab": "Table",
                "on_page_load": True}]

    def getData(self, params):
        area_number = params['area_number']
        year_number = params['year_number']
        df = pd.read_csv('data_frames_short/data_frame_short_{}.csv'.format(int(area_number)))
        df = df[(df['year'] == int(year_number))]
        df = df.set_index('year')
        return df

    def getPlot(self, params):
        df = self.getData(params)
        index_names = params['index_names']
        plt.figure(0)
        x1 = df["week"].tolist()
        y1 = df[index_names].tolist()
        plt.plot(x1, y1)
        return plt.figure(0)


app = StockExample()
app.launch(port=9094)
