import asyncio


class ClientOpenProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop
        self.revision = '001'
        self.no_ack_flag = ' ' # 1 пустой байта
        self.station_id = '  ' # 2 пустых байта
        self.spindle_id = '  ' # 2 пустых байта
        self.spare = '    ' # 4 пустых байта

        self.data_field = ''
        self.mess_end = '0'
        self.MID = {'Communication_start': '0001',
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

    def assembly_header(self, arg_mid):
        return self.arg_mid + self.revision + self.no_ack_flag + self.station_id + self.spindle_id + self.spare

    def message(self):
        count = 20 + len(self.data_field)
        s = str(count)
        length = '00' + s
        return length + self.data_field + self.mess_end

    def connection_made(self, transport):
        print("TCP connect")
        transport.write(self.message(self.assembly_header(self.MID['Communication_start'])).encode())
        print(self.message(self.assembly_header(self.MID['Communication_start'])))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


loop = asyncio.get_event_loop()
coro = loop.create_connection(lambda: ClientOpenProtocol(loop),
                              '192.168.8.1', 4545)
loop.run_until_complete(coro)
loop.close()



