import math
import os


def split_string(s_str):
    count = len([f for f in os.listdir("temp") if os.path.isfile(os.path.join("temp", f))])
    count = 10
    per_c=math.ceil(len(s_str)/count)
    c_count=0
    out_str=''
    split_list=[]
    for s in s_str:
        out_str+=s
        c_count+=1
        if c_count == per_c:
            split_list.append(out_str)
            out_str=''
            c_count=0
    if c_count!=0:
        split_list.append(out_str)
    return split_list