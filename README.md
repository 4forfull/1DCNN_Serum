# **1DCNN_Serum**
This repository provides the implementation for our paper **Serological antibody profiling of Helicobacter pylori carcinogenic toxins via computational analysis of label-free SERS spectra*. Our experiments show that this sofware can be used as a practical and efficient tool for Serum Antibody SERS spectral analysis. This software provides two functions for input spectral data: peak search and identify the unknown samples automatically and efficiently. 
# **Requirements**  
keras 2.4.3  
matplotlib 3.1.1  
numpy 1.18.5  
pandas 0.25.1  
python 3.7  
pyqt5 5.15.4  
scikit-learn 0.21.3 
# **Function**  
[**main**](https://github.com/4forfull/1DCNN_Serum/blob/main/serum_hp1.py): This is the main interface of the software, all the functions are integrated in it.  
[**model**](https://github.com/4forfull/1DCNN_Serum/blob/main/MSCNN.py): Load the pre-trained model, the spectral data of serum were predicted.  
[**curve**](https://github.com/4forfull/1DCNN_Serum/blob/main/visual_curve.py): Visualize the raw spectral data and fit the characteristic peaks.  
# **Usage**  
Run the [main.py](https://github.com/4forfull/1DCNN_Serum/blob/main/serum_hp1.py) file.  
Click "OPEN" and select the data you want to analyze. The demo data is given in the [demo](https://github.com/4forfull/1DCNN_Serum/tree/main/Demo) folder.  
![image](https://github.com/4forfull/1DCNN_Serum/blob/main/Figure/curve.png)  
Click "RUN" to execute the model file, and the software will automatically analyze the types of shigella.  
![image](https://github.com/4forfull/1DCNN_Serum/blob/main/Figure/predict.png)  
# **Contact**  
**Name**: Prof. Liang Wang, Jia-Wei Tang.  
**E-mail**: wangliang@gdph.org.cn, 15061183455@163.com.  
