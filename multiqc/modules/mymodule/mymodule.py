from multiqc.base_module import BaseMultiqcModule
import logging

log = logging.getLogger(__name__)
class MultiqcModule(BaseMultiqcModule):
    def __init__(self):
        super(MultiqcModule, self).__init__(
            name="MyModule",
            anchor="mymodule",
            info=" Test - this module catches tsv file types and prints a hello message"

        )
    log.info("Hello World")
