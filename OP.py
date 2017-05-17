"""

"""

class OpenProtocol:
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




        def assemblyHeader(self, arg_mid, arg_rev='001', arg_no_ack_flag=' ', arg_station_id='  ', arg_spindle_id='  ',
                               arg_spare='    '):
                return arg_mid + arg_rev + arg_no_ack_flag + arg_station_id + arg_spindle_id + arg_spare

        def Message(self, arg_header, arg_data_field='', arg_mess_end='0'):
                count = len(arg_header) + 4 + len(arg_data_field)
                s = str(count)
                length = '00' + s
                return length + arg_header + arg_data_field + arg_mess_end


