import pandas as pd
import time
import numpy as np


# full dataset you can download from
# https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption

def making_frame():
    start_time = time.time()
    df = pd.read_csv('household_power_consumption.txt', sep=';', low_memory=False, index_col=0)
    print("{} sec to read file".format(time.time() - start_time))

    start_time = time.time()
    df = df.dropna(how='any')
    print("{} sec to delete empty fields".format(time.time() - start_time))

    start_time = time.time()
    df.to_csv('lab_3_main_df.csv')
    print("{} sec to record csv".format(time.time() - start_time))


def panda_task_1(df):
    sample_1 = df[(df['Global_active_power'] > 5)]
    return sample_1


def panda_task_2(df):
    sample_1 = df[(df['Voltage'] > 235)]
    return sample_1


def panda_task_3(df):
    sample_1 = df[
        (df['Global_intensity'] > 19) & (df['Global_intensity'] < 20) & (df['Sub_metering_2'] > df['Sub_metering_3'])]
    return sample_1


def panda_task_4(df):
    sample_1 = df.sample(n=500, random_state=5, replace=False)

    sample_sub_metering_1 = pd.Series.tolist(sample_1['Sub_metering_1'])
    sample_sub_metering_2 = pd.Series.tolist(sample_1['Sub_metering_2'])
    sample_sub_metering_3 = pd.Series.tolist(sample_1['Sub_metering_3'])

    avg_sub_metering_1 = np.mean(sample_sub_metering_1)
    avg_sub_metering_2 = np.mean(sample_sub_metering_2)
    avg_sub_metering_3 = np.mean(sample_sub_metering_3)

    avg = [avg_sub_metering_1, avg_sub_metering_2, avg_sub_metering_3]
    return avg


def panda_task_5(df):
    sample_1 = df.sample(n=500, random_state=5, replace=False)
    sample_1 = sample_1[(sample_1['Time'] > '18:00:00')
                        & (sample_1['Global_active_power'] > 6)
                        & (sample_1['Sub_metering_2'] > sample_1['Sub_metering_1'])
                        & (sample_1['Sub_metering_2'] > sample_1['Sub_metering_3'])]

    sample_1 = sample_1.reset_index(drop=True)

    sample_first_half = sample_1[(sample_1.index < len(sample_1.index) / 2)]
    sample_first_half = sample_first_half.iloc[::3, :]

    sample_second_half = sample_1[(sample_1.index > len(sample_1.index) / 2)]
    sample_second_half = sample_second_half.iloc[::4, :]

    result_df = pd.concat([sample_first_half, sample_second_half], ignore_index=True)
    return result_df


def num_task_1():
    answer = np.array([])
    data = np.loadtxt('lab_3_small_part_of_df.csv', skiprows=1, dtype='str', delimiter=',')
    for counter in range(len(data)):
        if float(data[counter][2]) > 6:
            answer = np.append(answer, data[counter])
    answer = np.vstack(answer)

    print answer


def num_task_2():
    answer = np.array([])
    data = np.loadtxt('lab_3_small_part_of_df.csv', skiprows=1, dtype='str', delimiter=',')
    for counter in range(len(data)):
        if float(data[counter][4]) > 235:
            answer = np.append(answer, data[counter])
    answer = np.vstack(answer)

    print answer


def num_task_3():
    answer = np.array([])
    data = np.loadtxt('lab_3_small_part_of_df.csv', skiprows=1, dtype='str', delimiter=',')
    for counter in range(len(data)):
        if (float(data[counter][5]) > 19) and (float(data[counter][5]) < 20) and (
                    float(data[counter][7]) > float(data[counter][8])):
            answer = np.append(answer, data[counter])
    answer = np.vstack(answer)

    print answer


def num_task_4():
    data_col_6 = np.array([])
    data_col_7 = np.array([])
    data_col_8 = np.array([])

    print 'start load'
    start_time_def = time.time()
    data = np.loadtxt('lab_3_small_part_of_df.csv', skiprows=1, dtype='str', delimiter=',')
    print("end load in {} sec".format(time.time() - start_time_def))

    print 'start random'
    start_time_def = time.time()
    data = data[np.random.choice(data.shape[0], 500, replace=False), :]
    print("end random in {} sec".format(time.time() - start_time_def))

    print 'start looking for value 1,2,3'
    start_time_def = time.time()
    for counter in range(len(data)):
        if (float(data[counter][5]) > 19) and (float(data[counter][5]) < 20) and (
                    float(data[counter][7]) > float(data[counter][8])):
            data_col_6 = np.append(data_col_6, float(data[counter][6]))
            data_col_7 = np.append(data_col_7, float(data[counter][7]))
            data_col_8 = np.append(data_col_8, float(data[counter][8]))
    print("end looking for value 1,2,3 in {} sec".format(time.time() - start_time_def))

    print 'start making average'
    start_time_def = time.time()
    avg_data_col_6 = np.mean(data_col_6)
    avg_data_col_7 = np.mean(data_col_7)
    avg_data_col_8 = np.mean(data_col_8)
    print("end making average in {} sec".format(time.time() - start_time_def))

    print avg_data_col_6
    print avg_data_col_7
    print avg_data_col_8


def num_task_5():
    answer = np.array([])
    data = np.loadtxt('lab_3_small_part_of_df.csv', skiprows=1, dtype='str', delimiter=',')
    data = data[np.random.choice(data.shape[0], 500, replace=False), :]
    print 'end loading'
    for counter in range(len(data)):
        if data[counter][1] > '18:00:00' and float(data[counter][7]) > float(data[counter][6]) and \
                        float(data[counter][7]) > float(data[counter][8]):
            answer = np.append(answer, data[counter])
    answer = np.vstack(answer)

    print answer


if __name__ == '__main__':
    # making_frame()
    start_time = time.time()

    df = pd.read_csv('lab_3_small_part_of_df.csv')

    df_1 = panda_task_1(df)
    print("{} sec".format(time.time() - start_time))
    print df_1.head()
    print len(df_1.index)
