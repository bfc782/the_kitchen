# %%
import numpy as np

# init = [3, 4, 4, 1, 2]

# init = [1,5,5,1,5,1,5,3,1,3,2,4,3,4,1,1,3,5,4,4,2,1,2,1,2,1,2,1,5,2,1,5,1,2,2,1,5,5,5,1,1,1,5,1,3,4,5,1,2,2,5,5,3,4,5,4,4,1,4,5,3,4,4,5,2,4,2,2,1,3,4,3,2,3,4,1,4,4,4,5,1,3,4,2,5,4,5,3,1,4,1,1,1,2,4,2,1,5,1,4,5,3,3,4,1,1,4,3,4,1,1,1,5,4,3,5,2,4,1,1,2,3,2,4,4,3,3,5,3,1,4,5,5,4,3,3,5,1,5,3,5,2,5,1,5,5,2,3,3,1,1,2,2,4,3,1,5,1,1,3,1,4,1,2,3,5,5,1,2,3,4,3,4,1,1,5,5,3,3,4,5,1,1,4,1,4,1,3,5,5,1,4,3,1,3,5,5,5,5,5,2,2,1,2,4,1,5,3,3,5,4,5,4,1,5,1,5,1,2,5,4,5,5,3,2,2,2,5,4,4,3,3,1,4,1,2,3,1,5,4,5,3,4,1,1,2,2,1,2,5,1,1,1,5,4,5,2,1,4,4,1,1,3,3,1,3,2,1,5,2,3,4,5,3,5,4,3,1,3,5,5,5,5,2,1,1,4,2,5,1,5,1,3,4,3,5,5,1,4,3]
init2 = [1,2,3,4,5,6]

# %%
arr = np.array(init2)
cnt1, cnt2, cnt3, cnt4, cnt5, cnt6 = 0,0,0,0,0,0
cnts = [cnt1, cnt2, cnt3, cnt4, cnt5, cnt6]
for _ in range(80):
    arr = (arr - 1) % 7
    for j in range(1,7):
        if arr[j - 1] == 0:
            cnts[j - 1] += 1
print(cnts)



# new_fish = 0
# young_fish = 0
# days = 80

# for i in range(days):
#     if new_fish > 0:
#         arr.resize(arr.size + new_fish)
#         arr[-new_fish:] = 8

#     arr[:arr.size - young_fish] = \
#         (arr[:arr.size - young_fish] - 1) % 7
#     if young_fish > 0:
#         arr[-young_fish:] = arr[-young_fish:] -1
#     new_fish = sum(arr == 0)
#     young_fish = sum(arr > 7)
# print(arr.size)


# # %%
# days = 4
# arr = np.zeros(shape=(days, len(init)))
# new_fish = 0
# young_fish = 0

# # %%
# arr[0, :] = init
# for i in range(days):
#     if i == 0:
#         pass
#     else:
#         if new_fish > 0:
#             # arr.resize(days, arr.shape[1] + new_fish)
#             arr = np.resize(arr, (days, arr.shape[1] + new_fish))
#             arr[i, -new_fish:] = 8
    
#         arr[i, :arr.shape[1] - max(young_fish, new_fish)] = \
#             (arr[i - 1, :arr.shape[1] - max(young_fish, new_fish)] - 1) % 7

#         # if young_fish > 0:
#         #     arr[i, -young_fish:] = arr[i - 1, - young_fish:] -1

#         new_fish = sum(arr[i, :] == 0)
#         young_fish = sum(arr[i, :] > 7)
#     print(arr[:,:])



# %%
