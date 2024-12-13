def main():
    x1, y1, d1 = map(int, input().split())
    x2, y2, d2 = map(int, input().split())
    n = int(input())
    mirrors = []
    for i in range(n):
        X1, Y1, X2, Y2 = map(int, input().split())
        mirrors.append((X1, Y1, X2, Y2))

    def reflect(dir_, slope_plus_one):
        if slope_plus_one:
            if dir_ == 1: return 4
            if dir_ == 2: return 3
            if dir_ == 3: return 2
            if dir_ == 4: return 1
        else:
            if dir_ == 1: return 2
            if dir_ == 2: return 1
            if dir_ == 3: return 4
            if dir_ == 4: return 3

    def orientation(ax,ay,bx,by,cx,cy):
        val = (by - ay)*(cx - bx) - (bx - ax)*(cy - by)
        val = (bx - ax)*(cy - ay) - (by - ay)*(cx - ax)
        if val > 0:
            return 1
        elif val < 0:
            return 2
        else:
            return 0

    def on_segment(ax,ay,bx,by,cx,cy):
        return min(ax,bx)<=cx<=max(ax,bx) and min(ay,by)<=cy<=max(ay,by)

    def segments_intersect(xA,yA,xB,yB,xC,yC,xD,yD):
        o1 = orientation(xA,yA,xB,yB,xC,yC)
        o2 = orientation(xA,yA,xB,yB,xD,yD)
        o3 = orientation(xC,yC,xD,yD,xA,yA)
        o4 = orientation(xC,yC,xD,yD,xB,yB)

        if o1!=o2 and o3!=o4:
            return True
        if o1==0 and on_segment(xA,yA,xB,yB,xC,yC):
            return True
        if o2==0 and on_segment(xA,yA,xB,yB,xD,yD):
            return True
        if o3==0 and on_segment(xC,yC,xD,yD,xA,yA):
            return True
        if o4==0 and on_segment(xC,yC,xD,yD,xB,yB):
            return True
        return False

    def segment_ray_intersect(xA,yA,xB,yB,x0,y0,dir_):
        dx=0;dy=0
        if dir_==1: dy=1
        if dir_==2: dx=1
        if dir_==3: dy=-1
        if dir_==4: dx=-1
        M=10**11
        xF = x0+dx*M
        yF = y0+dy*M
        return segments_intersect(xA,yA,xB,yB,x0,y0,xF,yF)

    def two_rays_intersect(x0,y0,dir1,x1,y1,dir2):
        d1x=0;d1y=0
        if dir1==1: d1y=1
        if dir1==2: d1x=1
        if dir1==3: d1y=-1
        if dir1==4: d1x=-1

        d2x=0;d2y=0
        if dir2==1: d2y=1
        if dir2==2: d2x=1
        if dir2==3: d2y=-1
        if dir2==4: d2x=-1

        denom = d1x*d2y - d1y*d2x
        if denom==0:
            return False
        dx=(x1 - x0)
        dy=(y1 - y0)
        t = (dx*d2y - dy*d2x)/denom
        s = (dx*d1y - dy*d1x)/denom
        return t>=0 and s>=0

    def get_laser_path(x0,y0,d0,removed):
        segments = []
        reflections = []
        cx, cy = x0, y0
        cd = d0

        for _ in range(n+1):
            dx=0;dy=0
            if cd==1: dy=1
            if cd==2: dx=1
            if cd==3: dy=-1
            if cd==4: dx=-1
            best_dist = None
            best_point = None
            best_mi = None
            for i_m,(X1,Y1,X2,Y2) in enumerate(mirrors):
                if removed[i_m]:
                    continue
                dxm = X2 - X1
                dym = Y2 - Y1
                denom = dx*(Y2 - Y1)-dy*(X2 - X1)
                if denom==0:
                    continue
                num_t = (X1 - cx)*(Y2 - Y1)-(Y1 - cy)*(X2 - X1)
                t = num_t/denom
                if t<0:
                    continue
                if dxm!=0:
                    s_ = (cx+dx*t - X1)/dxm
                else:
                    s_ = (cy+dy*t - Y1)/dym
                if s_<=0 or s_>=1:
                    continue
                ix = cx+dx*t
                iy = cy+dy*t
                dist = (ix - cx)**2+(iy - cy)**2
                if best_dist is None or dist<best_dist:
                    best_dist=dist
                    best_point=(ix,iy)
                    best_mi=i_m
            if best_point is None:
                segments.append((cx,cy,None,None))
                return segments, reflections, cd
            else:
                ix, iy = best_point
                i_m = best_mi
                X1,Y1,X2,Y2 = mirrors[i_m]
                dxm=X2 - X1
                dym=Y2 - Y1
                slope_plus_one = (dxm>0 and dym>0) or (dxm<0 and dym<0)
                segments.append((cx,cy,ix,iy))
                cd = reflect(cd,slope_plus_one)
                cx, cy = ix, iy
                reflections.append(i_m)

        segments.append((cx,cy,None,None))
        return segments, reflections, cd

    def paths_intersect(path1,final_dir1,path2,final_dir2):
        len1=len(path1)
        len2=len(path2)

        inf1 = (path1[-1][2] is None)
        inf2 = (path2[-1][2] is None)

        end1 = len1-1 if inf1 else len1
        end2 = len2-1 if inf2 else len2
        for i in range(end1):
            xA,yA,xB,yB = path1[i]
            for j in range(end2):
                xC,yC,xD,yD = path2[j]
                if segments_intersect(xA,yA,xB,yB,xC,yC,xD,yD):
                    return True

        if inf1:
            xA,yA = path1[-1][0],path1[-1][1]
            for j in range(end2):
                xC,yC,xD,yD=path2[j]
                if segment_ray_intersect(xC,yC,xD,yD,xA,yA,final_dir1):
                    return True
            if inf2:
                xB,yB = path2[-1][0],path2[-1][1]
                if two_rays_intersect(xA,yA,final_dir1,xB,yB,final_dir2):
                    return True

        if inf2:
            xC,yC = path2[-1][0],path2[-1][1]
            for i in range(end1):
                xA,yA,xB,yB=path1[i]
                if segment_ray_intersect(xA,yA,xB,yB,xC,yC,final_dir2):
                    return True

        return False

    removed = [False]*n
    rem1=0
    rem2=0

    while True:
        p1,r1,dlast1 = get_laser_path(x1,y1,d1,removed)
        p2,r2,dlast2 = get_laser_path(x2,y2,d2,removed)
        if not paths_intersect(p1,dlast1,p2,dlast2):
            print(rem1, rem2)
            break
        else:
            m1 = r1[-1] if len(r1)>0 else None
            m2 = r2[-1] if len(r2)>0 else None
            if m1 is None and m2 is None:
                print(rem1,rem2)
                break
            if m1 is not None:
                removed[m1]=True
                rem1+=1
            if m2 is not None:
                removed[m2]=True
                rem2+=1

if __name__ == '__main__':
    main()
