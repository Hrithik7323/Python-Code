import numpy as np
array_3d = np.array([
    [[1,2,3],[4,5,6]],
    [[11,12,12,],[14,15,16]],
    [[21,22,23],[24,25,26]]
])
print(array_3d)
print("=============================================")
print(array_3d.shape)
print("=============================================")
print(array_3d[0,1,1])
print("=============================================")
print(array_3d[2,1,2])
print("=============================================")
print(array_3d.itemsize)
print("=============================================")
print(array_3d[0:2,:,0:2])
print("===============================================")
vall=np.arange(24)
reshape = (vall.reshape(2,3,4))
print("reshape",reshape)
print("===============================================")
print(vall)
print("===============================================")
print(reshape.shape)
print("===============================================")
normal_array=np.transpose(reshape,(0,1,2))
print(normal_array)
print("===============================================")
transpose_array=np.transpose(reshape,(1,0,2))
print(transpose_array)