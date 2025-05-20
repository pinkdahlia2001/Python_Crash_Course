import numpy as ny
import scipy.stats as stats

sybr_0h_pa256 = [7561, 7288, 6282]
sybr_24h_pa256 = [8888, 6426, 5750]

t_value, p_value = stats.ttest_rel(sybr_0h_pa256, sybr_24h_pa256)

print('T-value:', t_value)
print('P-value:', p_value)



sybr_0h_pa256_control = [7561, 7288, 6282]
sybr_24h_pa256_control = [2778, 4769, 2950]

t_value, p_value = stats.ttest_rel(sybr_0h_pa256_control, sybr_24h_pa256_control)

print('T-value:', t_value)
print('P-value:', p_value)