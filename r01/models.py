from django.db import models


# Create your models here.
class UserInfo(models.Model):
    """用户信息表"""
    username = models.CharField(max_length=32, null=False)
    password = models.CharField(max_length=32, null=False)
    regtime = models.DateTimeField(null=True)


class SensorBase(models.Model):
    """传感器基类"""
    # 数据采集时间
    collect_time = models.DateTimeField(null=False)
    # 机器人编号
    robot_number = models.CharField(max_length=256, null=False)
    # 机器人位姿
    robot_posture = models.CharField(max_length=64, null=False)
    # 24个传感器
    sensor_a = models.IntegerField()
    sensor_b = models.IntegerField()
    sensor_c = models.IntegerField()
    sensor_d = models.IntegerField()
    sensor_e = models.IntegerField()
    sensor_f = models.IntegerField()
    sensor_g = models.IntegerField()
    sensor_h = models.IntegerField()
    sensor_i = models.IntegerField()
    sensor_j = models.IntegerField()
    sensor_k = models.IntegerField()
    sensor_l = models.IntegerField()
    sensor_m = models.IntegerField()
    sensor_n = models.IntegerField()
    sensor_o = models.IntegerField()
    sensor_p = models.IntegerField()
    sensor_q = models.IntegerField()
    sensor_r = models.IntegerField()
    sensor_s = models.IntegerField()
    sensor_t = models.IntegerField()
    sensor_u = models.IntegerField()
    sensor_v = models.IntegerField()
    sensor_w = models.IntegerField()
    sensor_x = models.IntegerField()

    class Meta:
        abstract = True


# 两个传感器子类
class InfraredSensor(SensorBase):
    """红外传感器"""


class UltrasonicSensor(SensorBase):
    """超声传感器"""


class LaserSensor(models.Model):
    """激光传感器"""
    collect_time = models.DateTimeField(null=False)
    robot_numer = models.CharField(max_length=256)
    robot_posture = models.CharField(max_length=64)
    scene = models.CharField(max_length=64)
    data_filename = models.CharField(max_length=64)
    file_path = models.CharField(max_length=256)
    # 三个区域
    area_a = models.CharField(max_length=64)
    area_b = models.CharField(max_length=64)
    area_c = models.CharField(max_length=64)


class VisionBase(models.Model):
    """视觉传感器基类"""
    collect_time = models.DateTimeField(null=False)
    robot_numer = models.CharField(max_length=256)
    robot_posture = models.CharField(max_length=64)
    scene = models.CharField(max_length=64)
    filename = models.CharField(max_length=64)
    img_path = models.CharField(max_length=256)

    class Meta:
        abstract = True


class ForwardVisionSensor(VisionBase):
    """向前视觉传感器"""


class OverallViewSensor(VisionBase):
    """全景视觉传感器"""


class KinectVideoSensor(VisionBase):
    """Kinect 彩色视频传感器"""


class KinectDeepSensor(models.Model):
    """Kinect 深度传感器"""
    collect_time = models.DateTimeField(null=False)
    robot_numer = models.CharField(max_length=256)
    robot_posture = models.CharField(max_length=64)
    scene = models.CharField(max_length=64)
    deep_filename = models.CharField(max_length=64)
    deep_path = models.CharField(max_length=256)
    mapped_img_filename = models.CharField(max_length=64)
    mapped_img_path = models.CharField(max_length=256)
