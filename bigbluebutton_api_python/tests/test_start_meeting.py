import logging
import uuid

import requests
import pytest

from bigbluebutton_api_python import BigBlueButton


@pytest.mark.skip(reason='Test with real server url')
def test_start_meetings():
    bbbServerBaseUrl = ''
    securitySalt = ''

    meeting_name = 'Test Class'
    username = 'Guest'
    banner_text = 'Please log in to remove trial restrictions. www.shikhai.live',

    meeting_id = uuid.uuid4().hex
    params = {
        'name': meeting_name,
        'maxParticipants': 10,
        'record': True,
        'duration': 10,
        'record': True,
        'autoStartRecording': True,
        'allowStartStopRecording': True,
        'logoutURL': ''
    }

    bbb_api = BigBlueButton(bbbServerBaseUrl, securitySalt)

    response = bbb_api.create_meeting(meeting_id, params)

    logging.info('Meeting Create Response')
    logging.info(response)

    join_url = bbb_api.get_join_meeting_url(username, meeting_id, password=response['xml']['moderatorPW'])

    logging.info('Join Url Response')
    logging.info(join_url)

    response = requests.get(join_url)

    logging.info('Session Url Response')
    logging.info(response.url)

    assert '/c/join' in response.url

    meeting_id = uuid.uuid4().hex

    bbb_api = BigBlueButton(bbbServerBaseUrl, securitySalt)

    response = bbb_api.create_meeting(meeting_id, params)

    logging.info('Meeting Create Response')
    logging.info(response)

    join_url = bbb_api.get_join_meeting_url(username, meeting_id, password=response['xml']['moderatorPW'])

    logging.info('Join Url Response')
    logging.info(join_url)

    response = requests.get(join_url)

    logging.info('Session Url Response')
    logging.info(response.url)

    assert '/c/join' in response.url
