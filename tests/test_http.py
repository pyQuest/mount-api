from unittest.mock import patch

from mountapi.http import RequestData, Request, Response


@patch('werkzeug.wrappers.Request')
def test_request_data_empty_request_params(wsgi_request_mock):
    wsgi_request_mock.values.to_dict.return_value = {}
    wsgi_request_mock.get_data.return_value = {}
    request_data = RequestData(wsgi_request_mock)
    assert request_data.params == {}


@patch('werkzeug.wrappers.Request')
def test_request_data_get_request_params(wsgi_request_mock):
    wsgi_request_mock.values.to_dict.return_value = {'foo': 'bar'}
    wsgi_request_mock.get_data.return_value = {}
    request_data = RequestData(wsgi_request_mock)
    assert request_data.params == {'foo': 'bar'}


@patch('werkzeug.wrappers.Request')
def test_request_data_post_request_params(wsgi_request_mock):
    wsgi_request_mock.values.to_dict.return_value = {}
    wsgi_request_mock.get_data.return_value = b'{"foo": "bar"}'
    request_data = RequestData(wsgi_request_mock)
    assert request_data.params == {'foo': 'bar'}


@patch('mountapi.http.RequestData')
def test_request_empty_request_params_output(request_data_mock):
    def func():
        return {'foo': 'bar'}

    request_data_mock.params = {}
    request = Request(request_data_mock, func)
    assert request.get_output() == {'foo': 'bar'}


@patch('mountapi.http.RequestData')
def test_request_non_empty_request_params_output(request_data_mock):
    def func(foo):
        return {'foo': foo}

    request_data_mock.params = {'foo': 'bar'}
    request = Request(request_data_mock, func)
    assert request.get_output() == {'foo': 'bar'}


@patch('mountapi.http.Request')
def test_response_empty_output_wsgi(request_mock):
    request_mock.get_output.return_value = {}
    response_wsgi = Response(request_mock).wsgi()
    assert response_wsgi.status_code == 200
    assert response_wsgi.response == [b'{}']


@patch('mountapi.http.Request')
def test_response_non_empty_output_wsgi(request_mock):
    request_mock.get_output.return_value = {'foo': 'bar'}
    response_wsgi = Response(request_mock).wsgi()
    assert response_wsgi.status_code == 200
    assert response_wsgi.response == [b'{"foo": "bar"}']
