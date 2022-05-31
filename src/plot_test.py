import matplotlib.pylab as plt
import mpl_toolkits.mplot3d as a3
import numpy as np


class Surface:
    fileName = '../data/half_sphere.obj'
    faces = []

    def readMesh (self):
        vertices = []
        normals = []
        try:
            f = open(self.fileName, 'r')
            lines = f.readlines()
            for line in lines:
                line = line.split()
                if line[0] == 'v': # vertex
                    coord = list(map(float,line[1:]))
                    vertices.append(coord)
                elif line[0] == 'vn': # vertex normal
                    coord = list(map(float,line[1:]))
                    normals.append(coord)
                elif line[0] == 'f': # face
                    face = {'vertex':[],'normal':[]}
                    line = line[1:]
                    for el in line:
                        indicies = list(map(int,el.split('//')))
                        face['vertex'].append(vertices[indicies[0]-1])
                        face['normal'].append(normals[indicies[1]-1])
                    self.faces.append(face)
        except:
            print("Error opening the file")

class Param:
    fileName = '../data/half_sphere_out.obj'
    faces = []

    def readFile (self):
        vertices = []
        uvs = []
        try:
            f = open(self.fileName, 'r')
            lines = f.readlines()
            for line in lines:
                line = line.split()
                if line[0] == 'v': # vertex
                    coord = list(map(float,line[1:]))
                    vertices.append(coord)
                elif line[0] == 'vt': # uv
                    coord = list(map(float,line[1:]))
                    uvs.append(coord)
                elif line[0] == 'f': # face
                    face = {'vertex':[],'uvs':[]}
                    line = line[1:]
                    for el in line:
                        indicies = list(map(int,el.split('/')))
                        face['vertex'].append(vertices[indicies[0]-1])
                        face['uvs'].append(uvs[indicies[1]-1])
                    self.faces.append(face)
        except:
            print("Error opening the file")


def plot_faces (faces, ax):
    for face in faces:
        face['vertex'].append(face['vertex'][0])
        # face['normal'].append(face['normal'][0])
        xs = []; ys =[]; zs = []
        for i in range(len(face['vertex'])):
            vertex = face['vertex'][i]
            # normal = face['normal'][i]
            xs.append(vertex[0])
            ys.append(vertex[1])
            zs.append(vertex[2])

        ax.plot(xs,ys,zs,color='gray',linewidth='0.5')
        plt.ion()
        plt.draw()

def plot_uvs (faces, ax):
    for face in faces:
        face['uvs'].append(face['uvs'][0])
        xs = []; ys =[]
        for i in range(len(face['uvs'])):
            vertex = face['uvs'][i]
            xs.append(vertex[0])
            ys.append(vertex[1])

        ax.plot(xs,ys,color='gray',linewidth='0.5')
        plt.ion()
        plt.draw()

if __name__ == "__main__":
    # # surface
    # surf = Surface()
    # surf.fileName = '../data/half_sphere.obj'
    # surf.readMesh()
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection="3d")
    # ax.grid(False)
    # plot_faces(surf.faces, ax)
    # plt.show(block=True)

    # parameterized space
    param = Param()
    #param.fileName = '../data/LSCM.obj'
    param.readFile()

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.grid(False)
    plot_uvs(param.faces, ax)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show(block=True)
