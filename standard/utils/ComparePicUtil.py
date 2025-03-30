import time
from symtable import Class
import cv2

from standard.utils import PrintScreenUtil


def wait_for_friend_round():
    flag = True

    # 示例：查找按钮图标,如果匹配到则为友方回合，传入模板图片地址以及模板相对坐标，每隔3s检查一次

    while flag:
        if not PrintScreenUtil.find_target_on_screen(1650, 800, 250, 250):
            time.sleep(3)
        else:
            flag = False


class ComparePicUtil:
    # wait_for_friend_round()
    pass
