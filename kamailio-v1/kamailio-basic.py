import sys
import KSR as KSR

def dumpObj(obj):
    for attr in dir(obj):
        KSR.info("obj.%s = %s\n" % (attr, getattr(obj, attr)))

def mod_init():
    KSR.info("===== from Python mod init\n")
    # dumpObj(KSR)
    return kamailio()

class kamailio:
    def __init__(self):
        KSR.info('===== kamailio.__init__\n')

    def child_init(self, rank):
        KSR.info('===== kamailio.child_init(%d)\n' % rank)
        return 0

    #def ksr_request_route(self, msg):
        #KSR.info("===== request - from kamailio python script\n")
        #KSR.setdsturi("sip:alice@127.0.0.1:5080")
        #KSR.tm.t_on_branch("ksr_branch_route_one")
        #KSR.tm.t_on_reply("ksr_onreply_route_one")
        #KSR.tm.t_on_failure("ksr_failure_route_one")
        #KSR.sl.send_reply(100, "Trying")
        #if KSR.tm.t_relay() < 0 :
        #    KSR.sl.send_reply(500, "Server error")
        #return 1

    # SIP request routing
    # -- equivalent of request_route{}
    def ksr_request_route():
        KSR.info("===== request - from kamailio python script\n")
        ksr_route_natdetect()
        KSR.setdsturi("sip:alice@127.0.0.1:5080")
        KSR.tm.t_on_branch("ksr_branch_route_one")
        KSR.tm.t_on_reply("ksr_onreply_route_one")
        KSR.tm.t_on_failure("ksr_failure_route_one")
        KSR.sl.send_reply(100, "Trying")
        if KSR.tm.t_relay() < 0 :
            KSR.sl.send_reply(500, "Server error")
        return 1


    # Caller NAT detection
    def ksr_route_natdetect():
        KSR.force_rport()
        if KSR.nathelper.nat_uac_test(19)>0 :
            if KSR.is_REGISTER() :
                KSR.nathelper.fix_nated_register()
            elif KSR.siputils.is_first_hop()>0 :
                KSR.nathelper.set_contact_alias()

            KSR.setflag(FLT_NATS)

        return 1


    # SIP response handling
    # -- equivalent of reply_route{}
    def ksr_reply_route():
        KSR.dbg("response handling - python script\n")

        if KSR.sanity.sanity_check(17604, 6)<0 :
            KSR.err("Malformed SIP response from "
                    + KSR.pv.get("$si") + ":" + str(KSR.pv.get("$sp")) +"\n")
            KSR.set_drop()
            return -255

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