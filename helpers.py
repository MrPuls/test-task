import json


def parse_request(message: str) -> str:
    parsed_data = {}
    message_to_dict = json.loads(message)
    message_data = message_to_dict['data']
    message_entities = message_data.split('%%')
    for item in message_entities:
        data_params_pairs = item.split('&&')[1:]
        data_params_pairs.remove('')
        iterator = iter(item.split('&&')[1:])
        parsed_data.update({item.split('&&')[0]: dict([x for x in zip(iterator, iterator)])})
    message_to_dict['data'] = parsed_data
    return json.dumps(message_to_dict)
