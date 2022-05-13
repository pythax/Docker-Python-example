import sys
import os

string= """

FROM {}:latest
COPY {} ./
RUN pip install -r {}
WORKDIR /container
COPY {} ./
CMD [ "python", "./{}" ]


"""

class container:
    def create(self):
        string = """
        FROM {}:latest
        COPY {} ./
        RUN pip install -r {}
        WORKDIR /container
        COPY {} ./
        CMD [ "python", "./{}" ]
        """.format(sys.argv[2], sys.argv[3], sys.argv[3], sys.argv[1], sys.argv[1])
        FS = open("dockerfile", "w")
        FS.writelines(string)
        FS.close()
    
        os.system("docker build -t {} .".format(sys.argv[4]))




if __name__ == '__main__':
    if sys.argv.__len__() < 4:
        print("Not enough arguments specified. syntax:\n    python create.py <app name> <base image> <requirements file> <result image name>")
        print("\n.\n.\nbase image options: DEBIAN, CENTOS\n")
        sys.exit()
    CR = container()
    CR.create()
    os.system("docker run {}".format(sys.argv[4]))