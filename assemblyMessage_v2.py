#******************Structure message**********************************
# |Header(20byte)|Data Field(variable)|Message End(0 byte)
#********HEADER***********************
"""Length(1-4 byte) - The length is the length of the header plus the data field excluding the NUL termination.
                        The header always includes information about the length
                        of the message. The length is represented by four ASCII
                        digits (‘0’…’9’) specifying a range of 0000 to 9999.
   MID(5-8 byte) - The MID is four bytes long and is specified by four ASCII digits (‘0’…’9’).
                    The MID describes how to interpret the message.
   Revision(9-11 byte) - The revision of the MID is specified by three ASCII digits(‘0’…’9’).
                            The MID revision is unique per MID and is used in case
                            several versions are available for the same MID. Using
                            the revision number the integrator can subscribe or ask
                            for different versions of the same MID. By default the
                            MID revision number is three spaces (revision 1 of the
                            MID). So, if the integrator is interested in the initial
                            revision (revision 1) of the MID, it can send three spaces
                            as MID revision or 001. По умолчанию можно посылать три пустышки или 001.
   No ack flag(12 byte) - ONLY FOR SUBSCRIPTION MIDs.
                            The No Ack Flag is used when setting a subscription. If
                            the No Ack flag is not set in a subscription it means that
                            the subscriber will acknowledge each “push” message
                            sent by the controller (No Ack flag = 0 reliable mode).
                            If set, the controller will only push out the information
                            required without waiting for a receive acknowledgement
                            from the subscriber (No Ack flag = 1 unreliable mode).
   StationID(13,14 byte) - The station the message is addressed to in the case of
                                controller with multi-station configuration. The station ID
                                is 2 byte long and is specified by two ASCII digits
                                (‘0’…’9’). One space is considered as station 1 (default
                                value). Only available if not marked with N/A.
   Spindle ID(15,16) -      The spindle the message is addressed to in the case
                                several spindles are connected to the same controller.
                                The spindle ID is 2 bytes long and is specified by two
                                ASCII digits (‘0’…’9’). Two spaces are considered as
                                spindle 1 (default value). Only available if not marked
                                with N/A. OBS! Is allways 0 for FORD OBS!

   Spare(17-20) - Reserved space in the header for future use."""

MID = { 'Communication_start': '0001',
        'Communication_start_acknowledge': '0002',
        'Communication_stop': '0003',
        'Command_error': '0004',
        'Command_accepted': '0005',

        'Parameter_set_ID_upload_request': '0010',
        'Parameter_set_ID_upload_reply': '0011',
        'Parameter_set_data_upload_request': '0012',
        'Parameter_set_data_upload_reply': '0013',
        'Parameter_set_selected_subscribe': '0014',
        'Parameter_set_selected': '0015',
        'Parameter_set_selected_acknowledge': '0016',
        'Parameter_set_selected_unsubscribe': '0017',

        'Select_Parameter_set': '0018',
        'Set_Parameter_set_batch_size': '0019',
        'Reset_Parameter_set_batch_counter': '0020',
        'Lock_at_batch_done_subscribe': '0021',
        'Lock_at_batch_done_upload': '0022',
        'Lock_at_batch_done_upload_acknowledge': '0023',
        'Lock_at_batch_done_unsubscribe': '0024',

        'Reserved_for_Ford': '0025',

        'Job_ID_upload_request': '0030',
        'Job_ID_upload_reply': '0031',
        'Job_data_upload_request': '0032',
        'Job_data_upload_reply': '0033',
        'Job_info_subscribe': '0034',
        'Job_info': '0035',
        'Job_info_acknowledge': '0036',
        'Job_info_unsubscribe': '0037',
        'Select_Job': '0038',
        'Job_restart': '0039',

        'Tool_data_upload_request': '0040',
        'Tool_data_upload_reply': '0041',
        'Disable_tool': '0042',
        'Enable_tool': '0043',
        'Disconnect_tool_request': '0044',
        'Set_calibration_value_request': '0045',
        'Set_primary_tool_request': '0046',

        'VIN_download_request': '0050',
        'VIN_subscribe': '0051',
        'VIN': '0052',
        'VIN_acknowledge': '0053',
        'VIN_unsubscribe': '0054',

        'Last_tigh_g_result_data_subscribe': '0060',
        'Last_tightening_result_data': '0061',
        'Last_tightening_result_data_acknowledge': '0062',
        'Last_tightening_result_data_unsubscribe': '0063',
        'Old_tightening_result_upload_request': '0064',
        'Old_tightening_result_upload_reply': '0065'}


error_code = {'00': 'No Error',
                '01': 'Invalid data',
                '02': 'Parametr set id not present',
                '03': 'Parametr set can not be set',
                '04': 'Parametr set not runing',

                '06': 'VIN upload subscription already exists',
                '07': 'VIN upload subscription does not exists',
                '08': 'VIN input source not granted',
                '09': 'Last tightening result subscription already exists',
                '10': 'Last tightening result subscription does not exist',
                '11': 'Alarm subsciption already exists',
                '12': 'Alarm subsciption does not exists',
                '13': 'Parameter set selection subscription already exists',
                '14': 'Parameter set selection subscription does not exists',
                '15': 'Tightening ID requested not found',
                '16': 'Connection rejected protocol busy',
                '17': 'Job ID not present',
                '18': 'Job info subscription already exists',
                '19': 'Job info subscription does not exists',
                '20': 'Job can not  be set',
                '21': 'Job not running',
                '22': 'Not possible to execute dynamic Job request',
                '23': 'Job batch decrement failed',
                '24': 'Not possible to create Pset',
                '25': 'Programming control nor granted',

                '30': 'Controller is not a sync Master/station controller',
                '31': 'Multi-spindle status subscription already exists',
                '32': 'Multi-spindle status subscription does not exists',
                '33': 'Multi-spindle result subscription already exists',
                '34': 'Multi-spindle result subscription does not exists',

                '40': 'Job line control info subscription already exists',
                '41': 'Job line control info subscription does not exists',
                '42': 'Identifier input source not granted',
                '43': 'Multiple identifiers work order subscription already exists',
                '44': 'Multiple identifiers work order subscription does not exists',

                '50': 'Status external monitored inputs subscription already exists',
                '51': 'Status external monitored inputs subscription does not exists',
                '52': 'IO device not connected',
                '53': 'Faulty IO device ID',
                '54': 'Tool Tag ID unknown',
                '55': 'Tool Tag ID subscription already exists',
                '56': 'Tool Tag ID subscription does not  exists',

                '58': 'No alarm present',
                '59': 'Tool currently in use',
                '60': 'No histogram available',

                '70': 'Calibration failed',

                '79': 'Command faild',
                '80': 'Audi emergency status subscription exists',
                '81': 'Audi emergency status subscription does not exists',
                '82': 'Automatic/Manual mode subscribe already exist',
                '83': 'Automatic/Manual mode subscribe does not exist',
                '84': 'The relay function subscription already exists',
                '85': 'The relay function subscription DOES NOT exists',
                '86': 'The selector socket info subscription already exist',
                '87': 'The selector socket info subscription doe snot exist',
                '88': 'The digin info subscription already exist',
                '89': 'The digin info subscription does not exist ',
                '90': 'Lock at batch done subscription already exist',
                '91': 'Lock at batch done subscription DOES NOT exist',
                '92': 'Open protocol commands disabled',
                '93': 'Open protocol commands disabled subscription already exists',
                '94': 'Open protocol commands disabled subscription does not exists',
                '95': 'Reject request, PowerMACS is in manual mode',
                '96': 'Client alredy connected',
                '97': 'MID revision unsupported',
                '98': 'Controller internal request timeout',
                '99': 'Unknown MID'
               }


def assembly_header(arg_mid, arg_rev='001', arg_no_ack_flag=' ', arg_station_id='  ', arg_spindle_id='  ', arg_spare='    '):

    return arg_mid + arg_rev + arg_no_ack_flag + arg_station_id + arg_spindle_id + arg_spare



def message(arg_header, arg_data_field='', arg_mess_end='0'):
    count = len(arg_header) + 4 + len(arg_data_field)
    s = str(count)
    length = '00' + s
    return length + arg_header + arg_data_field + arg_mess_end






