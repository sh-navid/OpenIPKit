import scripts.nsproc as proc


def line(im, pt1, pt2, color=(0, 0, 0), thickness=5):
    k = proc.kernel((thickness, thickness), proc.KERNEL_TYPE_RECT)

    pass


def chessGrid(im, color1=(0, 0, 0), color2=(255, 255, 255), thickness=50):
    '''
    '''
    # FIXME: check this in different sizes; does not work sometimes
    k = proc.kernel((thickness, thickness), proc.KERNEL_TYPE_RECT)
    h, w = im.shape[:2]
    nh, nw = h//thickness, w//thickness
    im[:] = color2
    paint = True
    for hh in range(0, nh+1):
        for ww in range(0, nw+1):
            paint = not paint
            if paint:
                continue
            y = hh*thickness
            x = ww*thickness
            im[y:y+thickness, x:x+thickness] = color1
    return im
