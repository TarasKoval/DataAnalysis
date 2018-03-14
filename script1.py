import urllib2
import pandas as pd


def download():
    url_1 = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=Mean'
    url_2 = 'https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID={}&year1=1981&year2=2017&type=VHI_Parea'

    for counter in range(1, 28):
        url = url_1.format(counter)
        vhi_url = urllib2.urlopen(url)
        out = open(r'raw_short_data/vhi_short_id_{}.csv'.format(counter), 'wb')
        out.write(vhi_url.read())
        out.close()
        print "short {} downloaded".format(counter)

    for counter in range(1, 28):
        url = url_2.format(counter)
        vhi_url = urllib2.urlopen(url)
        out = open(r'raw_long_data/vhi_long_id_{}.csv'.format(counter), 'wb')
        out.write(vhi_url.read())
        out.close()
        print "long {} downloaded".format(counter)


def making_frames():
    renaming_list = [
        [1, 22], [2, 24], [3, 23], [4, 25], [5, 3], [6, 4], [7, 8], [8, 19], [9, 20], [10, 21],
        [11, 9], [12, 26], [13, 10], [14, 11], [15, 12], [16, 13], [17, 14], [18, 15], [19, 16],
        [20, 27], [21, 17], [22, 18], [23, 6], [24, 1], [25, 2], [26, 7], [27, 5]
    ]

    for counter in range(1, 2):
        df = pd.read_csv(r'raw_short_data/vhi_short_id_{}.csv'.format(counter),
                         skiprows=1, skipfooter=1,
                         engine='python',
                         names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'],
                         index_col=0,
                         sep='[,\s]\s*'
                         )
        if df.isnull().values.any():
            print("Df {} has empty fields".format(counter))

        df.to_csv(r"data_frames_short/data_frame_short_{}.csv".format(renaming_list[counter - 1][1]))
        print(counter)

    for counter in range(1, 1):
        df = pd.read_csv(r'raw_long_data/vhi_long_id_{}.csv'.format(counter),
                         skiprows=1, skipfooter=1,
                         engine='python',
                         names=['year', 'week', '0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50',
                                '55', '60', '65', '70', '75', '80', '85', '90', '95', '100'],
                         index_col=0,
                         sep='[,\s]\s*'
                         )
        if df.isnull().values.any():
            print("Df {} has empty fields".format(counter))

        df.to_csv(r"data_frames_long/data_frame_long_{}.csv".format(renaming_list[counter - 1][1]))
        print(counter)


def task_1(input_area, input_year):
    df = pd.read_csv('data_frames_short/data_frame_short_{}.csv'.format(input_area))

    sample = df[(df['year'] == input_year)]['VHI']

    list_sample = pd.Series.tolist(sample)
    print("Max VHI for area #{} at {} year: {}".format(input_area, input_year, max(list_sample)))
    print("Min VHI for area #{} at {} year: {}".format(input_area, input_year, min(list_sample)))


def task_2_3(input_area, percent_to_check, vhi_to_check):
    df = pd.read_csv('data_frames_long/data_frame_long_{}.csv'.format(input_area))
    sample = df.index.tolist()

    for vhi_counter in range(0, vhi_to_check + 5, 5):
        print("\n{}".format(vhi_counter))
        for counter in range(0, sample[-1]):
            percent = df[(df.index == counter)][str(vhi_counter)].tolist()
            if percent[0] > percent_to_check:
                print(
                    "{}-{} {}".format(df[(df.index == counter)]['year'].tolist()[0],
                                      df[(df.index == counter)]['week'].tolist()[0],
                                      percent[0]))


if __name__ == '__main__':
    # download()
    # making_frames()
    task_1(15, 2000)
    # task_2_3(15, 10, 5)
    # task_2_3(15, 35, 35)
