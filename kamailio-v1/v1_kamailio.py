## Kamailio - equivalent of routing blocks in Python
##
## KSR - the new dynamic object exporting Kamailio functions
## Router - the old object exporting Kamailio functions
##

## Relevant remarks:
##  * return code -255 is used to propagate the 'exit' behaviour to the
##  parent route block function. The alternative is to use the native
##  Python function sys.exit() (or exit()) -- it throws an exception that
##  is caught by Kamailio and previents the stop of the interpreter.


import sys
import KSR as KSR

# global variables corresponding to defined values (e.g., flags) in kamailio.cfg
FLT_ACC=1
FLT_ACCMISSED=2
FLT_ACCFAILED=3
FLT_NATS=5

FLB_NATB=6
FLB_NATSIPPING=7


# global function to instantiate a kamailio class object
# -- executed when kamailio app_python module is initialized
def mod_init():
    KSR.info("===== from Python mod init\n")
    # dumpObj(KSR)
    return kamailio()

def dumpObj(obj):
    for attr in dir(obj):
        KSR.info("obj.%s = %s\n" % (attr, getattr(obj, attr)))


# -- {start defining kamailio class}
class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n')


    # executed when kamailio child processes are initialized
    def child_init(self, rank):
        KSR.info('===== kamailio.child_init(%d)\n' % rank)
        return 0

    def ksr_request_route(self, msg):
        KSR.info("===== request - from kamailio python script\n")
        KSR.setdsturi("sip:alice@127.0.0.1:5080")
        KSR.tm.t_on_branch("ksr_branch_route_one")
        KSR.tm.t_on_reply("ksr_onreply_route_one")
        KSR.tm.t_on_failure("ksr_failure_route_one")
        KSR.sl.send_reply(100, "Trying")
        if KSR.tm.t_relay() < 0 :
            KSR.sl.send_reply(500, "Server error")
        return 1

    def ksr_reply_route(self, msg):
        KSR.info("===== response - from kamailio python script\n")
        return 1

    def ksr_onsend_route(self, msg):
        KSR.info("===== onsend route - from kamailio python script\n")
        return 1

    def ksr_branch_route_one(self, msg):
        KSR.info("===== branch route - from kamailio python script\n")
        return 1

    def ksr_onreply_route_one(self, msg):
        KSR.info("===== onreply route - from kamailio python script\n")
        return 1

    def ksr_failure_route_one(self, msg):
        KSR.info("===== failure route - from kamailio python script\n")
        return 1
