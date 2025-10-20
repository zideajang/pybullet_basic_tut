import pybullet as p
import pybullet_data
import time

# 1. 初始化 PyBullet
# p.GUI 表示可视化模式，p.DIRECT 表示非可视化模式（更快）
physicsClient = p.connect(p.GUI)
# physicsClient = p.connect(p.DIRECT) # 如果不需要GUI窗口

# 设置重力
p.setGravity(0, 0, -10)

# 添加搜索路径，以便找到内置的URDF文件（如plane.urdf）
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 2. 创建平面（地面）
# 加载PyBullet内置的平面模型
planeId = p.loadURDF("plane.urdf")

# 3. 创建小球（球体）
radius = 0.5 # 小球的半径

# 创建球体的碰撞形状
colSphereId = p.createCollisionShape(shapeType=p.GEOM_SPHERE, radius=radius)

# 创建球体的视觉形状（可选，用于GUI显示）
visSphereId = p.createVisualShape(shapeType=p.GEOM_SPHERE, radius=radius, rgbaColor=[1, 0, 0, 1]) # 红色小球

# 4. 设置小球的初始位置
# z轴的初始位置设置为半径值，这样小球的底部就刚好接触到地面（地面在z=0）
basePosition = [0, 0, radius]
baseOrientation = p.getQuaternionFromEuler([0, 0, 0])

# 创建小球的刚体
ballId = p.createMultiBody(
    baseMass=1,                             # 小球的质量
    baseCollisionShapeIndex=colSphereId,    # 碰撞形状
    baseVisualShapeIndex=visSphereId,       # 视觉形状
    basePosition=basePosition,              # 初始位置
    baseOrientation=baseOrientation         # 初始方向
)

# 5. 运行模拟步（可选，但推荐）
# 运行一段时间让物理引擎稳定
for i in range(1000):
    p.stepSimulation()
    time.sleep(1./240.) # 延迟，使其在GUI中可见（240 FPS）

# 保持窗口打开直到用户关闭
while p.isConnected():
    p.stepSimulation()
    time.sleep(1./240.)

# 关闭连接
p.disconnect()