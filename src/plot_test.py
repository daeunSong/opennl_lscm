import matplotlib.pylab as plt
import mpl_toolkits.mplot3d as a3
import numpy as np


class Surface:
    fileName = '../data/half_sphere_out.obj'
    faces = []  # contains vertices, uvs, normals per face
    vertices = [] # contains vertices, uvs, normals
    uvs = []
    normals = []
    num_ver = 0

    def __init__(self, fileName):
        self.fileName = fileName
        self.readMesh()

    def readMesh (self):
        vertices = []
        normals = []
        uvs = []
        init = False
        check_index = []
        try:
            f = open(self.fileName, 'r')
            lines = f.readlines()
            for line in lines:
                line = line.split()
                # point = {'vertex':[], 'uv':[], 'normal':[]}
                if line[0] == 'v': # vertex
                    coord = list(map(float,line[1:]))
                    vertices.append(coord)
                    self.num_ver = self.num_ver + 1
                    # point['vertex'] = coord
                elif line[0] == 'vt': # uv
                    coord = list(map(float,line[1:]))
                    uvs.append(coord)
                    # point['uv'] = coord
                elif line[0] == 'vn': # vertex normal
                    coord = list(map(float,line[1:]))
                    normals.append(coord)
                    # point['normal'] = coord
                elif line[0] == 'f': # face
                    face = {'vertex':[], 'uv':[], 'normal':[]}
                    line = line[1:]
                    if not init :
                        check_index = list(np.zeros(self.num_ver))
                        init = True
                    for el in line:
                        indicies = list(map(int,el.split('/')))
                        face['vertex'].append(vertices[indicies[0]-1])
                        face['uv'].append(uvs[indicies[1]-1])
                        face['normal'].append(normals[indicies[2]-1])
                        if check_index[indicies[0]-1] == 0:
                            self.vertices.append(vertices[indicies[0]-1])
                            self.uvs.append(uvs[indicies[1]-1])
                            self.normals.append(normals[indicies[2]-1])
                            check_index[indicies[0]-1] = 1
                    self.faces.append(face)
                # self.points.append(point)
        except:
            print("Error opening the file")


    def plot_param (self, ax, plot_normals = False):
        for face in self.faces:
            face['uv'].append(face['uv'][0])
            xs = []; ys =[]
            for i in range(len(face['uv'])):
                vertex = face['uv'][i]
                xs.append(vertex[0])
                ys.append(vertex[1])
            ax.plot(xs,ys,color='gray',linewidth='0.3')
            plt.ion()
            plt.draw()

    def plot_surf (self, ax, plot_normals = False):
        for face in self.faces:
            face['vertex'].append(face['vertex'][0])
            face['normal'].append(face['normal'][0])
            xs = []; ys =[]; zs = []
            for i in range(len(face['vertex'])):
                vertex = face['vertex'][i]
                normal = face['normal'][i]
                xs.append(vertex[0])
                ys.append(vertex[1])
                zs.append(vertex[2])
                if plot_normals:
                    self.plot_normal (vertex, normal, ax)

            ax.plot(xs,ys,zs,color='gray',linewidth='0.3')
            plt.ion()
            plt.draw()

    def plot_normal (self, vertex, normal, ax, scale=0.3):
        p1 = vertex
        p2 = list(np.array(vertex) + np.array(normal)* scale)
        xs = [p1[0], p2[0]]
        ys = [p1[1], p2[1]]
        zs = [p1[2], p2[2]]

        ax.plot(xs,ys,zs,color='red',linewidth='1.0')

        plt.ion()
        plt.draw()

if __name__ == "__main__":
    surf = Surface('../data/pcd_output.obj')

    # plotting
    fig = plt.figure(figsize=plt.figaspect(0.5))

    # 2d uv space
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_xlabel('$U$')
    ax1.set_ylabel('$V$')
    ax1.grid(False)
    surf.plot_param(ax1)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show(block=False)

    # 3d surface
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")
    ax2.set_xlabel('$X$')
    ax2.set_ylabel('$Y$')
    ax2.set_zlabel('$Z$')
    ax2.grid(False)
    surf.plot_surf(ax2, False)


    plt.show(block=False)
