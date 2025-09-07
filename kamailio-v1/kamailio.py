from kamailio import KSR

def ksr_request_route():
    KSR.info("=== Incoming SIP request: {} ===".format(KSR.pv.get("$rm")))

    if KSR.is_INVITE():
        KSR.info("Handling INVITE...")
        # RTPengine einbinden
        if KSR.rtpengine.rtpengine_manage() < 0:
            KSR.err("RTPengine manage failed\n")
        KSR.sl.send_reply(100, "Trying")
        return 1

    if KSR.is_REGISTER():
        KSR.info("Handling REGISTER...")
        KSR.sl.send_reply(200, "OK")
        return 1

    # Default
    KSR.sl.send_reply(501, "Not Implemented")
    return 1
