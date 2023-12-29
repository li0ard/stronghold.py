import math
import numpy as np

STRONGHOLD_RINGS = [
	[1408, 2688],
	[4480, 5760],
	[7552, 8832],
	[10624, 11904],
	[13696, 14976],
	[16768, 18048],
	[19840, 21120],
	[22912, 24192]
]

class Point:
	def __init__(self, x, y, z, angle):
		self.x = x
		self.y = y
		self.z = z
		self.angle = angle % 360
		self.slope = math.tan(-angle * math.pi / 180)

	def getLine(self):
		return self.x - self.slope * self.z;

	def getInGameAngle(self):
		if self.angle > 180:
			return -180 + (self.angle - 180);
		elif self.angle < -180:
			return +180 + (self.angle + 180);
		else:
			return self.angle

def getPointIntersection(a: Point, b: Point):
	z = (b.getLine() - a.getLine()) / (a.slope - b.slope)
	x = a.slope * z + a.getLine()

	return [x, z]

def getAngleAtoB(a: Point, b: Point):
	angle = (math.atan2(a.x - b.x, a.z - b.z));
	angle = (-(angle / math.pi) * 360.0) / 2.0 + 180.0;

	if angle > 180:
		angle = -180 + (angle - 180)
	return angle

def getDistanceBetweenPoints(a: Point, b: Point):
	xDistance = a.x - b.x
	yDistance = a.y - b.y
	zDistance = a.z - b.z

	distance = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2) + math.pow(zDistance, 2));
	return distance

def getLineIntersectionOnCircle(point: Point, radius):
	x = point.x
	z = point.z
	angle = point.angle
	if angle < 0:
		angle += 360
	angle -= 180
	d = 90 - angle
	x1 = x / 8
	z1 = z / 8
	r = d * (math.pi / 180)
	m1 = -1 * math.tan(r)
	a = 1 + (m1 * m1);
	b1 = -1 * m1 * x1 + z1
	b = 2 * m1 * b1
	co = b1 * b1 - radius * radius
	xp = ((-1 * b) + (np.sign(angle) * math.sqrt(b * b - 4 * a * co))) / (2 * a);
	zp = m1 * xp + b1;
	return [xp, zp]

def findClosestPointInCircle(point: Point, radius):
	magnitude = math.sqrt(point.x * point.x + point.z * point.z)
	x = point.x / magnitude * radius
	z = point.z / magnitude * radius
	return [x, z]

def checkInRing(point: Point):
	zeroDistance = getDistanceBetweenPoints(Point(0, 0, 0, 0), point)
	inRing = False

	for i in STRONGHOLD_RINGS:
		if zeroDistance > i[0] and zeroDistance < i[1]:
			inRing = True
			break

	return inRing

def applyX4Z4Rule(point: Point):
	x = point.x
	z = point.z
	xOffset = x % 16
	zOffset = z % 16
	x = x - xOffset + 4 if xOffset >= 0 else -12 #(xOffset >= 0 ? 4 : -12)
	z = z - zOffset + 4 if zOffset >= 0 else -12 #(zOffset >= 0 ? 4 : -12)
	return [x, z]
