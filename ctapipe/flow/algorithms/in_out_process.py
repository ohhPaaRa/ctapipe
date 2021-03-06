from ctapipe.core import Component
from os.path import isdir
from os import makedirs
from subprocess import Popen
from ctapipe.flow.algorithms.build_command import build_command



class InOutProcess(Component):
    exe = None
    out_extension = None
    options = None
    output_dir = None


    """CalibrationStep` class represents a Stage for pipeline.
        it executes prun2pcalibrun
    """

    def init(self, exe, options=None, out_extension=None, output_dir=None, append_to_file=None):
        self.exe = exe
        self.out_extension = out_extension
        self.options = options
        self.output_dir = output_dir
        self.append_to_file = append_to_file
        self.log.info("--- InOutProcess init ---")
        self.log.info("--- InOutProcess exe {} ".format(self.exe))
        self.log.info("--- InOutProcess options {} ".format(self.options))
        self.log.info("--- InOutProcess out_extension {} ".format(self.out_extension))
        self.log.info("--- InOutProcess output_dir {} ".format(self.output_dir))
        if self.output_dir:
            if not isdir(self.output_dir):
                makedirs(self.output_dir)

        if self.exe:
            return True
        return False

    def run(self, in_filename):
        #cmd, _ = build_command(self.exe, in_filename, options=self.options)
        #self.log.info("--- InOutProcess cmd {} --- in_filename {}".format(cmd, in_filename))

        if in_filename != None:
            if self.append_to_file:
                output_file = in_filename
            self.log.info("--- InOutProcess receive [{}] ---".format(in_filename))
            cmd, out_file = build_command(self.exe, in_filename, options=self.options,
                                   out_extension=self.out_extension,
                                   output_dir=self.output_dir, append_to_file=self.append_to_file)

            self.log.info("--- InOutProcess cmd {} --- in_filename {}".format(cmd, in_filename))
            if self.output_dir:
                proc = Popen(cmd, cwd=self.output_dir)
            else:
                proc = Popen(cmd)
            proc.wait()
            self.log.info("--- InOutProcess send [{}] ---".format(out_file))
            return (out_file)

    def finish(self):
        self.log.debug("--- InOutProcess finish ---")
        pass
