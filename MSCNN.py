import numpy as np
from pandas import read_csv, DataFrame
from sklearn.preprocessing import MinMaxScaler
from keras.models import model_from_json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def MSCNN_pre(filepath):
    print('Analysis starts. Please wait while enjoying your coffee... \n')
    df = read_csv(filepath)

    X = np.expand_dims(df.values[:, 0:636].astype(float), axis=2)

    json_file = open(r"阴性阳性二分类Multiscale_CNN.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("阴性阳性二分类Multiscale_CNN.h5")

    json_file = open(r"一型二型二分类Multiscale_CNN.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model1 = model_from_json(loaded_model_json)
    loaded_model1.load_weights("一型二型二分类Multiscale_CNN.h5")

    # 输出预测类别
    y_pred = loaded_model.predict(X)
    y_pred = np.int64(y_pred > 0.5)
    predicted_pro = loaded_model.predict(X)
    predicted_pro = np.max(predicted_pro)

    y_pred1 = loaded_model1.predict(X)
    y_pred1 = np.int64(y_pred1 > 0.5)
    predicted_pro1 = loaded_model1.predict(X)
    predicted_pro1 = np.max(predicted_pro1)

    if y_pred == 0:
        print("Analysis result: The patient was Infected with H. pylori ({:.2%})".format(1-predicted_pro), end=' ')
        if y_pred1 == 0:
            print("and the antibody type was Type I ({:.2%})".format(1 - predicted_pro1))
        else:
            print("and the antibody type was Type II ({:.2%})".format(predicted_pro1))
    else:
        print("Analysis result: The patient was not infected with H. pylori and the predicted accuracy was {:.2%}".format(predicted_pro))


if __name__ == "__main__":
    file_path = 'D:/pythonjinjie/serum_hp_software/demo/positive.csv'
    CNN_pre(file_path)