import timeit
import numpy as np


def quaternion_to_euler_angle_vectorized1(w, x, y, z):
    ysqr = y * y

    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + ysqr)
    X = np.degrees(np.arctan2(t0, t1))

    t2 = +2.0 * (w * y - z * x)
    t2 = np.where(t2>+1.0,+1.0,t2)
    #t2 = +1.0 if t2 > +1.0 else t2

    t2 = np.where(t2<-1.0, -1.0, t2)
    #t2 = -1.0 if t2 < -1.0 else t2
    Y = np.degrees(np.arcsin(t2))

    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (ysqr + z * z)
    Z = np.degrees(np.arctan2(t3, t4))

    return X, Y, Z 

def main():
    # quaternion_to_euler_angle_vectorized1(orientation_quat.x, orientation_quat.y, orientation_quat.z , orientation_quat.w)
    # quat x:0.15959138547023613,y:-0.07084293188439553,z:-0.050913137237545855,w: -0.9833207620824165

    # get  the time of one way :
    time3 = timeit.default_timer()
    quaternion_to_euler_angle_vectorized1(0.15959138547023613, -0.07084293188439553,-0.050913137237545855 ,-0.9833207620824165)
    time4 = timeit.default_timer()
    diff_3_4 =  time4-time3
    print("diff :%s"  % diff_3_4)

    # get the time of second way :

    time1 = timeit.default_timer()
    r = [ 0.15959138547023613 ,  -0.07084293188439553, -0.050913137237545855 , -0.9833207620824165]
    time2 = timeit.default_timer()
    diff_1_2 = time2 - time1
    if (diff_1_2 > diff_3_4):
        print("diff_1_2  is slower ")
    elif (diff_3_4 > diff_1_2):
        print("diff_3_4  is slower ")
    print("r:", r)

    # print(f"deg x:{self.orientation.x}, y:{self.orientation.y}, z:{self.orientation.z}")
        

if __name__ == "__main__":
    main()

