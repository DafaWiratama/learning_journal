import cv2
import numpy as np

buffer = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

vertex = np.array([
    [-1, -1, -1], [-1, 1, -1], [1, 1, -1], [1, -1, -1],
    [-1, -1, 1], [-1, 1, 1], [1, 1, 1], [1, -1, 1],
]) / 4.

faces = np.array([
    [0, 1, 2], [0, 2, 3],
    [4, 5, 6], [4, 6, 7],

    [0, 4, 7], [0, 7, 3],
    [0, 1, 5], [0, 5, 4],

    [1, 2, 6], [1, 6, 5],
    [2, 3, 7], [2, 7, 6],
])

resolution = 512


def rotation_x(angle: float) -> np.array:
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)],
    ])


def rotation_y(angle: float) -> np.array:
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)],
    ])


def rotation_z(angle: float) -> np.array:
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1],
    ])


def projection_matrix():
    fov = np.pi / 3.
    aspect = resolution / resolution
    near = 0.1
    far = 100.
    toReturn = np.array([
        [1 / (np.tan(fov / 2) * aspect), 0, 0, 0],
        [0, 1 / np.tan(fov / 2), 0, 0],
        [0, 0, -(far + near) / (far - near), -1],
        [0, 0, -(2 * far * near) / (far - near), 0],
    ])
    return toReturn


def draw_line(x1, y1, x2, y2, buffer):
    x1 += .5
    y1 += .5
    x2 += .5
    y2 += .5
    x_step = (x2 - x1) / resolution
    y_step = (y2 - y1) / resolution

    for i in range(int(resolution)):
        x = (x1 + i * x_step) * resolution - 1
        y = (y1 + i * y_step) * resolution - 1
        if 0 < x < resolution and 0 < y < resolution:
            buffer[int(x), int(y)] = [255, 255, 255]

    return buffer


angle_x = 0.
angle_y = 0.
angle_z = 0.


def on_draw(buffer: np.array) -> np.array:
    for face in faces:

        for i in range(-1, len(face) - 1):
            p1 = vertex[face[i]]
            p2 = vertex[face[i + 1]]

            x1, y1, z1 = p1 @ rotation_x(angle_x) @ rotation_y(angle_y) @ rotation_z(angle_z)
            x2, y2, z2 = p2 @ rotation_x(angle_x) @ rotation_y(angle_y) @ rotation_z(angle_z)

            z1 = (z1 + 5) / 5
            z2 = (z2 + 5) / 5

            buffer = draw_line(x1 / z1, y1 / z1, x2 / z2, y2 / z2, buffer)

    return buffer


cv2.namedWindow('ViewPort', cv2.WINDOW_NORMAL)
cv2.resizeWindow('ViewPort', resolution, resolution)

target_fps = 30
frame_time = int(1000 / target_fps)

while cv2.waitKey(frame_time) != 27:
    buffer[:, :, :] = 0

    angle_x += .05
    angle_y += .025
    angle_z += .01

    cv2.imshow('ViewPort', on_draw(buffer))

cv2.destroyAllWindows()

