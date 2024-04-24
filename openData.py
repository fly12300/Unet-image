# 两种方法都能打开
import pickle

f = open('results_trial3/history_CV0.pkl','rb')
data = pickle.load(f)
print(data)

