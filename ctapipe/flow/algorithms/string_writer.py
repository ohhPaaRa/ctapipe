from ctapipe.core import Component
from traitlets import Unicode
from time import sleep

class StringWriter(Component):

    """`StringWriter` class represents a Stage or a Consumer for pipeline.
        It writes received objects to file
    """
    filename = Unicode('/tmp/test.txt', help='output filename').tag(
        config=True)

    def init(self):
        self.file = open(self.filename, 'w')
        self.log.info("--- StringWriter init filename {}---".format(self.filename))
        return True

    def run(self, object):
        self.file.write(str(object) + "\n")
        self.log.debug('StringWriter write {}'.format( object))

    def finish(self):
        self.file.close()
        self.log.debug("--- StringWriter finish---")
