import pybullet as p
import pybullet_data
import time
import math

# 1. 初始化 PyBullet
physicsClient = p.connect(p.GUI) # 或 p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -10) # 设置重力

# 2. 创建地面
planeId = p.loadURDF("plane.urdf")

# --------------------------------------------------
# 3. 创建立方体 (Box)
# --------------------------------------------------
half_extents = [0.5, 0.5, 0.5] # 立方体在 X, Y, Z 方向的半尺寸 (实际尺寸是 1x1x1)
cube_mass = 1.0
cube_pos = [-2, 0, half_extents[2]] # 放置在 (X=-2, Y=0)，Z坐标为半高
cube_orn = p.getQuaternionFromEuler([0, 0, 0])

# 创建碰撞形状
cubeColShapeId = p.createCollisionShape(
    shapeType=p.GEOM_BOX,
    halfExtents=half_extents
)
# 创建视觉形状 (可选，但推荐)
cubeVisShapeId = p.createVisualShape(
    shapeType=p.GEOM_BOX,
    halfExtents=half_extents,
    rgbaColor=[0, 0, 1, 1] # 蓝色
)

# 创建多体 (MultiBody)
cubeId = p.createMultiBody(
    baseMass=cube_mass,
    baseCollisionShapeIndex=cubeColShapeId,
    baseVisualShapeIndex=cubeVisShapeId,
    basePosition=cube_pos,
    baseOrientation=cube_orn
)

# --------------------------------------------------
# 4. 创建球体 (Sphere)
# --------------------------------------------------
sphere_radius = 0.5
sphere_mass = 1.0
sphere_pos = [0, 0, sphere_radius] # 放置在 (X=0, Y=0)，Z坐标为半径
sphere_orn = p.getQuaternionFromEuler([0, 0, 0])

# 创建碰撞形状
sphereColShapeId = p.createCollisionShape(
    shapeType=p.GEOM_SPHERE,
    radius=sphere_radius
)
# 创建视觉形状
sphereVisShapeId = p.createVisualShape(
    shapeType=p.GEOM_SPHERE,
    radius=sphere_radius,
    rgbaColor=[1, 0, 0, 1] # 红色
)

# 创建多体
sphereId = p.createMultiBody(
    baseMass=sphere_mass,
    baseCollisionShapeIndex=sphereColShapeId,
    baseVisualShapeIndex=sphereVisShapeId,
    basePosition=sphere_pos,
    baseOrientation=sphere_orn
)

# --------------------------------------------------
# 5. 创建圆柱体 (Cylinder)
# --------------------------------------------------
cylinder_radius = 0.5
cylinder_height = 1.0
cylinder_mass = 1.0
# PyBullet的GEOM_CYLINDER默认是Z轴对齐的，其`height`参数是圆柱体的实际高度
cylinder_pos = [2, 0, cylinder_height / 2.0] # 放置在 (X=2, Y=0)，Z坐标为半高
cylinder_orn = p.getQuaternionFromEuler([0, 0, 0]) # 保持Z轴向上

# 创建碰撞形状。注意：圆柱体的参数是 (radius, height)
cylinderColShapeId = p.createCollisionShape(
    shapeType=p.GEOM_CYLINDER,
    radius=cylinder_radius,
    height=cylinder_height
)
# 创建视觉形状
cylinderVisShapeId = p.createVisualShape(
    shapeType=p.GEOM_CYLINDER,
    radius=cylinder_radius,
    length=cylinder_height, # 注意视觉形状参数是 length
    rgbaColor=[0, 1, 0, 1] # 绿色
)

# 创建多体
cylinderId = p.createMultiBody(
    baseMass=cylinder_mass,
    baseCollisionShapeIndex=cylinderColShapeId,
    baseVisualShapeIndex=cylinderVisShapeId,
    basePosition=cylinder_pos,
    baseOrientation=cylinder_orn
)

# 6. 运行模拟
# 调整视角以便更好地观察
p.resetDebugVisualizerCamera(cameraDistance=5, cameraYaw=45, cameraPitch=-30, cameraTargetPosition=[0, 0, 0])

print("PyBullet 仿真开始...")
while p.isConnected():
    p.stepSimulation()
    time.sleep(1./240.) # 延迟，使其在GUI中可见

p.disconnect()