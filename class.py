import pandas as pd
# # a=[1,7,2]
# a = {"one":1,"two":2,"three":3}
# # b=pd.Series(a,index=["x","y","z"])
# # b=pd.Series(a)
#
# # print(b.loc["y"])
# print(b)


a={"roll no":[1,2,3,4],
   "name":["a","b","c","d"],
   "marks":[20,30,50,70]}


b=pd.DataFrame(a)
x=int(input("enter index"))
print(b.loc[x])


