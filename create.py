import sys
import os




class container_image:
    def create(self):
        string = """
        FROM {}:latest
        COPY {} ./
        RUN apt-get update 
        RUN apt-get -y install python3-pip
        RUN pip3 install -r {}
        WORKDIR /container
        COPY {} ./
        CMD [ "python3", "./{}" ]
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
    CR = container_image()
    CR.create()