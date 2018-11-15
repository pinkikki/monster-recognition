import cv2
import numpy as np


def size(im):
  """
  画像のサイズ表示
  """
  print(im.shape)
  show(im)


def show(im):
  """
  画像表示
  """
  cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # リサイズ可能なWindow
  cv2.imshow('image', im)
  cv2.waitKey(0)  # 任意のキーボードを叩いたら、後続の処理を実行
  cv2.destroyAllWindows


def read(file_path: str, mode: int = cv2.IMREAD_UNCHANGED) -> object:
  """
  画像読込み
  :param file_path: ファイルパス
  :param mode: 画像読込みモード
                  cv2.IMREAD_COLOR(カラー画像)
                  cv2.IMREAD_GRAYSCALE(グレースケール画像)
                  cv2.IMREAD_UNCHANGED(アルファチャンネルを含んだ画像)
  """
  return cv2.imread(file_path, mode)


def save(im, file_name):
  """
  画像保存
  """
  cv2.imwrite(file_name, im)


def line(im, start, end, color, thickness):
  cv2.line(im, start, end, color, thickness)
  show(im)


def rectangle(im, upper_left, lower_right, color, thickness):
  """
  :param im: 画像
  :param upper_left: 長方形の左上の座標
  :param lower_right: 長方形の右下の座標
  :param color: 色
  :param thickness: 太さ
  """
  cv2.rectangle(im, upper_left, lower_right, color, thickness)
  show(im)


def circle(im, center, radius, color, thickness):
  """
  :param im: 画像
  :param center: 円の中心座標
  :param radius: 半径
  :param color: 色
  :param thickness: 太さ、-1を指定すると塗りつぶし
  """
  cv2.circle(im, center, radius, color, thickness)
  show(im)


def ellipse(im, center, axes, angle, start_angle, end_angle, color, thickness):
  """
  :param im: 画像
  :param center: 中心座標
  :param axes: 楕円主軸の大きさの半分
  :param angle: 楕円の回転角度
  :param start_angle: 楕円の開始角度
  :param end_angle: 楕円の終了角度
  :param color: 色
  :param thickness: 太さ
  """
  cv2.ellipse(im, center, axes, angle, start_angle, end_angle, color, thickness)
  show(im)


def polygon(im, pts, color, thickness):
  cv2.polylines(im, [pts], True, color, thickness)
  show(im)


if __name__ == '__main__':
  im = read('../input/background.jpg')
  size(im)
  line(im, (0, 0), (100, 20), (255, 255, 255), 10)
  rectangle(im, (300, 300), (500, 500), (255, 0, 0), 3)
  circle(im, (300, 700), 100, (0, 255, 0), 1)
  ellipse(im, (400, 800), (100, 40), 0, 0, 360, (0, 0, 255), 2)
  polygon(im, np.array([[10, 100], [200, 300], [400, 200], [500, 10]], np.int32), (0, 255, 255), 2)
