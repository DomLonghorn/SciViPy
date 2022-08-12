import laspy as lp
import numpy as np
import open3d as o3d


input_path="/home/user/home/user/Desktop/Data/Max Data/"
dataname="ConveredData.csv"

point_cloud=lp.read(input_path+dataname)


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose())
pcd.colors = o3d.utility.Vector3dVector(np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()/65535)


v_size=round(max(pcd.get_max_bound()-pcd.get_min_bound())*0.005,4)
voxel_grid=o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=v_size)

voxel_grid=o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,voxel_size=v_size)



voxels=voxel_grid.get_voxels()
vox_mesh=o3d.geometry.TriangleMesh()

for v in voxels:
   cube=o3d.geometry.TriangleMesh.create_box(width=1, height=1,
   depth=1)
   cube.paint_uniform_color(v.color)
   cube.translate(v.grid_index, relative=False)
   vox_mesh+=cube



vox_mesh.translate([0.5,0.5,0.5], relative=True)
vox_mesh.scale(voxel_size, [0,0,0])
vox_mesh.translate(voxel_grid.origin, relative=True)
vox_mesh.merge_close_vertices(0.0000001)
o3d.io.write_triangle_mesh(input_path+”voxel_mesh_h.obj”, vox_mesh)


T=np.array([[1, 0, 0, 0],[0, 0, 1, 0],[0, -1, 0, 0],[0, 0, 0, 1]])
o3d.io.write_triangle_mesh(input_path+"4_vox_mesh_r.ply", vox_mesh.transform(T))

