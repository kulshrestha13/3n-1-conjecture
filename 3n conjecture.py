
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from tqdm import tqdm


start = time.time()
res = []

def algo(x):
    if x%2 == 0:
        x=x/2
    else:
        x=3*x+1
    lst.append(x)
    if x!=1:
        algo(x)         


try:
    index = np.load('index.npy', allow_pickle=True)
    index = index.tolist()

    for i in tqdm(index):
        #i=26
        x=3*i+1
        lst = [x]
        algo(x)
        
        lst = np.array(lst)
        q1 = np.percentile(lst, 25)
        median = np.median(lst)
        q3 = np.percentile(lst, 75)
        maximum = np.max(lst)
        
        res.append({"Number": i, "Steps": len(lst), "q1": q1, "median": median, "q3": q3, "maximum": maximum})
        
        
    res_df = pd.DataFrame(res)
    range = np.max(res_df["Steps"])-np.min(res_df["Steps"])
    median = np.median(res_df["Steps"])
    res_df["std steps"] = (res_df["Steps"] - median)/range * 20
    res_df["exp steps"] = 1 / (1 + np.exp(-1*res_df["std steps"]))
    res_arr = res_df.to_numpy()
    np.save('res.npy', res_arr)

    #plt_df = res_df.sort_values(by='exp steps', ignore_index=True)
    #plt.plot(plt_df['std steps'],plt_df["exp steps"])
    #plt.show()

    end = time.time()
    print(end-start)
except Exception as e:
    print(e)
    print(f"Error at {i} position")