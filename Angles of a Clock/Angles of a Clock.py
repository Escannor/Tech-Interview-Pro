#Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

def calcAngle(h, m):
    '''Return the angle of the clock'''
    hAngle=(h*30)+(m/2)
    if m == 0:
        mAngle = 360
    else:
        mAngle = m*6
    totalAngle  =abs( hAngle-mAngle)
    if totalAngle > 180:
        totalAngle = 360 - totalAngle
    return int(totalAngle)

print (calcAngle(3, 30))
# 75
print (calcAngle(12, 30))
# 165
