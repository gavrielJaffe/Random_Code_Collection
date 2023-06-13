
def test_R_velo_ang_velo(R_ang_velo_velo):
    R = R_ang_velo_velo[0]
    ang_velo = R_ang_velo_velo[1]
    velo = R_ang_velo_velo[2]
    return ((R >= 5 ) and (0 <= ang_velo <= 4.5) and (0 <= velo <= 3.5))

     
def main():
    """
    init this in code
    test_list_ranges = R,ang_velo,velo
    """
    #test_on the tuple = R                ,ang_velo      ,velo
    # R_ang_velo_velo = (9.566121426990593, -0.01348366, -0.128986328840256)
    R = 13
    ang_velo = -0.01348366
    velo = 0.128986328840256

    R_ang_velo_velo = (R,ang_velo,velo)
    answer =  test_R_velo_ang_velo(R_ang_velo_velo)
    if answer:
        print('in the right range')
    else:
        print('NOT in range')

if __name__=="__main__":
    main()