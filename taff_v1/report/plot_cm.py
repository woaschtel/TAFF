"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
from settings import settingsTaff

from time import localtime

# sensorName = ["n1", "n2", "n3"]
# sensorMax = [4, 4, 4]
# sensorValue = [1, 5, 3]
# sensorDiff = []

# for maxi, val in zip(sensorMax, sensorValue):
#     sensorDiff.append(maxi - val)


class plot_cm():
    def __init__(self, CM_ID, sensorName, sensorValue, sensorMax, sensorDiff,
                 SAVE_FIGURE="no",
                 SAVE_FIGURE_NAME="plotCm"):
        """


        """
        self.__cmId = CM_ID
        self.__sensorName = sensorName
        self.__sensorValue = sensorValue
        self.__sensorMax = sensorMax
        self.__sensorDiff = sensorDiff
        self.__plt = plt

        #
        #

        for i in range(len(self.__sensorDiff)):
            if self.__sensorDiff[i] < 0:
                self.__sensorDiff[i] = 0

        for i in range(len(self.__sensorValue)):
            self.__sensorValue[i] = int(self.__sensorValue[i])

        #
        # figure fuer das figure 1
        self.__plt.figure(1, figsize=(18, 11))
        # erstellen des figures
        self.__createFigure_sensorValue()
        # ausrichtien der subplots
        self.__plt.subplots_adjust(left=0.06, bottom=0.24, right=0.83, top=0.96,
                                   wspace=0, hspace=0.27)

        lt = localtime()

        datetime_str = "{:04}{:02}{:02}{:02}{:02}{:02}".format(
            lt.tm_year, lt.tm_mon, lt.tm_mday, lt.tm_hour, lt.tm_min, lt.tm_sec)

        if(SAVE_FIGURE == "no"):
            print("INFO: no pic generated")
        elif(SAVE_FIGURE == "yes"):
            txt = "{}{}_id{}_{}_{}.png".format(settingsTaff.PLOT_CM_FOLDER,
                                            SAVE_FIGURE_NAME,
                                            self.__cmId,
                                            datetime_str,
                                            1)
            self.__plt.savefig(txt)

        #
        # figure fuer das figure 2
        self.__plt.figure(2, figsize=(18, 11))
        # erstellen des figures
        self.__createFigure_allAmbient()
        # ausrichtien der subplots
        self.__plt.subplots_adjust(left=0.05, bottom=0.05, right=0.98, top=0.96,
                                   wspace=0.13, hspace=0.18)

        if(SAVE_FIGURE == "no"):
            print("INFO: no pic generated")
        elif(SAVE_FIGURE == "yes"):
            txt = "{}{}_id{}_{}_{}.png".format(settingsTaff.PLOT_CM_FOLDER,
                                                 SAVE_FIGURE_NAME,
                                                 self.__cmId,
                                                 datetime_str,
                                                 2)
            self.__plt.savefig(txt)

    def show(self):
        self.__plt.show()

    def __createFigure_sensorValue(self):
        """

        """

        self.__plt.subplot(211)

        bar_width = 0.4
        x = np.arange(len(self.__sensorName))
        opcacity = 0.5

        self.__plt.bar(x,
                       self.__sensorValue,
                       bar_width,
                       color='red',
                       label='sensorValue',
                       alpha=opcacity)

        self.__plt.bar(x,
                       self.__sensorDiff,
                       bar_width,
                       color='#2029B2',
                       label='sensorDiff',
                       alpha=opcacity,
                       bottom=self.__sensorValue)

        self.__plt.bar(x + bar_width,
                       self.__sensorMax,
                       bar_width,
                       color='#776F67',
                       label='sensorMax',
                       alpha=opcacity)

        self.__plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        self.__plt.ylabel('temperature [°C]')
        self.__plt.title(
            'Climatic Measurement ID[{}] sensor values'.format(self.__cmId))

        #
        # Erstellen des Tabels

        # columns names generieren
        column_name_list = []
        for i in range(len(self.__sensorName)):
            column_name_list.append("s{}".format(i))

        # row list erstellen
        row_name_list = ["max", "val", "diff"]

        table_data_list = []
        table_data_list.append(self.__sensorMax)
        table_data_list.append(self.__sensorValue)
        table_data_list.append(self.__sensorDiff)
        print()
        print("DEBUG: print table_data_list")
        print()
        print(table_data_list)
        print()

        self.__plt.table(cellText=table_data_list,
                         rowLabels=row_name_list,
                         colLabels=column_name_list,
                         loc='bottom')

        self.__plt.xticks([])

        """
        Plot 2 Configuration

        """
        self.__plt.subplot(212)

        value_perc = []
        new_value = []
        new_diff = []
        new_max = []

        for i in range(len(self.__sensorValue)):

            try:
                value_perc.append(
                    self.__sensorValue[i] / self.__sensorMax[i] * 100)
            except:
                value_perc.append(0)
            new_value.append(100 / 100 * value_perc[i])
            new_diff.append(100 - new_value[i])
            new_max.append(new_value[i] + new_diff[i])

        str_form1 = " {:8.2f} |" * 6
        str_form2 = " {:8} |" * 6

        print(str_form2.format("perc",
                               "sensVal",
                               "new val",
                               "sensMax",
                               "new max",
                               "new diff"))

        for i in range(len(new_value)):
            print(str_form1.format(float(value_perc[i]),
                                   float(self.__sensorValue[i]),
                                   float(new_value[i]),
                                   float(self.__sensorMax[i]),
                                   float(new_max[i]),
                                   float(new_diff[i])))

        bar_width = 0.4
        x = np.arange(len(self.__sensorName))
        opcacity = 0.5

        self.__plt.bar(x,
                       new_value,
                       bar_width,
                       color='red',
                       label='sensorValue',
                       alpha=opcacity)

        self.__plt.bar(x,
                       new_diff,
                       bar_width,
                       color='#2029B2',
                       label='sensorDiff',
                       alpha=opcacity,
                       bottom=new_value)

        self.__plt.bar(x + bar_width,
                       new_max,
                       bar_width,
                       color='#776F67',
                       label='sensorMax',
                       alpha=opcacity)

        # firnatuere deb banebb auf 30 zeichen
        format_name = []
        for i in self.__sensorName:
            format_name.append(i[:30])

        # umdrehen der beschriftung
        self.__plt.xticks(x + bar_width, format_name, rotation=90)

        # self.__plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        x1, x2, y1, y2 = self.__plt.axis()
        self.__plt.ylabel('percent')
        self.__plt.title('sensor values in perc based max = 100')
        # override the xlabels with our custom

    def __createFigure_allAmbient(self):
        """
            function to create a plot for diff temperatures

        """

        # errechnen der offsets
        offset_20 = 20 - self.__sensorValue[0]
        offset_35 = 35 - self.__sensorValue[0]
        offset_40 = 40 - self.__sensorValue[0]
        offset_45 = 45 - self.__sensorValue[0]

        sensor_value20 = []
        sensor_value35 = []
        sensor_value40 = []
        sensor_value45 = []

        sensor_diff20 = []
        sensor_diff35 = []
        sensor_diff40 = []
        sensor_diff45 = []

        for i in range(len(self.__sensorValue)):
            sensor_value20.append(self.__sensorValue[i] + offset_20)
            sensor_value35.append(self.__sensorValue[i] + offset_35)
            sensor_value40.append(self.__sensorValue[i] + offset_40)
            sensor_value45.append(self.__sensorValue[i] + offset_45)

            sensor_diff20.append(self.__sensorMax[i] - sensor_value20[i])
            sensor_diff35.append(self.__sensorMax[i] - sensor_value35[i])
            sensor_diff40.append(self.__sensorMax[i] - sensor_value40[i])
            sensor_diff45.append(self.__sensorMax[i] - sensor_value45[i])

        for i in range(len(self.__sensorValue)):
            if sensor_diff20[i] < 0:
                sensor_diff20[i] = 0

            if sensor_diff35[i] < 0:
                sensor_diff35[i] = 0

            if sensor_diff40[i] < 0:
                sensor_diff40[i] = 0

            if sensor_diff45[i] < 0:
                sensor_diff45[i] = 0

        for i in range(len(sensor_value45)):
            print("{:9}  {:9}  {:9}".format(sensor_value45[i],
                                            sensor_diff45[i],
                                            ""))

        # print subPlots

        self.__plt.subplot(221)
        self.__print_fig2_subplot(sensor_value20, sensor_diff20)
        self.__plt.subplot(222)
        self.__print_fig2_subplot(sensor_value35, sensor_diff35)
        self.__plt.subplot(223)
        self.__print_fig2_subplot(sensor_value40, sensor_diff40)
        self.__plt.subplot(224)
        self.__print_fig2_subplot(sensor_value45, sensor_diff45)

    def __print_fig2_subplot(self, _sensorVal, _sensorDiff):

        bar_width = 0.4
        x = np.arange(len(self.__sensorName))
        opcacity = 0.5

        self.__plt.bar(x,
                       _sensorVal,
                       bar_width,
                       color='red',
                       label='sensorValue',
                       alpha=opcacity)

        self.__plt.bar(x,
                       _sensorDiff,
                       bar_width,
                       color='#2029B2',
                       label='sensorDiff',
                       alpha=opcacity,
                       bottom=_sensorVal)

        self.__plt.bar(x + bar_width,
                       self.__sensorMax,
                       bar_width,
                       color='#776F67',
                       label='sensorMax',
                       alpha=opcacity)

        # self.__plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        self.__plt.ylabel('temperature [°C]')
        txt = "CM-ID: {} sensor values @ {}°C Ambient".format(self.__cmId,
                                                              _sensorVal[0])

        self.__plt.title(txt)

        format_name = []
        for i in range(len(_sensorVal)):
            txt = "s{:02}".format(i)
            format_name.append(txt)

        self.__plt.xticks(x + bar_width, format_name, rotation=90)
