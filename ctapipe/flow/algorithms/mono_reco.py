from ctapipe.core.traits import (
    List,
    traits_expand_path,
    Unicode,
)
from ctapipe.flow.algorithms.in_out_process import InOutProcess



class MonoReco(InOutProcess):

    exe = Unicode(help='executable').tag(
        config=True)
    options = List(help='executable option').tag(
        config=True)
    output_dir = Unicode(help='executable').tag(
        config=True)

    @validate('exe')
    @traits_expand_path
    def _check_exe(self, proposal):
        return proposal['value']

    def init(self):
        super().init(self.exe, self.options, out_extension="ptablehillassvdset",
                     output_dir=self.output_dir)
