def get_header(arg_mess): return arg_mess[:20]

def get_length(arg_mess): return arg_mess[:4]

def get_mid(arg_mess): return arg_mess[4:8]

def get_revision(arg_mess): return arg_mess[9:12]

def get_no_ack_flag(arg_mess): return arg_mess[12]

def get_station_id(arg_mess): return arg_mess[13:15]

def get_spindle_id(arg_mess): return arg_mess[15:17]

def get_spare(arg_mess): return arg_mess[17:20]

def get_err_code(arg_mess): return arg_mess[24:26]



