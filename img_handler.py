from PIL import Image
def ResizeImg(path,new_w,new_h,new_img_path=""):
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open(path)
    # 获得图像尺寸:
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放到目标尺寸
    im.thumbnail((new_w, new_h))
    print('Resize image to: %sx%s' % (new_w,new_h))
    # 把缩放后的图像用jpeg格式保存:
    im.save(new_img_path, 'jpeg')


def IsImgFile(file_name):
    img_file_suffix_list = [".png",".jpg",".jpeg"]
    for suffix in img_file_suffix_list :
        if file_name.find(suffix) !=-1:
            return True
    return False

import os
def RecurDir(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    # 需要遍历子文件
    for file in files: #遍历文件夹
        if os.path.isdir(file): #判断是否是文件夹,是的话塞入其中的文件
            files.append(RecurDir(file))
        files.remove(file)
    return files

def ResizeDirImgs(dir_path,new_w,new_h):
    print("resize dir %s's imgs to size(%d,%d)" %(dir_path,new_w,new_h))
    files= os.listdir(dir_path) #得到文件夹下的所有文件名称
    new_dir = dir_path
    if len(files)!=0:
        new_dir = dir_path+"/resize_imgs_{}_{}/".format(new_w,new_h)
        os.mkdir(new_dir)
    for file in files:
        print("file name= ",file)
        if not os.path.isdir(file):
            if IsImgFile(file):
                new_img_path = new_dir+file
                ResizeImg(dir_path+"/"+file,new_w,new_h,new_img_path)

if __name__ == "__main__":
    ResizeImg("./imgs/timg.jpg",100,100,"./imgs/"+"timg_resize.jpg")
    ResizeDirImgs("./imgs",1000,1200)